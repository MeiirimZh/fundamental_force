import random
import pygame

pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force")

bg = pygame.image.load('SpaceBg.jpg').convert()

font = pygame.font.Font('BebasNeue-Regular.ttf', 32)
info_font = pygame.font.Font('BebasNeue-Regular.ttf', 18)

class Player:
    def __init__(self, x, y, speed, armor):
        self.sprite = pygame.image.load('FlavioShip.png')

        self.x = x
        self.y = y
        self.speed = speed

        self.armor = armor

        self.reload_time = 300
        self.last_time_shot = 0

beams = []
enemy_beams = []

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

    def change_direction(self, current_time):
        enemy_beams.append(SoldierBeam(self.x, self.y, 1))
        self.checkpoint_time = current_time
        if self.direction == 'R':
            self.direction = 'L'
        else:
            self.direction = 'R'
        self.movement_duration = random.randint(3, 5)

player = Player(450, 400, 1, 3)

entropy_soldiers = []

enemy_count = 20

last_enemy_spawn_time = 0

help_text = (info_font.render('Move: [Arrows]', True, (255, 255, 255)),
             info_font.render('Shoot: [A]', True, (255, 255, 255)))

def reset_game():
    global beams, enemy_beams, \
        player, entropy_soldiers, \
        enemy_count, last_enemy_spawn_time
    beams = []
    enemy_beams = []
    player.armor = 3
    player.x = 450
    player.y = 400
    entropy_soldiers = []
    enemy_count = 20
    last_enemy_spawn_time = 0

def wave1():
    global enemy_count, last_enemy_spawn_time

    current_time = pygame.time.get_ticks()

    armor_text = font.render(f'Armor: {player.armor}', True, (255, 255, 255))

    enemy_count_text = font.render(f'Enemies: {enemy_count}', True, (255, 255, 255))

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

        if player.x <= soldier.x + 71 and soldier.x <= player.x + 59 and player.y <= soldier.y + 79 and soldier.y <= player.y + 61:
            if not soldier.has_collied:
                player.armor -= 1
                soldier.has_collied = True
        else:
            soldier.has_collied = False

    screen.blit(armor_text, (10, 10))
    screen.blit(enemy_count_text, (10, 50))
    screen.blit(help_text[0], (10, 500))
    screen.blit(help_text[1], (10, 520))

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
            player.armor -= 1

    pygame.display.flip()