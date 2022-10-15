import pygame, os


class Simulation():
    def __init__(self):
        self.gravity = 100
        self.shed = []
        self.dt = 1/60

    def add(self, new_entity):
        self.shed.append(new_entity)

    def update_entity(self, entity):
        assert isinstance(entity, Entity) # need to change later
        entity.vy += self.gravity * self.dt
        entity.pg_obj.y += entity.vy * self.dt

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
        if master.pg_obj.colliderect(platform.pg_obj):
            print('COLLIDE')
            print(abs(platform.pg_obj.top - master.pg_obj.bottom))
            print(master.vy)
            if abs(platform.pg_obj.top - master.pg_obj.bottom) < collision_tolerance:
                print('HOLD')
                master.static = True # Work for noe but need changes
                master.pg_obj.y = platform.pg_obj.y-54



class Entity():
    def __init__(self, mass, dimension, ini_position, image, static): # if static is true then the thing will just stay in place
        self.mass = mass
        self.dimension = dimension # (WIDTH, HEIGHT)
        self.vx = 0; self.vy = 0
        self.static = static
        self.pg_pic = image
        self.pg_obj = pygame.Rect(ini_position[0], ini_position[1], dimension[0], dimension[1])





