import pygame
from maps import Maps
from pygame import *
from world import World
from player import Player
from player import IntButton
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
main_sound = pygame.mixer.Sound('../assets/menu_theme.mp3')
main_sound.set_volume(0.05)
main_sound.play(-1)

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
player = Player(*map.get_player_pos(0))
coins_pos = map.get_coins_pos(1)
coins = [Coin(*pos) for pos in coins_pos]
myMenu = Menu(screen)
intButton = IntButton(player.get_x(),player.get_y()-60)

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
        
        hp_felirat = Display('Health: ' + str(player.get_hp()), 50, 50, 30)
        lvl_felirat = Display('Level: ' + str(player.get_lvl()), 180, 50, 30)
        xp_felirat = Display('XP: ' + str(player.get_xp()), 290, 50, 30)

        str_felirat = Display('Strength: ' + str(player.get_str()), 500,50,30)
        int_felirat = Display('Intelligence: ' + str(player.get_int()), 500,80,30)
        char_felirat = Display('Charisma: ' + str(player.get_char()), 650,50,30)
        dex_felirat = Display('Dexterity: ' + str(player.get_dex()), 650,80,30)
        class_felirat =Display('Class: ' + (player.get_class()), 800,80,30)
        if player.get_class() == 'Hobo':
            choose_class = Display('Choose your class!', 130,880,30)  
        if player.get_interact() == True:
            item_felirat = Display(player.get_itemname(),player.get_x(),player.get_y()-80, 20)

        
        world.draw()
        player.update(SCREEN_HEIGHT, screen, world,coins)
        intButton.update(player.get_x(),player.get_y()-60, screen, player)
        
        # hozzáadtam a world-öt a player update metódusába és átadom itt azt is neki, innen kapja meg a tile-ek rect-jét a player
        
        if player.get_exit_reached():
            current_map += 1
            if current_map <= 4:
                coins_pos = map.get_coins_pos(current_map + 1)
                coins = [Coin(*pos) for pos in coins_pos]
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
                player.set_xp(1)
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_e:
                if player.get_interact() and player.get_itemname() == 'sword':
                    print("Sword equipped")
                    player.set_class('knight')
                    for tile in list(world.tile_list):
                        if tile[2] == "sword" or tile[2] == "staff" or tile[2] == 'bow':
                            world.tile_list.remove(tile)
                elif player.get_interact() and player.get_itemname() == 'bow':
                    print("bow equipped")
                    player.set_class('Rogue')
                    for tile in list(world.tile_list):
                        if tile[2] == "sword" or tile[2] == "staff" or tile[2] == 'bow':
                            world.tile_list.remove(tile)
                elif player.get_interact() and player.get_itemname() == 'staff':
                    print("staff equipped")
                    player.set_class('Mage')
                    for tile in list(world.tile_list):
                        if tile[2] == "sword" or tile[2] == "staff" or tile[2] == 'bow':
                            world.tile_list.remove(tile)
                #player.set_pressinge(True)
                #print('e')
       # else:
           # player.set_pressinge(False)

    pygame.display.update()


pygame.mixer.quit()
pygame.quit()