import pygame
import os
import json
from pygame.locals import *
from coin import Coin


class IntButton():
    def __init__(self, x, y):
        self.image = pygame.image.load('../assets/intbutton.png')
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, dx, dy, screen, player):
        if player.get_interact() == True:
            # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            screen.blit(self.image, self.rect)
        self.rect.x = dx
        self.rect.y = dy

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == 1:
            self.image = pygame.image.load('../assets/arrow.png')
            self.image = pygame.transform.scale(self.image, (25, 10))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if direction == -1:
            self.image = pygame.image.load('../assets/arrow.png')
            self.image = pygame.transform.scale(self.image, (25, 10))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        self.direction = direction
        self.speed = 10

    def update(self, world):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 990:
            self.kill()
        for tile in world.tile_list:
            if tile[2] in ["wall", "ground", "gate", "trap", "spikes", ]:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    break


class Firebolt(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == 1:
            self.image = pygame.image.load('../assets/firebolt.png')
            self.image = pygame.transform.scale(self.image, (30, 20))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if direction == -1:
            self.image = pygame.image.load('../assets/firebolt.png')
            self.image = pygame.transform.scale(self.image, (30, 20))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        self.direction = direction
        self.speed = 15

    def update(self, world):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 990:
            self.kill()
        for tile in world.tile_list:
            if tile[2] in ["wall", "ground", "gate", "trap", "spikes", ]:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    break

class Player():
    def __init__(self, x, y, cast):
        self.arrows = []
        self.firebolts = []
        self.images_right = []
        self.images_left = []
        self.images_attack_right = []
        self.images_attack_left = []
        self.attack_index = 0
        self.attack_counter = 0
        self.attack_range = pygame.Rect(0, 0, 0, 0)
        self.index = 0
        self.counter = 0
        self.__cast = cast
        for num in range(1, 8):
            img_right = pygame.image.load(f'../assets/{self.__cast}{num}.png')
            img_right = pygame.transform.scale(img_right, (45, 75))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        for num in range(0, 4):
            img_attack_right = pygame.image.load(f'../assets/{self.__cast}attack{num}.png')
            img_attack_right = pygame.transform.scale(img_attack_right, (45, 75))
            img_attack_left = pygame.transform.flip(img_attack_right, True, False)
            self.images_attack_right.append(img_attack_right)
            self.images_attack_left.append(img_attack_left)
        self.idle_right = pygame.image.load(f'../assets/{self.__cast}idle.png')
        self.hurt_img = pygame.image.load(f'../assets/Knighthurt.png')
        self.hurt_img = pygame.transform.scale(self.hurt_img, (45, 75))
        self.idle_right = pygame.transform.scale(self.idle_right, (45, 75))
        self.idle_left = pygame.transform.flip(self.idle_right, True, False)
        self.image = self.idle_right
        self.hurt = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.__exit_reached = False
        self.interact = False
        self.pressinge = False
        self.__current_map = 0
        self.itemname = ''
        self.__currency = 0
        self.__inventory = []
        self.dmgcd = 0
        self.hurt_sound = pygame.mixer.Sound('../assets/damage_se.mp3')
        self.hurt_sound.set_volume(0.3)
        self.__str = 3
        self.__dex = 2
        self.__int = 1
        self.__char = 2
        self.__xp = 0
        self.__armor = 5
        self.__hp = 10
        self.__mana = 10
        self.__max_mana = 10
        self.__max_hp = 10
        self.onground = False
        self.direction = 0
        self.lvl = 1
        self.attacking = False
        self.attackspeed = 5
        print('szint:', self.lvl)

    def lvlup(self):
        if self.get_cast() == 'Knight':
            self.__str += 3
            self.__int += 1
            self.__dex += 2
            self.__char += 2
            self.__hp += 8
            self.__mana += 3
            self.lvl += 1
        elif self.get_cast() == 'Wizard':
            self.__str += 1
            self.__int += 4
            self.__dex += 2
            self.__char += 2
            self.__hp += 3
            self.__mana += 10
            self.lvl += 1
        elif self.get_cast() == 'Rogue':
            self.__str += 2
            self.__int += 1
            self.__dex += 3
            self.__char += 3
            self.__hp += 5
            self.__mana += 5
            self.lvl += 1
        else:
            pass

    def reset_progress(self):
        if os.path.exists('../data/player_data.json'):
            os.remove('../data/player_data.json')

    def set_pressinge(self, value):
        self.pressinge == value

    def get_itemname(self):
        return self.itemname

    def set_itemname(self, name):
        self.itemname = name

    def set_lvl(self, value):
        self.lvl += value

    def get_lvl(self):
        return self.lvl

    def get_interact(self):
        return self.interact

    def get_current_map(self):
        return self.__current_map

    def set_current_map(self, value):
        self.__current_map = value

    def get_exit_reached(self):
        return self.__exit_reached

    def set_exit_reached(self, value):
        self.__exit_reached = value

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        self.__hp += value

    def set_mana(self, value):
        self.__mana = value

    def increase_mana(self, value):
        self.__mana += value

    def get_mana(self):
        return self.__mana

    def get_xp(self):
        return self.__xp

    def set_xp(self, value):
        self.__xp += value

    def set_cast(self, value):
        self.__cast = value

    def get_cast(self):
        return self.__cast

    def set_armor(self, value):
        self.__armor = value

    def get_armor(self):
        return self.__armor

    def set_str(self, value):
        self.__str = value

    def get_str(self):
        return self.__str

    def set_dex(self, value):
        self.__dex = value

    def get_dex(self):
        return self.__dex

    def set_int(self, value):
        self.__int = value

    def get_int(self):
        return self.__int

    def set_char(self, value):
        self.__char = value

    def get_char(self):
        return self.__char

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def pickup(self):
        print('picked up:' + self.itemname)

    def get_max_hp(self):
        return self.__max_hp

    def set_max_hp(self, value):
        self.__max_hp += value

    def get_max_mana(self):
        return self.__max_mana

    def set_max_mana(self, value):
        self.__max_mana += value

    def load(self):
        data = None

        try:
            with open('../data/player_data.json', 'r') as file:
                data = json.load(file)
            self.set_cast(data['class'])
            self.set_lvl(data['level'])
            self.set_xp(data['xp'])
            self.set_hp(data['hp'])
            self.set_mana(data['mana'])
            self.set_armor(data['armor'])
            self.set_str(data['str'])
            self.set_dex(data['dex'])
            self.set_int(data['int'])
            self.set_char(data['char'])
            self.set_current_map(data['map'])
        except OSError as e:
            print(e.errno)

    def save(self):
        file_path = '../data/player_data.json'

        data = {
            "class": self.__cast,
            "level": self.lvl,
            "xp": self.__xp,
            "hp": self.__hp,
            "mana": self.__mana,
            "armor": self.__armor,
            "str": self.__str,
            "dex": self.__dex,
            "int": self.__int,
            "char": self.__char,
            "map": self.__current_map
        }

        if os.path.exists(file_path):
            with open(file_path, 'w') as outfile:
                json.dump(data, outfile, indent=4)
        else:
            with open(file_path, 'a') as outfile:
                json.dump(data, outfile, indent=4)
    arrow_group = pygame.sprite.Group()
    firebolt_group = pygame.sprite.Group()
    
    def attack(self):
        if self.attacking == True:
            if self.direction == 1:
                self.attack_range = pygame.Rect(self.rect.x + self.rect.width, self.rect.y, 30, self.rect.height)
            elif self.direction == -1:
                self.attack_range = pygame.Rect(self.rect.x, self.rect.y, 30, self.rect.height)

            if self.attack_index >=len(self.images_attack_right) or self.attack_index >= len(self.images_attack_left) :
                self.attack_index = 0
                if self.get_cast() == 'Rogue':
                        arrow = Arrow(self.rect.x + self.rect.width, self.rect.centery, self.direction)
                        self.arrow_group.add(arrow)
                elif self.get_cast() == 'Wizard':
                        firebolt = Firebolt(self.rect.x + self.rect.width, self.rect.centery, self.direction)
                        self.firebolt_group.add(firebolt)
                self.attacking = False
                self.attack_range = pygame.Rect(0, 0, 0, 0)
                return

            if self.direction == 1:
                self.image = self.images_attack_right[self.attack_index]
            elif self.direction == -1:
                self.image = self.images_attack_left[self.attack_index]

            self.attack_counter += 1
            if self.attack_counter >= self.attackspeed:
                self.attack_index += 1
                self.attack_counter = 0


    def update(self, screen_height, screen, world, coins):
        dx = 0
        dy = 0
        walk_cooldown = 5
        if self.attacking:
        	self.attack()

        if self.dmgcd > 0:
            self.dmgcd -=1

        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.onground == True:
            self.vel_y = -20
            self.onground = False

        # átírtam az ugrást, hogy a collisiont érzékelje és csak akkor ugorhasson, ha a talajjal ütközik
        if key[pygame.K_LEFT]:
            dx -= 5
            self.direction = -1
            self.counter += 1

        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1

        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and self.attacking == False:
            self.counter = 0
            self.index = 0
            if self.hurt == True:
                self.image = self.hurt_img
                self.hurt = False
            else:
                if self.direction == 1:
                    self.image = self.idle_right
                if self.direction == -1:
                    self.image = self.idle_left

        if key[pygame.K_LEFT] == True and key[pygame.K_RIGHT] == True and self.attacking == False:
            self.counter = 0
            self.index = 0
            if self.hurt == True:
                self.image = self.hurt_img
                self.hurt = False
            else:
                if self.direction == 1:
                    self.image = self.idle_right
                if self.direction == -1:
                    self.image = self.idle_left

        if key[pygame.K_SPACE]:
            self.attacking = True

        # anim
        if self.counter > walk_cooldown and self.attacking == False:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        # draw player onto screen
        screen.blit(self.image, self.rect)

        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        # check for collision
        # a collision egy az egyben jó volt, csak elöször véletlen a lvlup()-ba raktam XD
        for tile in world.tile_list:
            # check for collision in x direction
            if tile[2] == "entrance":
                self.interact = False
                continue
            elif tile[2] == "sword":
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    self.interact = True
                    self.itemname = 'sword'
            elif tile[2] == "bow":
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    self.interact = True
                    self.itemname = 'bow'
            elif tile[2] == "staff":
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    self.interact = True
                    self.itemname = 'staff'
            elif tile[2] == "exit" or tile[2] == "blood" or tile[2] == "wall" or tile[2] == "ground" or tile[2] == 'gate':
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                    # csekkolja h a pálya exit megvan-e találva - Márk
                    if tile[2] == "exit":
                        self.set_exit_reached(True)
                        self.itemname = ''
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        # ezt írtam hozzá, hogy ha a talajjal érintkezik akkor igaz legyen az onground ami engedi ugrani.
                        self.onground = True
            elif tile[2] == "spikes":
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.onground = True

                        #if self.dmgcd <= 25 and self.dmgcd > 0:
                            #self.dmgcd -= 1
                        if self.dmgcd <= 0:
                            if self.get_hp() - (self.get_max_hp() // 3) >= 0:
                                self.image = self.hurt_img
                                self.set_hp(-(self.get_max_hp() // 3))
                                self.hurt = True
                                self.hurt_sound.play()

                                self.dmgcd = 25
                            else:
                                self.set_hp(-self.get_hp())
                                self.image = self.hurt_img
                                self.hurt = True
                                self.hurt_sound.play()
            elif tile[2] == "trap":
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                    #if self.dmgcd <= 25 and self.dmgcd > 0:
                        #self.dmgcd -= 1
                    if self.dmgcd == 0:
                        if self.get_hp() - (self.get_max_hp() // 3) >= 0:
                            self.image = self.hurt_img
                            self.set_hp(-(self.get_max_hp() // 3))
                            self.hurt = True
                            self.dmgcd = 25
                            self.hurt_sound.play()
                        else:
                            self.set_hp(-self.get_hp())
                            self.image = self.hurt_img
                            self.hurt = True
                            self.hurt_sound.play()


                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

                        #if self.dmgcd <= 25 and self.dmgcd > 0:
                            #self.dmgcd -= 1
                        if self.dmgcd == 0:
                            if self.get_hp() - (self.get_max_hp() // 3) >= 0:
                                self.image = self.hurt_img
                                self.set_hp(-(self.get_max_hp() // 3))
                                self.hurt = True
                                self.dmgcd = 25
                                self.hurt_sound.play()
                            else:
                                self.set_hp(-self.get_hp())
                                self.image = self.hurt_img
                                self.hurt = True
                                self.hurt_sound.play()


                        # ezt írtam hozzá, hogy ha a talajjal érintkezik akkor igaz legyen az onground ami engedi ugrani.
                        self.onground = True


        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        # coin felvétel - Márk
        for coin in coins:
            if coin.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):

                coin_sound = pygame.mixer.Sound('../assets/coin_se.mp3')
                coin_sound.set_volume(0.1)
                coin_sound.play()
                coins.remove(coin)
                self.__currency += 1
                print('MONEY: %d ' % self.__currency)

    # LEVELING
        if self.get_xp() >= 10 and self.get_lvl() < 2:
            self.lvlup()
        if self.get_xp() >= 20 and self.get_lvl() < 3:
            self.lvlup()
        if self.get_xp() >= 30 and self.get_lvl() < 4:
            self.lvlup()
        if self.get_xp() >= 40 and self.get_lvl() < 5:
            self.lvlup()
