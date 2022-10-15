import pygame, simu
import constants as const

def draw_entities(simulation, screen):
    for entity in simulation.shed:
        screen.blit(entity.pg_pic, (entity.pg.x, entity.pg.y))

def entities_creation(sim):
    main_platform = simu.Entity(100, (900, 30), (50, 300), const.main_platform, True)
    player = simu.Entity(10, (54, 54), (500, 0), const.bot, False)
    big_guy = simu.Entity(10, (60, 60), (600, 0), const.doge, False)

    sim.add(main_platform)
    sim.add(player)

def handle_master_movement(master, keys_pressed):
    if keys_pressed[pygame.K_a]:  # LEFT
        master.pg.x -= const.VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        master.pg.x += const.VEL
    if keys_pressed[pygame.K_w]:  # UP
        master.pg.y -= 10
    if keys_pressed[pygame.K_s]:  # DOWN
        master.pg.y += const.VEL

def main():
    screen = pygame.display.set_mode(const.screen_size)
    pygame.display.set_caption('BAO')
    clock = pygame.time.Clock()

    sim = simu.Simulation()
    entities_creation(sim)
    value = 1
    valueX = -1

    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sim.shed[-1].pg.x, sim.shed[1].pg.y = event.pos[0], event.pos[1]
                sim.shed[-1].vy = 0

        keys_pressed = pygame.key.get_pressed()
        handle_master_movement(sim.shed[-1], keys_pressed)

        screen.fill(const.background_color)

        draw_entities(sim, screen)


        if sim.shed[0].pg.y >= 450:
            value = -3
        if sim.shed[0].pg.y <= 200:
            value = 3
        if sim.shed[0].pg.x == 20:
            print("HITUKJBCKHB")
            valueX = 1
        if sim.shed[0].pg.x == 80:
            valueX = -1

        sim.shed[0].pg.y += value
        sim.shed[0].pg.x += valueX

        sim.step()
        pygame.display.update()

main()




