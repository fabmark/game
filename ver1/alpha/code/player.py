import pygame
import json
import os
from pygame.locals import *
from coin import Coin

class Player():
	def __init__(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range (1, 9):			
			img_right = pygame.image.load(f'../assets/walk{num}.png')
			img_right = pygame.transform.scale(img_right, (30, 50))
			img_left = pygame.transform.flip(img_right, True, False)			
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.idle_right = pygame.image.load('../assets/IDLE.png')
		self.idle_right = pygame.transform.scale(self.idle_right, (30,50))
		self.idle_left = pygame.transform.flip(self.idle_right, True, False)
		self.image = self.idle_right
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		# __ <-- miatt privát láthatóságúak a változók - Márk
		self.__exit_reached = False
		self.__current_map = 0
		self.__currency = 0
		self.__inventory = []
		self.__cast = 'knight'
		self.__str = 3
		self.__dex = 2
		self.__int = 1
		self.__char = 2
		self.__xp = 0
		self.__hp = 1
		self.__armor = 5


		self.onground = False
		self.direction = 0
		self.lvl = 1
		print('szint:',self.lvl)


    #attributúmoknak majd kellenek getterek/setterek (pl. int) - Márk
	def get_current_map(self):
		return self.__current_map

	def set_current_map(self, value):
		self.__current_map = value

	def get_exit_reached(self):
		return self.__exit_reached

	def set_exit_reached(self, value):
		self.__exit_reached = value

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

	def get_hp(self):
		return self.__hp
	
	def set_hp(self, value):
		self.__hp += value

	def get_lvl(self):
		return self.lvl

	def set_lvl(self, value):
		self.lvl += value

	def set_cast(self, value):
		self.__cast = value
	
	def get_cast(self):
		return self.__cast

	def set_xp(self, value):
		self.__xp = value
	
	def get_xp(self):
		return self.__xp

	def load(self):
		pass
	
	def save(self):
		file_path = '../data/player_data.json'

		data = {
			"class": "knight",
			"level": 1,
			"xp": 0,
			"hp": 10,
			"armor": 5,
			"str": 3,
			"dex": 2,
			"int": 10,
			"char": 2
		}

		if os.path.exists(file_path):
			with open('player_data.json', 'w') as outfile:
				json.dump(data, outfile, indent=4)
		else:
			with open('player_data.json', 'a') as outfile:
				json.dump(data, outfile, indent=4)
		
		pass

	def update(self,screen_height,screen,world,coins):
		dx = 0
		dy = 0
		walk_cooldown = 5

		#get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.onground == True:
			self.vel_y = -16
			self.onground = False			
			
			#print('jumping')
		#átírtam az ugrást, hogy a collisiont érzékelje és csak akkor ugorhasson, ha a talajjal ütközik		
		if key[pygame.K_LEFT]:
			dx -= 5
			self.direction = -1
			self.counter += 1

		if key[pygame.K_RIGHT]:
			dx += 5
			self.counter += 1
			self.direction = 1

		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
			self.counter = 0
			self.index = 0
			if self.direction == 1:
				self.image = self.idle_right
			if self.direction == -1:
				self.image = self.idle_left
				
		if key[pygame.K_LEFT] == True and key[pygame.K_RIGHT] == True:
			self.counter = 0
			self.index = 0
			if self.direction == 1:
				self.image = self.idle_right
			if self.direction == -1:
				self.image = self.idle_left				
        		
		#anim
		if self.counter > walk_cooldown: 
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images_right):
				self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]

		#add gravity
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

        
		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			dy = 0

		#draw player onto screen
		screen.blit(self.image, self.rect)	
		#pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)	

		#check for collision
		# a collision egy az egyben jó volt, csak elöször véletlen a lvlup()-ba raktam XD
		for tile in world.tile_list:
			#check for collision in x direction
			if tile[2] == "entrance":
				continue
			else:
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
					#csekkolja h a pálya exit megvan-e találva - Márk
					if tile[2] == "exit":
						self.set_exit_reached(True)
		
				#check for collision in y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if below the ground i.e. jumping
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if above the ground i.e. falling
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						# ezt írtam hozzá, hogy ha a talajjal érintkezik akkor igaz legyen az onground ami engedi ugrani.
						self.onground = True
						#print('on ground')
										
		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy
		
		#coin felvétel - Márk
		for coin in coins:
			if coin.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				coins.remove(coin)
				coin_sound = pygame.mixer.Sound('../assets/coin_se.mp3')
				coin_sound.set_volume(0.1)
				coin_sound.play()
				self.__currency += 1
				print('MONEY: %d ' % self.__currency)



	def lvlup(self):		
		self.lvl += 1
		#print('szint:',self.lvl)
