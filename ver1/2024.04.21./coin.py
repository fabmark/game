import pygame

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
class Coin():
    counter = 0
    def __init__(self, x, y):
        self.img_array = []
        self.index = 0
        for i in range(6):
            temp = pygame.image.load('img/'+str(i)+'.png')
            temp = pygame.transform.scale(temp, (20, 20))
            self.img_array.append(temp)

        self.image = self.img_array[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def animate(self):
        spin_cd = 5
        if Coin.counter > spin_cd:
            Coin.counter = 0
            if self.index >= len(self.img_array):
                self.index = 0
                Coin.counter += 1
            else:
                self.image = self.img_array[self.index]
                self.index += 1
                Coin.counter += 1
        screen.blit(self.image, self.rect)
        # pygame.time.delay(75)


