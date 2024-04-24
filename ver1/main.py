import pygame
from pygame import *
from world import World
from player import Player
from coin import Coin
from map1 import world_data as world_data_1, object_positions as object_positions_1
from map2 import world_data as world_data_2, object_positions as object_positions_2
from map3 import world_data as world_data_3, object_positions as object_positions_3
from map4 import world_data as world_data_4, object_positions as object_positions_4
from map5 import world_data as world_data_5, object_positions as object_positions_5

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 990
screen_height = 990

screen_number = 1  # Change this value to switch between maps

screen = pygame.display.set_mode((screen_width, screen_height))
# Set the correct caption
pygame.display.set_caption('Operation Hoot-Hoot')

# define game variables
tile_size = 30

# load images
bg_img = pygame.image.load('img/bg.png')


class Display():
    def __init__(self, txt, x, y, font_size=30):
        self.text = txt
        font = pygame.font.Font(None, font_size)
        text = font.render(txt, True, (255, 0, 0))
        screen.blit(text, (x, y))

    def update(self, txt, x, y, font_size=30):
        self.text = txt
        font = pygame.font.Font(None, font_size)
        text = font.render(txt, True, (255, 0, 0))
        screen.blit(text, (x, y))


# def display_text(txt, x, y, font_size=30):
#    font = pygame.font.Font(None, font_size)
#   text = font.render(txt, True, (255, 0, 0))
#  screen.blit(text, (x, y))


#def map_choice():
    #    choice = ''
        #    while True:
        #        screen.fill((0, 0, 0))
        #        question = Display("Which map do you choose?", 350, 500)
        #        input = Display(choice, 650, 500)
        #        pygame.display.update()
        #        for event in pygame.event.get():
        #            if event.type == pygame.KEYDOWN:
        #                if event.key == pygame.K_RETURN:
        #                    return int(choice)
        #                elif event.key == pygame.K_BACKSPACE:
        #                    choice = choice[:-1]
        #                    input.update(choice, 650, 500)
        #                    print(choice)
        #                elif event.key == pygame.K_ESCAPE:
        #                    return False
        #                else:
        #                    choice += event.unicode
        #            elif event.type == pygame.QUIT:
#                return None


#screen_number = map_choice()

if screen_number == 1:
    world_data = world_data_1
    object_positions = object_positions_1
elif screen_number == 2:
    world_data = world_data_2
    object_positions = object_positions_2
elif screen_number == 3:
    world_data = world_data_3
    object_positions = object_positions_3
elif screen_number == 4:
    world_data = world_data_4
    object_positions = object_positions_4
elif screen_number == 5:
    world_data = world_data_5
    object_positions = object_positions_5

world = World(world_data)
player1 = Player(*object_positions()[0])
coin_positions = object_positions()[1]
coins = [Coin(*pos) for pos in coin_positions]  # Create coins from positions

run = True
update_count = 0
max_updates = 5

while run:

    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    world.draw()
    # world.animate()

    for coin in coins:
        coin.counter += 1
        coin.animate()

    player1.update(screen_height, screen, world)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
             player1.lvlup()
            if event.key == pygame.K_n:
                screen_number += 1
                if screen_number > 5:  # Loop back to level 1 if screen_number exceeds 5
                    screen_number = 1
                if screen_number == 1:
                    world_data = world_data_1
                    object_positions = object_positions_1
                elif screen_number == 2:
                    world_data = world_data_2
                    object_positions = object_positions_2
                elif screen_number == 3:
                    world_data = world_data_3
                    object_positions = object_positions_3
                elif screen_number == 4:
                    world_data = world_data_4
                    object_positions = object_positions_4
                elif screen_number == 5:
                    world_data = world_data_5
                    object_positions = object_positions_5
                world = World(world_data)
                player1 = Player(*object_positions()[0])
                coin_positions = object_positions()[1]
                coins = [Coin(*pos) for pos in coin_positions]  # Create coins from positions

    pygame.display.update()

pygame.quit()
