import pygame


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inventory")

bg_img = pygame.image.load("../assets/inventory.png")
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Item:
    def __init__(self, name, image):
        self.name = name
        self.image = image

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


    def draw(self):
        item_height = 40
        item_width = 40
        start_x = 140
        start_y = 355
        slot_size = 25
        for n, item in enumerate(self.items):
                image = pygame.image.load(item.image)
                image = pygame.transform.scale(image, (item_width, item_height))
                screen.blit(image, (start_x + (item_width + slot_size) * n, start_y))

items = [Item("Sword", '../assets/sword.png'),
         Item("Bow", '../assets/bow.png'),
         Item("Staff", '../assets/staff.png'),

         ]

inventory = Inventory()

running = True

while running:
    screen.blit(bg_img, (0, 0))
    inventory.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                for item in inventory.items:
                    if item.name == "Sword":
                        inventory.items.remove(item)
                        break
            elif event.key == pygame.K_RETURN:
                for item in items:
                    if item.name == "Sword":
                        inventory.add_item(item)

    pygame.display.update()


pygame.quit()
