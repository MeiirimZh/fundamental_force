from wave1 import *
from gameover import *

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if player.armor != 0:
            wave1()
        else:
            game_over()

    pygame.quit()


if __name__ == "__main__":
    main()
