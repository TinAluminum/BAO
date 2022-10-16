import pygame, os


background_color = (88, 107, 112)
screen_size = (1000, 600)


# Entities
bot = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'Ghost.png')), (54, 54))
small_platform = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'small_platform.png')), (120, 30))
main_platform = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'main_platform_2.png')), (900, 30))
doge = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'dodge.png')), (60, 60))



# Player velocity
VEL = 5