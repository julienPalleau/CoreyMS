####################
# Annee Bissextile #
####################


reponse = "o"

while reponse.lower() == "o":
    try:
        annee = int(input(
            "Entrer une annee et le programme vous dira si elle est bisextille : "))
        assert annee > 0
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
    except AssertionError:
        print("L'annee saisie est inferieur ou egale a 0.")
    else:
        if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
            print("L'annee saisie est bissextile")
        else:
            print("L'anne saisie n'est pas bissextile")

        reponse = (input("voules vous rejouer O/N : "))

print("Merci d'avoir joue, au revoir et bonne journee!")
