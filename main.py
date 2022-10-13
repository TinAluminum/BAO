import pygame, sys, pymunk, os
import constants as const

def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 60)
    space.add(body, shape)
    return shape

def draw_apples(apples, screen, apple_surface):
    for apple in apples:
        pygame.draw.circle(screen, (0,0,0), apple.body.position, 60)
        apple_rect = apple_surface.get_rect(center = apple.body.position)
        screen.blit(apple_surface, apple_rect)

def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (500, 500)
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_ball(balls, screen):
    for ball in balls:
        pygame.draw.circle(screen, (0, 0, 0), ball.body.position, 50)

def main():
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('BAO physic engine test')
    clock = pygame.time.Clock()
    run = True
    space = pymunk.Space()
    space.gravity = (0, 100)
    apple_surface = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'Apple.gif')), (250, 250))
    apples = []


    balls = []
    balls.append(static_ball(space))

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                apples.append(create_apple(space, event.pos))

        screen.fill(const.background_color)

        draw_apples(apples, screen, apple_surface)
        draw_static_ball(balls, screen)
        space.step(1/50)
        pygame.display.update()

main()




