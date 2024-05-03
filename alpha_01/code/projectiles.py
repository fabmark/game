import pygame



class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/arrow.png')
        self.image = pygame.transform.scale(self.image, (25, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.direction = direction
        self.speed = 10

    def update(self, world):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 990:
            self.kill()
        for tile in world.tile_list:
            if tile[2] in ["wall", "ground", "gate", "trap", "spikes", "entrance" ]:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    break


class Firebolt(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/firebolt.png')
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.direction = direction
        self.speed = 15

    def update(self, world):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 990:
            self.kill()
        for tile in world.tile_list:
            if tile[2] in ["wall", "ground", "gate", "trap", "spikes", "entrance" ]:
                if tile[1].colliderect(self.rect):
                    self.kill()
                    break