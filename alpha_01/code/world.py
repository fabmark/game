import pygame
from coin import Coin


screen_width = 990
screen_height = 990

screen = pygame.display.set_mode((screen_width, screen_height))



class World():
    def __init__(self, data):
        self.tile_list = []
        tile_size = 30

        #load images
        ground_img = pygame.image.load('../assets/ground.png')
        wall_img = pygame.image.load('../assets/wall.png')
        black_img = pygame.image.load('../assets/black.png')
        spikes_img = pygame.image.load('../assets/spikes.png')
        trap_img = pygame.image.load('../assets/trap.png')
        sword_img = pygame.image.load('../assets/sword.png')
        bow_img = pygame.image.load('../assets/bow.png')
        staff_img = pygame.image.load('../assets/staff.png')
        blood_img = pygame.image.load('../assets/blood.png')
        gate_img = pygame.image.load('../assets/exit_btn.png')
        mobwall_img = pygame.image.load('../assets/mobwall.png')

        row_count = 0
        # raktam "type-okat" ide, csak azért h a pálya végét könnyebb legyen megkülönböztetni - Márk
        for row in data:
            col_count = 0
            for tile in row:
                if tile == '1':
                    img = pygame.transform.scale(ground_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "ground")
                    self.tile_list.append(tile)
                if tile == '2':
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "wall")
                    self.tile_list.append(tile)
                if tile == '3':
                    img = pygame.transform.scale(black_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "entrance")
                    self.tile_list.append(tile)
                if tile == '4':
                    img = pygame.transform.scale(blood_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "blood")
                    self.tile_list.append(tile)
                if tile == '5':
                    img = pygame.transform.scale(trap_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "trap")
                    self.tile_list.append(tile)
                if tile == '6':
                    img = pygame.transform.scale(spikes_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "spikes")
                    self.tile_list.append(tile)
                if tile == 'K':
                    img = pygame.transform.scale(sword_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "sword")
                    self.tile_list.append(tile)
                if tile == 'I':
                    img = pygame.transform.scale(bow_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "bow")
                    self.tile_list.append(tile)
                if tile == 'V':
                    img = pygame.transform.scale(staff_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "staff")
                    self.tile_list.append(tile)
                if tile == 'G':
                    img = pygame.transform.scale(gate_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "gate")
                    self.tile_list.append(tile)
                if tile == '9':
                    img = pygame.transform.scale(black_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "exit")
                    self.tile_list.append(tile)
                if tile == 'M':
                    img = pygame.transform.scale(mobwall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "M")
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

        # def animate(self):
        #for tile in self. tile_list:
            #if isinstance(tile, Coin):
                #tile.animate()
