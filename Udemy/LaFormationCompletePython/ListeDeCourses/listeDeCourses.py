from os import system, name
import os
import json

choix = 1
affichage = """Choisissez une option:
                \t1: Ajouter un élément
                \t2: Enlever un élément
                \t3: Afficher la liste
                \t4: Vider la liste
                \t5: Sauvegarder
                \t6: Quitter
                """

dossier_courant = os.path.dirname(__file__)
fichier = os.path.join(dossier_courant, "liste.json")


def clear():
    if name == 'nt':
        _ = system('cls')


if os.path.exists(fichier):
    with open(fichier, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

while True:
    print("\n" + affichage)
    choix = input("Quel est votre choix : ")
    while not choix.isdigit():
        print("Veuillez entrer un choix valide (1..5)")
        choix = input("Quel est votre choix : ")

    choix = int(choix)
    if choix == 1:
        element = input("Quel produit desirez vous ajouter à votre liste ?")
        if element == "":
            print("vous n'avez pas saisi de produit, rien ne sera ajoute à votre liste")
        else:
            liste_de_courses.append(element)
            print(f"Le produit {element} a bien etait ajoute à votre liste.")
    elif choix == 2:
        element = input("Quel produits désirez vous supprimer de de votre liste (entre les numeros separes par un "
                        "espace ?")
        if element in liste_de_courses:
            liste_de_courses.remove(element)
            print(f"Le produit {element} a bien etait supprime de votre liste.")
        else:
            print("L'element ne peut etre supprime car il n'est pas present dans votre liste !")
    elif choix == 3:
        print("Dans votre liste vous avez: ")
        for item in liste_de_courses:
            print(item)
    elif choix == 4:
        liste_de_courses = []
        print(f"Votre liste de course vient d'etre vidée {liste_de_courses}")
    elif choix == 5:
        with open(fichier, "w") as f:
            json.dump(liste_de_courses, f, indent=4)

    elif choix == 6:
        print("Vous avez quitte l'application, au revoir.")
        break
    else:
        print("Veuillez entrer un choix valide (1..5)")

    print("pause")
    input()
