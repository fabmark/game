import pygame

class Coin():
    def __init__(self, x, y):
        
        self.img_array = []
        self.index = 0
        for i in range(6):
            temp = pygame.image.load('assets/'+str(i)+'.png')
            temp = pygame.transform.scale(temp, (40,40))
            self.img_array.append(temp)

        self.image = self.img_array[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def animate(self):
        
        
        if self.index >= len(self.img_array):
            self.index = 0
        else:
            self.image = self.img_array[self.index]
            self.index += 1
        screen.blit(self.image, self.rect)
        pygame.time.delay(75)
