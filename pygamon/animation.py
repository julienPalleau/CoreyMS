import pygame


# definir une classe qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'{sprite_name}.png')


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images du sprite
    images = []

