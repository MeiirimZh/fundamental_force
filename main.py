import wave1 as w1
from wave1 import *
from gameover import *
from win import *

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        if w1.enemy_count == 0:
            win()
        elif player.armor != 0:
            wave1()
        else:
            game_over()

if __name__ == "__main__":
    main()
