import pygame
from wave1 import reset_game

pygame.init()

screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force - Game Over!")

bg = pygame.image.load('SpaceBg.jpg').convert()

font = pygame.font.Font('BebasNeue-Regular.ttf', 40)
font_2 = pygame.font.Font('BebasNeue-Regular.ttf', 20)

game_over_text = font.render('Game Over!', True, (255,255,255))
restart_text = font_2.render('Press [Space] to restart the wave', True, (255, 255, 255))

def game_over():
    screen.blit(bg, (0, 0))
    screen.blit(game_over_text, (400, 270))
    screen.blit(restart_text, (363, 330))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        reset_game()

    pygame.display.flip()