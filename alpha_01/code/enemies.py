import pygame

class Goblin():
    def __init__(self, x, y):
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

    def update(self, screen_height, screen, world):
        screen.blit(self.image, self.rect)