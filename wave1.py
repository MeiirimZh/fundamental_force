import random
import pygame

# Configuring the window
pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force")

# Images
bg = pygame.image.load('SpaceBg.jpg').convert()
flavio_ship = pygame.image.load('FlavioShip.png')

# Fonts
font = pygame.font.Font('BebasNeue-Regular.ttf', 32)
info_font = pygame.font.Font('BebasNeue-Regular.ttf', 18)

# Sprite collections
beams = []
enemy_beams = []
entropy_soldiers = []

class Player:
    def __init__(self, sprite, x, y, speed, armor):
        self.sprite = sprite
        
        self.width = sprite.get_size()[0]
        self.height = sprite.get_size()[1]

        self.x = x
        self.y = y
        self.speed = speed

        self.armor = armor

        self.reload_time = 300
        self.last_time_shot = 0

        self.rush_reload = 10
        self.rush_duration = 5
        self.last_time_rushed = 0

        self.can_rush = False

class Beam:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('BlueBeam1.png')

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y -= self.speed

class SoldierBeam:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('RedBeam1.png')

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

class EntropySoldier:
    def __init__(self, speed):
        self.sprite = pygame.image.load('EntropySoldier.png')

        self.direction = random.choice(('R', 'L'))
        self.movement_duration = random.randint(3, 5)

        self.checkpoint_time = 0

        self.has_collied = False

        self.x = random.randint(100, 800)
        self.y = -20
        self.speed = speed

        enemy_beams.append(SoldierBeam(self.x+23, self.y, 1))

    def move(self):
        self.y += self.speed

player = Player(flavio_ship,450, 400, 1, 5)

enemy_count = 20

last_enemy_spawn_time = 0

rush = False

help_text = (info_font.render('Move: [Arrows]', True, (255, 255, 255)),
             info_font.render('Shoot: [A]', True, (255, 255, 255)),
             info_font.render('Rush: [S]', True, (255, 255, 255)))

game_won = False

start_time = 0

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
    enemy_count = 20
    last_enemy_spawn_time = 0
    start_time = pygame.time.get_ticks()
    player.last_time_rushed = 0
    rush = False

def wave1():
    global start_time, last_enemy_spawn_time, rush, game_won, enemy_count

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    armor_text = font.render(f'Armor: {player.armor}', True, (255, 255, 255))

    enemy_count_text = font.render(f'Enemies: {enemy_count}', True, (255, 255, 255))

    if round(elapsed_time/1000)-player.last_time_rushed < player.rush_reload:
        rush_text = font.render(f'Rush: {player.rush_reload-(round(elapsed_time/1000)-player.last_time_rushed)}', True, (255, 255, 255))
    else:
        rush_text = font.render('Rush: READY', True, (255, 255, 255))
        player.can_rush = True

    keys = pygame.key.get_pressed()
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
            beams.append(Beam(player.x + 15, player.y, 2))
            player.last_time_shot = current_time

    if keys[pygame.K_s]:
        if player.can_rush:
            player.last_time_rushed = round(elapsed_time / 1000)
            rush = True

    if rush:
        rush_text = font.render('Rush: EXECUTING', True, (255, 255, 255))
        if round(elapsed_time/1000) - player.last_time_rushed == player.rush_duration:
            rush = False
            player.last_time_rushed += player.rush_duration
            player.can_rush = False

    screen.blit(bg, (0, 0))

    if round(current_time/1000) - last_enemy_spawn_time == 1 and len(entropy_soldiers) < enemy_count:
        entropy_soldiers.append(EntropySoldier(0.5))
        last_enemy_spawn_time = round(current_time/1000)
    else:
        last_enemy_spawn_time = round(current_time / 1000)

    for soldier in entropy_soldiers:
        screen.blit(soldier.sprite, (soldier.x, soldier.y))
        soldier.move()
        if soldier.y >= 600:
            entropy_soldiers.remove(soldier)

        if rush:
            soldier.speed = 2

        if not rush:
            if player.x <= soldier.x + 71 and soldier.x <= player.x + 59 and player.y <= soldier.y + 79 and soldier.y <= player.y + 61:
                if not soldier.has_collied:
                    player.armor -= 1
                    soldier.has_collied = True
            else:
                soldier.has_collied = False
        else:
            if player.x <= soldier.x + 71 and soldier.x <= player.x + 59 and player.y <= soldier.y + 79 and soldier.y <= player.y + 61:
                if not soldier.has_collied:
                    entropy_soldiers.remove(soldier)
                    enemy_count -= 1
            else:
                soldier.has_collied = False

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
            if beam.x in range(int(soldier.x), int(soldier.x)+71) and beam.y in range(int(soldier.y), int(soldier.y)+79):
                beams.remove(beam)
                entropy_soldiers.remove(soldier)
                enemy_count -= 1

    for enemy_beam in enemy_beams:
        enemy_beam.move()
        screen.blit(enemy_beam.sprite, (enemy_beam.x, enemy_beam.y))
        if (player.x <= enemy_beam.x + 30) and (enemy_beam.x <= player.x + 59) and (player.y <= enemy_beam.y + 127) and (enemy_beam.y <= player.y + 61):
            enemy_beams.remove(enemy_beam)
            if not rush:
                player.armor -= 1

        if rush:
            enemy_beam.speed = 4

    pygame.display.flip()