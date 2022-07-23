# bissextile
annee = int(input("Saisissez une annee: "))

if (annee % 4 == 0):
    if (annee % 100 == 0):
        if (annee % 400 == 0):
            print("L'anne saisie est bissextile !")
        else:
            print("L'annee saisie n'est pas bissextile")
    else:
        print("L'annee est bissextile !")
else:
    print("L'annee saisie n'est pas bissextile")
