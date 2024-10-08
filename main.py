import random

import pygame

pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force")

bg = pygame.image.load('SpaceBg.jpg').convert()

class Player:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('FlavioShip.png')

        self.x = x
        self.y = y
        self.speed = speed

        self.reload_time = 300
        self.last_time_shot = 0

beams = []

class Beam:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('BlueBeam1.png')

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y -= self.speed

class EntropySoldier:
    def __init__(self, speed):
        self.sprite = pygame.image.load('EntropySoldier.png')

        self.direction = random.choice(('R', 'L'))
        self.movement_duration = random.randint(1, 2)

        self.checkpoint_time = 0

        self.x = random.randint(150, 300)
        self.y = random.randint(150, 300)
        self.speed = speed

    def move(self):
        if self.direction == 'R':
            self.x += self.speed
        else:
            self.x -= self.speed

player = Player(0, 0, 1)
entropy_soldier = EntropySoldier(0.3)

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if current_time - player.last_time_shot > player.reload_time:
                    beams.append(Beam(player.x+15, player.y, 2))
                    player.last_time_shot = current_time

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.y >= 0:
        player.y -= player.speed
    elif keys[pygame.K_DOWN] and player.y <= 539:
        player.y += player.speed
    elif keys[pygame.K_RIGHT] and player.x <= 901:
        player.x += player.speed
    elif keys[pygame.K_LEFT] and player.x >= 0:
        player.x -= player.speed

    screen.blit(bg, (0, 0))
    entropy_soldier.move()
    if entropy_soldier.checkpoint_time + entropy_soldier.movement_duration == current_time:
        entropy_soldier.checkpoint_time = current_time
        entropy_soldier.direction = random.choice(('R', 'L'))
        entropy_soldier.movement_duration = random.randint(3, 5)

    screen.blit(player.sprite, (player.x, player.y))
    screen.blit(entropy_soldier.sprite, (entropy_soldier.x, entropy_soldier.y))

    for beam in beams[:]:
        beam.move()
        if beam.y < -60:
            beams.remove(beam)
        else:
            screen.blit(beam.sprite, (beam.x, beam.y))

    pygame.display.flip()
