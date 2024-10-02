import pygame

pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force")

image = pygame.image.load('FlavioShip.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))

    pygame.display.update()