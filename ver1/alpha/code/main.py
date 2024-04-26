import pygame
from maps import Maps
from pygame import *
from world import World
from player import Player
from coin import Coin
from menu import *

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_HEIGHT = 990
SCREEN_WIDTH = 990
tile_size = 30

#kis háttér zene - Márk
pygame.mixer.music.load('../assets/menu_theme.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

bg_img = pygame.image.load("../assets/bg.png")
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Display():
    def __init__(self,txt, x, y, font_size):
        self.text = txt
        font = pygame.font.Font(None, font_size)
        text = font.render(txt, True, (255, 255, 255))
        screen.blit(text, (x, y))


map = Maps()
world = World(map.load_world_from_file())
player = Player(*map.get_player_pos(1))
coins_pos = map.get_coins_pos(1)
coins = [Coin(*pos) for pos in coins_pos]
myMenu = Menu(screen)

run = True
'''
update_count = 0
max_updates = 5
'''
current_map = 0

while run:
    
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    

    if myMenu.get_visible():
        title1 = Display('Platfomer', SCREEN_WIDTH // 2 - 190, SCREEN_HEIGHT // 2 - 200, 100)
        title2 = Display('The Game', SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 120, 70)
        if myMenu.get_exit_btn().draw():
            run = False
        if myMenu.get_load_btn().draw():
            pass
        if myMenu.get_play_btn().draw():
            myMenu.set_visible(False)
            continue
    else:
        
        for coin in coins:
            coin.counter += 1
            coin.animate()

        world.draw()
        player.update(SCREEN_HEIGHT, screen, world,coins)
        # hozzáadtam a world-öt a player update metódusába és átadom itt azt is neki, innen kapja meg a tile-ek rect-jét a player
        
        #ez veszi le a coin-t - Márk
        if player.get_coin_touched():
            for coin in coins:
                if player.get_touched_coin_x() == coin.rect.x:
                    coins.remove(coin)
            player.set_coin_touched(False)
            player.set_touched_coin_x(0)


        if player.get_exit_reached():
            current_map += 1
            if current_map <= 4:
                map.set_map(current_map)
                x = current_map
                world = World(map.load_world_from_file())
                player = Player(*map.get_player_pos(x))
                player.set_current_map(current_map)
                player.set_exit_reached(False)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player.lvlup()
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()


pygame.mixer.quit()
pygame.quit()
