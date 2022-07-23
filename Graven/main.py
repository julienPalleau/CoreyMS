from game import Game
import math
import pygame
import os

pygame.init()


# generer les path d'acces aux images
# method 1 (la plus propre d'un point de vue programation)
# current_path = os.path.dirname(__file__)
# resource_path = os.path.join(current_path, 'assets')
# image_path = os.path.join(resource_path, 'bg.jpg')
# methode 2 avec un path en dur
image_path = "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Graven\\assets\\bg.jpg"

# generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan
background = pygame.image.load(image_path)

# importer charger la banniere
banner = pygame.image.load(
    "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Graven\\assets\\banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger le bouton pour lancer la partie
play_button = pygame.image.load(
    "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Graven\\assets\\button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    # verifier si notre jeu a commence ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si notre jueu n'a pas commence
    else:
        # ajoute l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchee pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lance
                game.start()
