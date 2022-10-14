import pygame, simu
import constants as const


def main():
    screen = pygame.display.set_mode(const.screen_size)
    pygame.display.set_caption('BAO')
    clock = pygame.time.Clock()

    sim = simu.Simulation()
    test = simu.Entity(10, (10, 10), (500, 0), True)

    sim.add(test)

    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(const.background_color)
        screen.blit(const.bot, (test.x, test.y))

        sim.update_entity(test)
        pygame.display.update()

main()




