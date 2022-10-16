import pygame, simu
import constants as const

def draw_entities(simulation, screen):
    for entity in simulation.shed["Static"]:
        screen.blit(entity.pg_pic, (entity.pg.x, entity.pg.y))
    for entity in simulation.shed["Dynamic"]:
        screen.blit(entity.pg_pic, (entity.pg.x, entity.pg.y))

def case_1(sim):
    player = simu.Entity(10, (54, 54), (500, 0), const.bot, False)
    main_platform = simu.Entity(100, (900, 30), (50, 500), const.main_platform, True)
    small_platform = simu.Entity(10, (120, 60), (440, 200), const.small_platform, True)
    small_platform2 = simu.Entity(10, (120, 60), (700, 350), const.small_platform, True)
    small_platform3 = simu.Entity(10, (120, 60), (200, 350), const.small_platform, True)
    doge = simu.Entity(10, (60, 60), (300, 0), const.doge, False)
    sim.add(main_platform)
    sim.add(small_platform)
    sim.add(small_platform2)
    sim.add(small_platform3)


    sim.add(doge)
    sim.add(player)

def entities_creation(sim):
    case_1(sim)

def handle_master_movement(master, keys_pressed):
    if keys_pressed[pygame.K_a]:  # LEFT
        master.pg.x -= const.VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        master.pg.x += const.VEL
    if keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_w]:  # UP
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
        master = sim.shed['Dynamic'][-1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                master.pg.x, master.pg.y = event.pos[0], event.pos[1]
                master.vy = 0

        keys_pressed = pygame.key.get_pressed()
        handle_master_movement(master, keys_pressed)

        screen.fill(const.background_color)

        draw_entities(sim, screen)

        sim.step()
        pygame.display.update()

main()




