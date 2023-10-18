from saisie import saisie

nbreColonnes = 7
nbreLines = 7

# affiche une ligne du tableau


def afficher_ligne():
    i = 0
    while (i < (nbreLines + 1)):
        print("|   ", end='')
        i += 1
        j = 0


# affichage du tableau vide
def afficher_tableau(tableau1):

    # on recupere la valeur retournee par la fonction de saisie dans saisie.py
    # testSaisieFunction = saisie()

    # affichage des numeros de colonnes
    j = 0
    # le 1 est à 2 espaces du bord alors que chaque chiffre est separe par 4 espaces, donc on affiche 1
    print("  " + str(j+1), end='')
    while (j < (nbreColonnes - 1)):
        # ici on affiche le reste des chiffres
        print("   " + str(j+2), end='')
        j += 1
    j = 0
    print("")

    # affichage de la premiere ligne de separation -----------
    j = 0
    while (j < 29):
        print("-", end='')
        j += 1
    j = 0
    print("")  # pour sauter une ligne apres l'affichage du numero des lignes

    # affichage des tableaux
    j = 0

    # On test la valeur recuperer au debut de la fonction afficher_tableau(tableau1)
    if (tableau1 == ""):
        while (j < nbreLines):
            print(j+1, end='')
            afficher_ligne()
            print("")
            j += 1
        j = 1

        # affichage de la derniere ligne de separation -----------
        print(" ", end='')
        while (j < 30):
            print("-", end='')
            j += 1
        j = 0
    else:
        i = 0
        j = 0
        while (i < 7):
            while (j < 7):
                print('|', tableau1[i][j], end=' ')
                j += 1
            print("|")
            j = 0
            i += 1

            # affichage du tableau avec au moins un coup joue

        j = 0
        while (j < 29):
            print("-", end='')
            j += 1
        print("")
