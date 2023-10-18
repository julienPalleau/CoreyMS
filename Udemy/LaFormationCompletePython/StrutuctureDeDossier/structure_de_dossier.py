# import os
#
# d = {"Films": ["Le seigneur des anneaux", "Harry Potter", "Moon", "Forest Gump"],
#      "Employes": ["Paul", "Pierre", "Marie"],
#      "Exercices": ["les_variables", "les_fichiers", "les boucles"]}
#
#
# for key, value in d.items():
#     os.chdir(os.getcwd())
#     dir_level1 = os.path.join(os.getcwd(), key)
#     os.makedirs(key, exist_ok=True)
#
#     os.chdir(dir_level1)
#     titres = d[key]
#     for titre in titres:
#         os.makedirs(titre, exist_ok=True)


# Correction
import os

chemin = r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Udemy\LaFormationCompletePython\StrutuctureDeDossier"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key, value in d.items():
    for dossier in value:
        chemin_dossier = os.path.join(chemin, key, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
