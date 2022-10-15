import pygame, os


class Simulation():
    def __init__(self):
        self.gravity = 1000
        self.shed = []
        self.dt = 1/60

    def add(self, new_entity):
        self.shed.append(new_entity)

    def update_entity(self, entity):
        assert isinstance(entity, Entity) # need to change later
        entity.vy += self.gravity * self.dt
        entity.pg.y += entity.vy * self.dt

    def step(self):
        for entity in self.shed:
            if entity.static is False:
                self.update_entity(entity)
                self.check_collision()

    def check_collision(self):
        collision_tolerance = 20
        master = self.shed[1]
        assert isinstance(master, Entity)
        platform = self.shed[0]
        if master.pg.colliderect(platform.pg):
            print('COLLIDE')
            print(abs(platform.pg.top - master.pg.bottom))
            print(master.vy)
            if abs(platform.pg.top - master.pg.bottom) < collision_tolerance:
                print('HOLD')
                master.pg.y = platform.pg.y-54
                master.vy = 0



class Entity():
    def __init__(self, mass, dimension, ini_position, image, static): # if static is true then the thing will just stay in place
        self.mass = mass
        self.dimension = dimension # (WIDTH, HEIGHT)
        self.vx = 0; self.vy = 0
        self.static = static
        self.pg_pic = image
        self.pg = pygame.Rect(ini_position[0], ini_position[1], dimension[0], dimension[1])





