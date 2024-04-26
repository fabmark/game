import pygame

class Button():
        def __init__(self, x, y, image ,screen):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.screen = screen
            self.clicked = False

        def draw(self):
            action = False
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                 self.clicked = False
                      
            self.screen.blit(self.image, self.rect)
            return action
        

class Menu():
    def __init__(self,screen):
        self.play_btn = Button(990 // 2 - 100, 990 // 2 + 50, pygame.transform.scale(pygame.image.load('../assets/play_btn.png'),(150,90)), screen)
        self.exit_btn = Button(990 // 2 - 100, 990 // 2 + 250, pygame.transform.scale(pygame.image.load('../assets/exit_btn.png'),(150,90)), screen)
        self.load_btn = Button(990 // 2 - 100, 990 // 2 + 150, pygame.transform.scale(pygame.image.load('../assets/load_btn.png'),(150,90)), screen)
        self.save_btn = None
        self.__visible = True

    def get_visible(self):
         return self.__visible
    
    def set_visible(self, value):
         self.__visible = value

    # gombok visszaadása - Márk
    def get_play_btn(self):
         return self.play_btn

    def get_exit_btn(self):
         return self.exit_btn
    
    def get_load_btn(self):
         return self.load_btn