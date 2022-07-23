from random import randint

# Creation du jeu de cartes


def crea_jeu():
    jeu = []
    oranges = [0 for i in range(4)]
    vertes = [i for i in range(1, 11)]
    violettes = [i * 10 for i in vertes if i % 2 != 0]
    violettes = violettes * 2
    # print(oranges)
    # print(vertes)
    # print(violettes)
    for i in vertes:
        jeu.append([1, i])
    for i in violettes:
        jeu.append([0, i])
    for i in oranges:
        jeu.append([2, i])
    # print(jeu)
    return (jeu)

    # [[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [0, 10], [0, 30], [0, 50], [0, 70], [0, 90], [0, 10], [0, 30], [0, 50], [0, 70], [0, 90], [2, 0], [2, 0], [2, 0], [2, 0]]]


# Distribution aleatoire du jeu de cartes aux deux joueurs
def distribue(jeu):
    jeu1, jeu2 = [], []
    while len(jeu) != 0:
        a = randint(0, len(jeu) - 1)
        jeu1.append(jeu[a])
        del jeu[a]
        b = randint(0, len(jeu) - 1)
        jeu2.append(jeu[b])
        del jeu[b]
    return (jeu1, jeu2)


# Retourne la carte gagnante parmi les deux passees en parametres
def pli(carte1, carte2):
    gagnant = []
    couleur_carte1 = carte1[0]
    num_carte1 = carte1[1]
    couleur_carte2 = carte2[0]
    num_carte2 = carte2[1]
    print(carte1)

    if couleur_carte1 == couleur_carte2:
        if num_carte1 == num_carte2:
            return None
        elif num_carte1 > num_carte2:
            # gagnant.append(carte1)
            gagnant = carte1
        else:
            # gagnant.append(carte2)
            gagnant = carte2
    elif couleur_carte1 > couleur_carte2:
        # gagnant.append(carte1)
        gagnant = carte1
    else:
        # gagnant.append(carte2)
        gagnant = carte2
    return gagnant


# Fonction de jeu d'une carte par le joueur 1
def jouer_carte1_LVL0(main):
    # Niveau 0 : on joue toujours la première carte de la main (restante)
    return (main[0])


# # Niveau 1 : Jouer les 4 cartes les plus faibles, puis jouer les plus fortes afin de battre le robot.

def jouer_carte1_LVL1(main):
    mainA = sorted(main)
    if (len(main) > 8):
        return (mainA[0])
    else:
        return (mainA[len(main) - 1])


# # Jouer_une_carte_NIV_1(crea_jeu())

# # Niveau 2 : Jouer les 4 cartes avec les plus faibles valeurs puis une carte orange pour avoir un décallage sur les vert du robot puis jouer les cartes les plus fortes

def jouer_carte1_LVL2(main):
    mainA = sorted(main)
    if (len(main) > 8):
        i = 0
        while mainA[i][0] == 0:
            i = i + 1
        return (mainA[i])
    elif len(main) == 8:
        return (mainA[len(mainA) - 1])
    elif len(main) > 3:
        return (mainA[len(mainA) - 4])
    else:
        return (mainA[0])


# # Fonction de jeu d'une carte par le joueur 2 (le robot dans un premier temps)
def jouer_carte2(main):
    liste1 = [i[1] for i in main if i[0] == 1]
    liste2 = [i[1] for i in main if i[0] == 0]
    for i in main:
        if i[0] == 2:
            return (i)
    for i in main:
        if i[0] == 1 and i[1] == max(liste1):
            return (i)
    for i in main:
        if i[1] == min(liste2):
            return (i)
    return (main[0])


# La partie, renvoie le gagnant.
def partie():
    joueur1, joueur2 = distribue(crea_jeu())
    score1, score2 = 0, 0
    for i in range(12):
        carte_j1 = jouer_carte1_LVL1(joueur1)
        #print("carte1", carte_j1)
        joueur1.remove(carte_j1)
        carte_j2 = jouer_carte2(joueur2)
        #print("carte2", carte_j2)
        joueur2.remove(carte_j2)
        gagnant = pli(carte_j1, carte_j2)
        #print("gagnant", gagnant)
        if gagnant == carte_j1:
            score1 = score1 + carte_j1[1] + carte_j2[1]
        elif gagnant == carte_j2:
            score2 = score2 + carte_j1[1] + carte_j2[1]

    if score1 > score2:
        return (1)
    elif score1 < score2:
        return (2)
    else:
        return (0)


# # Programme principal, on joue 1000 parties


g1, g2 = 0, 0
for x in range(1000):
    r = partie()
    if r == 1:
        g1 += 1
    if r == 2:
        g2 += 1
print(g1, ' — ', g2)
