import pygame
from pygame.locals import *


class Player():
	def __init__(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range (1, 9):			
			img_right = pygame.image.load(f'img/walk{num}.png')
			img_right = pygame.transform.scale(img_right, (30, 50))
			img_left = pygame.transform.flip(img_right, True, False)			
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.idle_right = pygame.image.load('img/IDLE.png')
		self.idle_right = pygame.transform.scale(self.idle_right, (30,50))
		self.idle_left = pygame.transform.flip(self.idle_right, True, False)
		self.image = self.idle_right
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.lvl = 1
		print('szint:',self.lvl)

	def update(self,screen_height,screen):
		dx = 0
		dy = 0
		walk_cooldown = 5

		#get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
			self.jumped = True
		if key[pygame.K_SPACE] == False:
			self.jumped = False
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

		#check for collision

		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

        
		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			dy = 0

		#draw player onto screen
		screen.blit(self.image, self.rect)
			
		
		
		

	def lvlup(self):		
		self.lvl += 1
		print('szint:',self.lvl)









