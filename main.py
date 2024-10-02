import pygame

pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force")

bg = pygame.image.load('SpaceBg.jpg').convert()

show_image = False

class Player:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('FlavioShip.png')

        self.x = x
        self.y = y
        self.speed = speed

beams = []

class Beam:
    def __init__(self, x, y, speed):
        self.sprite = pygame.image.load('BlueBeam1.png')

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y -= self.speed

player = Player(0, 0, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                beams.append(Beam(0, 0, 2))
                show_image = True
                beams[-1].x = player.x + 15
                beams[-1].y = player.y

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
    screen.blit(player.sprite, (player.x, player.y))

    for beam in beams[:]:
        beam.move()
        if beam.y < -60:
            beams.remove(beam)
        else:
            screen.blit(beam.sprite, (beam.x, beam.y))

    pygame.display.flip()
