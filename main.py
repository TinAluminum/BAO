import pygame
import constants as const


def main():
    screen = pygame.display.set_mode(const.screen_size)
    pygame.display.set_caption('BAO collision test')
    clock = pygame.time.Clock()
    run = True

    moving_rect = pygame.Rect(350, 350, 100, 100)
    x_speed, y_speed = 5,4

    other_rect = pygame.Rect(300, 600, 200, 100)
    other_speed = 2

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(const.background_color)
        pygame.draw.rect(screen, (255, 255, 255), moving_rect)
        pygame.draw.rect(screen, (255, 0, 0), other_rect)

        pygame.display.flip()

main()




