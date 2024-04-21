import pygame
from world import World
from player import Player
from coin import Coin

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Map1')

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

world_data = load_world_from_file("map1.txt")
world = World(world_data)
player1 = Player(100, screen_height - 130)
coin1 = Coin(200, 300)

run = True
update_count = 0
max_updates = 5  # Adjust this value to suit your needs

while run:
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    world.draw()
    #world.animate()

    Coin.counter += 1
    coin1.animate()
    player1.update(screen_height, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player1.lvlup()

    pygame.display.update()

pygame.quit()
