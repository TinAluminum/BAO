import pygame



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





class Entity():
    def __init__(self, mass, dimension, ini_position, static): # if static is true then the thing will just stay in place
        self.mass = mass
        self.dimension = dimension # (WIDTH, HEIGHT)
        self.vx = 0; self.vy = 0
        self.x = ini_position[0]
        self.y = ini_position[1]
        self.static = static
        # self.pg_obj = pygame.Rect(ini_position, 10, 10)




sim = Simulation()
object = Entity(10, (20, 20), (0, 0), False)
sim.add(object)
for i in range(60):
    sim.update_entity(object)
    print(object.y, object.vy)