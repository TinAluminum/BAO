import pygame
import constants as const


def main():
    screen = pygame.display.set_mode(const.screen_size)
    pygame.display.set_caption('BAO')
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(const.background_color)


        pygame.display.update()

main()




