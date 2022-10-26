from affichage import afficher_ligne, afficher_tableau
from saisie import saisie
from check import check

# creation de la liste pour avoir des valeurs independantes sinon il duplique la premiere ligne
list1 = [[" "] * 7 for _ in range(7)]

test = True
while(test):
    afficher_tableau(saisie(list1))
    # print(check(list1))
    if (check(list1)):
        print("Bravo ! Le joueur1 a gagne")
        test = False
    else:
        print("Debug2")
    print("")

#list1 = rangement_de_saisie(list1, saisie())
