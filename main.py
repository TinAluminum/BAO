import pygame, simu
import constants as const

def draw_entities(simulation, screen):
    for entity in simulation.shed:
        screen.blit(entity.pg_pic, (entity.pg_obj.x, entity.pg_obj.y))

def entities_creation(sim):
    main_platform = simu.Entity(100, (900, 30), (50, 400), const.main_platform, True)
    player = simu.Entity(10, (54, 54), (500, 0), const.bot, False)
    big_guy = simu.Entity(10, (60, 60), (600, 0), const.doge, False)

    sim.add(main_platform)
    sim.add(player)



def main():
    screen = pygame.display.set_mode(const.screen_size)
    pygame.display.set_caption('BAO')
    clock = pygame.time.Clock()

    sim = simu.Simulation()
    entities_creation(sim)

    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(const.background_color)


        draw_entities(sim, screen)


        sim.step()
        pygame.display.update()

main()




