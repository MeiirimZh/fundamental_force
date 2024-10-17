import pygame


pygame.init()

screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Fundamental Force - You won!")

bg = pygame.image.load('SpaceBg.jpg').convert()

font = pygame.font.Font('BebasNeue-Regular.ttf', 40)
font_2 = pygame.font.Font('BebasNeue-Regular.ttf', 20)

win_text = font.render('You won!', True, (255, 255, 255))
exit_text = font_2.render('Press [Esc] to quit the game', True, (255, 255, 255))

def win():
    screen.blit(bg, (0, 0))
    screen.blit(win_text, (400, 270))
    screen.blit(exit_text, (366, 330))

    pygame.display.flip()
