import pygame
from player import Player

class Goblin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0, 13):
            img_right = pygame.image.load(f'../assets/goblin{num}.png')
            img_right = pygame.transform.scale(img_right, (45, 75))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.idle_right = pygame.image.load(f'../assets/goblinidle.png')
        self.idle_right = pygame.transform.scale(self.idle_right, (45, 75))
        self.idle_left = pygame.transform.flip(self.idle_right, True, False)
        self.image = self.idle_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.direction = 0
        self.hp = 10
        self.dmgcd = 0

    def update(self, screen_height, screen, world, firebolts, arrows, player):
        dx = 0
        dy = 0
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
    
        screen.blit(self.image, self.rect)
        if self.dmgcd > 0:
            self.dmgcd -=1
    
        for tile in world.tile_list:
            if tile[2] == "blood" or tile[2] == "wall" or tile[2] == "ground" or tile[2] == 'gate':
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

        for firebolt in firebolts:
            if firebolt.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                firebolt.kill()
                self.hp -= 5  
                break

        for arrow in arrows:
            if arrow.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                arrow.kill()
                self.hp -= 3
                break
        if player.attack_range.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            if self.dmgcd == 0:
                self.hp -=5
                self.dmgcd = 10
        if self.hp <= 0:
            self.kill()




        self.rect.x += dx
        self.rect.y += dy