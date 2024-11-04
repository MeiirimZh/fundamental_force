import pygame
from config import space_bg_1, font_40, font_20

pygame.init()

screen = pygame.display.set_mode((960, 600))

win_text = font_40.render('You won!', True, (255, 255, 255))
exit_text = font_20.render('Press [Esc] to quit the game', True, (255, 255, 255))

def win(score):
    score_text = font_20.render(f'Scores: {score}', True, (255, 255, 255))

    screen.blit(space_bg_1, (0, 0))
    screen.blit(win_text, (400, 270))
    screen.blit(score_text, (415, 330))
    screen.blit(exit_text, (366, 355))

    pygame.display.flip()
