import pygame
from constants import *

def main():
    #game init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #handling fps
    clock = pygame.time.Clock()
    dt = 0

    #game loop start
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__== "__main__":
    main()
