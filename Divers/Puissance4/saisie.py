def saisie(list1):
    #########################################################
    # Check si la valeur de la colonne fournie est correcte #
    #########################################################
    message = "You didn't enter a valid Column ! it must be an integer 1 < x < 7"
    test = False
    # Check is c'est un entier
    while (test == False):
        try:
            numeroColonne = int(input(
                "Veuillez saisir le numero de colonne dans laquelle vous voulez jouer : "))
            test = True
        except (ValueError):
            print(message)

    # check si l'entier est dans le range 1 - 7
    test = False
    while (test == False):
        if (0 <= int(numeroColonne) - 1 < 7):
            test = True
        else:
            print(message)
            try:
                numeroColonne = int(input(
                    "Veuillez saisir le numero de colonne dans laquelle vous voulez jouer : "))
            except (ValueError):
                print(message)

    i = 7
    nb_coup = 1  # pour s'assurer qu'une seule case est jouee
    while (i >= 1):
        if list1[i - 1][int(numeroColonne - 1)] != "X" and list1[i - 1][int(numeroColonne - 1)] != "O" and nb_coup > 0:
            list1[i - 1][int(numeroColonne - 1)] = 'X'
            i = -1
            nb_coup -= 1
        else:
            pass
        i -= 1

    return list1
