import pygame
from player import Player
from player_beam import PlayerBeam
from common_enemy import CommonEnemy
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, basic_font, help_text,
    space_bg_1, flavio_ship, entropy_soldier_ship, blue_beam, enemy_red_beam)

# Configuring the window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sprite collections
beams = []
enemy_beams = []
entropy_soldiers = []

# Variables
enemy_count = 30
enemy_spawn_time = 1
last_enemy_spawn_time = 0
rush = False
game_won = False
start_time = 0

player = Player(flavio_ship,450, 400, 1, 5)

def reset_game():
    global start_time, beams, enemy_beams, \
        player, entropy_soldiers, \
        enemy_count, last_enemy_spawn_time, rush
    beams = []
    enemy_beams = []
    player.armor = 5
    player.x = 450
    player.y = 400
    entropy_soldiers = []
    enemy_count = 30
    last_enemy_spawn_time = 0
    start_time = pygame.time.get_ticks()
    player.last_time_rushed = 0
    rush = False

def wave1():
    global start_time, last_enemy_spawn_time, rush, game_won, enemy_count

    # Get time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    keys = pygame.key.get_pressed()

    # GUI
    armor_text = basic_font.render(f'Armor: {player.armor}', True, (255, 255, 255))
    enemy_count_text = basic_font.render(f'Enemies: {enemy_count}', True, (255, 255, 255))

    if round(elapsed_time/1000)-player.last_time_rushed < player.rush_reload:
        rush_text = basic_font.render(f'Rush: {player.rush_reload-(round(elapsed_time/1000)-player.last_time_rushed)}', True, (255, 255, 255))
    else:
        rush_text = basic_font.render('Rush: READY', True, (255, 255, 255))
        player.can_rush = True

    if keys[pygame.K_UP] and player.y >= 0:
        player.y -= player.speed
    elif keys[pygame.K_DOWN] and player.y <= 539:
        player.y += player.speed
    elif keys[pygame.K_RIGHT] and player.x <= 901:
        player.x += player.speed
    elif keys[pygame.K_LEFT] and player.x >= 0:
        player.x -= player.speed

    if keys[pygame.K_a]:
        if current_time - player.last_time_shot > player.reload_time:
            beams.append(PlayerBeam(blue_beam, player.x + 15, player.y, 2))
            player.last_time_shot = current_time

    if keys[pygame.K_s] and player.can_rush:
        player.last_time_rushed = round(elapsed_time / 1000)
        rush = True

    if rush:
        rush_text = basic_font.render('Rush: EXECUTING', True, (255, 255, 255))
        if round(elapsed_time/1000) - player.last_time_rushed == player.rush_duration:
            rush = False
            player.last_time_rushed += player.rush_duration
            player.can_rush = False

    screen.blit(space_bg_1, (0, 0))

    if round(current_time/1000) - last_enemy_spawn_time == enemy_spawn_time and len(entropy_soldiers) < enemy_count:
        entropy_soldiers.append(CommonEnemy(entropy_soldier_ship, enemy_beams, enemy_red_beam, 0.5))
        last_enemy_spawn_time = round(current_time/1000)
    else:
        last_enemy_spawn_time = round(current_time / 1000)

    for soldier in entropy_soldiers:
        screen.blit(soldier.sprite, (soldier.x, soldier.y))
        soldier.move()
        if soldier.y >= 600:
            entropy_soldiers.remove(soldier)

        if not rush:
            if player.x <= soldier.x + soldier.width and soldier.x <= player.x + player.hit_box_x and player.y <= soldier.y + soldier.height and soldier.y <= player.y + player.hit_box_y:
                if not soldier.has_collied:
                    player.armor -= 1
                    soldier.has_collied = True
            else:
                soldier.has_collied = False
        else:
            soldier.speed = 2
            if player.x <= soldier.x + soldier.width and soldier.x <= player.x + player.hit_box_x and player.y <= soldier.y + soldier.height and soldier.y <= player.y + player.hit_box_y:
                if not soldier.has_collied:
                    entropy_soldiers.remove(soldier)
                    enemy_count -= 1
            else:
                soldier.has_collied = False

    # Output texts
    screen.blit(armor_text, (10, 10))
    screen.blit(enemy_count_text, (10, 50))
    screen.blit(help_text[0], (10, 500))
    screen.blit(help_text[1], (10, 520))
    screen.blit(help_text[2], (10, 540))
    screen.blit(rush_text, (10, 90))

    screen.blit(player.sprite, (player.x, player.y))

    for beam in beams[:]:
        beam.move()
        if beam.y < -60:
            beams.remove(beam)
        else:
            screen.blit(beam.sprite, (beam.x, beam.y))

        for soldier in entropy_soldiers:
            if beam.x in range(int(soldier.x), int(soldier.x)+soldier.width) and beam.y in range(int(soldier.y), int(soldier.y)+soldier.height):
                beams.remove(beam)
                entropy_soldiers.remove(soldier)
                enemy_count -= 1

    for enemy_beam in enemy_beams:
        enemy_beam.move()
        screen.blit(enemy_beam.sprite, (enemy_beam.x, enemy_beam.y))
        if (player.x <= enemy_beam.x + enemy_beam.width) and (enemy_beam.x <= player.x + player.hit_box_x) and (player.y <= enemy_beam.y + enemy_beam.height) and (enemy_beam.y <= player.y + player.hit_box_y) and not rush:
            enemy_beams.remove(enemy_beam)
            player.armor -= 1

        if rush:
            enemy_beam.speed = 4

    pygame.display.flip()
