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
        entity.y += entity.vy * self.dt

    def step(self):
        for entity in self.shed:
            if entity.static is False:
                self.update_entity(entity)





class Entity():
    def __init__(self, mass, dimension, ini_position, image, static): # if static is true then the thing will just stay in place
        self.mass = mass
        self.dimension = dimension # (WIDTH, HEIGHT)
        self.vx = 0; self.vy = 0
        self.x = ini_position[0]
        self.y = ini_position[1]
        self.static = static
        self.pg_pic = image




