list_film = [
    {
        'name': 'The Matrix',
        'director': 'Wachowskis',
        'year': '1994'
    },
    {
        'name': 'Star Wars',
        'director': 'Lucas',
        'year': '1977'
    }
]
print("Menu :")
answer = int(input("Voulez vous saisir un nouveau film ? - taper (1)\n"
                   "Voulez vous visualiser tous les films ? - taper (2)\n"
                   "Voulez vous trouvez un film par l'un de ses attributs ? - taper (3)"))

Entre_un_film = True
if answer == 1:
    while Entre_un_film:
        titre = input("Entrez un titre :")
        realisateur = input("Entrer le nom du realisateur :")
        annee = input("Entrer l'annee :")

        fiche_film3 = {'name': titre, 'director': realisateur, 'year': annee}
        list_film.append(fiche_film3)

        result = input("Voulez vous saisir un autre film? o/n")
        if result == 'n':
            Entre_un_film = False
elif answer == 2:
    for i in range(len(list_film)):
        print(list_film[i]['name'])
elif answer == 3:
    recherche = input("Saisissez un attribut (nom du film, realisateur our annee de realisation)")
    titre = realisateur = annee_de_realisation = ""
    for i in range(len(list_film)):
        if list_film[i]['name'] == recherche:
            titre = list_film[i]['name']
        if list_film[i]['director'] == recherche:
            realisateur = list_film[i]['director']
        if list_film[i]['year'] == recherche:
            annee_de_realisation = list_film[i]['year']
        if titre or realisateur or annee_de_realisation:
            print({titre}, {realisateur}, {annee_de_realisation})
            print(f"Titre du film : {list_film[i]['name']}, realisateur : {list_film[i]['director']} "
                  f"et annee de realisation : {list_film[i]['year']}")
            break
        else:
            print("impossible de trouver de film(s) avec ces parametres")
