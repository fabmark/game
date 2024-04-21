import pygame
from world import World

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Map2')

#define game variables
tile_size = 20

#load images
bg_img = pygame.image.load('img/bg.png')

def load_world_from_file(filename):
    with open(filename, 'r') as file:
        world_data = []
        for line in file:
            world_data.append(list(map(int, line.split())))
    return world_data

world_data = load_world_from_file("map2.txt")
world = World(world_data)

run = True
while run:
    screen.blit(bg_img, (0, 0))
    world.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
