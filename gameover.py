import pygame
from wave1 import reset_game
from config import space_bg_1, font_40, font_20

pygame.init()

screen = pygame.display.set_mode((960, 600))

game_over_text = font_40.render('Game Over!', True, (255, 255, 255))
restart_text = font_20.render('Press [Space] to restart the wave', True, (255, 255, 255))

def game_over():
    screen.blit(space_bg_1, (0, 0))
    screen.blit(game_over_text, (400, 270))
    screen.blit(restart_text, (363, 330))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        reset_game()

    pygame.display.flip()