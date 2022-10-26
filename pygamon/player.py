import pygame
import animation


class Player(animation.AnimateSprite):
    def __init__(self, x, y):
        super().__init__("player")

        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),  # 32 car chaque image fait 32 pixels
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])

        self.feet = pygame.Rect(0, 0, self.rect.width*0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 2

    def save_location(self):
        self.old_position.copy()

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey((0, 0, 0))

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.image, (0, 0), (x, y, 32, 32))
        return image
