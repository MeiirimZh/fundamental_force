import pygame

pygame.init()
screen = pygame.display.set_mode((960, 600))

# Window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600

# Fonts
basic_font = pygame.font.Font('fonts/BebasNeue-Regular.ttf', 32)
info_font = pygame.font.Font('fonts/BebasNeue-Regular.ttf', 18)
font_40 = pygame.font.Font('fonts/BebasNeue-Regular.ttf', 40)
font_20 = pygame.font.Font('fonts/BebasNeue-Regular.ttf', 20)

# Text
help_text = (info_font.render('Move: [Arrows]', True, (255, 255, 255)),
             info_font.render('Shoot: [A]', True, (255, 255, 255)),
             info_font.render('Rush: [S]', True, (255, 255, 255)))

# Sounds
laser_sound_1 = pygame.mixer.Sound("sounds/laser_sound_1.mp3")

# Images
space_bg_1 = pygame.image.load('images/SpaceBg.jpg').convert()
flavio_ship = pygame.image.load('images/FlavioShip.png')
entropy_soldier_ship = pygame.image.load('images/EntropySoldier.png')
blue_beam = pygame.image.load('images/BlueBeam1.png')
enemy_red_beam = pygame.image.load('images/RedBeam1.png')
