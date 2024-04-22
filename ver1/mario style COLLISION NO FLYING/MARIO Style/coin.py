import pygame

screen_width = 990
screen_height = 990

screen = pygame.display.set_mode((screen_width, screen_height))
class Coin():
    def __init__(self, x, y):
        self.img_array = []
        self.index = 0
        for i in range(6):
            temp = pygame.image.load('MARIO Style/img/'+str(i)+'.png')
            temp = pygame.transform.scale(temp, (30, 30))
            self.img_array.append(temp)

        self.image = self.img_array[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # Individual counter for each coin

    def animate(self):
        spin_cd = 5
        if self.counter > spin_cd:
            self.counter = 0
            if self.index >= len(self.img_array) - 1:
                self.index = 0
            else:
                self.index += 1
            self.image = self.img_array[self.index]
        screen.blit(self.image, self.rect)
