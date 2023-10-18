import glob
import os
import json

# dossier = "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\LaFormationCompletePython\\" \
#           "ChercherDesInformationsDansUnDossier\\**"
# files = glob.glob(dossier, recursive=True)
#
# for file in files:
#     if os.path.isfile(file):
#         path, extension = os.path.splitext(file)
#         if extension == ".txt":
#             with open(file, 'r') as f:
#                 line = f.read()
#                 valeurs = line.split(':')
#                 for valeur in valeurs:
#                     if '123456789' in valeur:
#                         print(f"Trouve la valeur 123456789 dans le fichier {file}!!!")
#
#         elif extension == ".json":
#             with open(file) as f:
#                 line = json.load(f)
#                 for key, value in line.items():
#                     for key2, value2 in value.items():
#                         if 92817 == value2:
#                             print(f"Trouve la valeur 92817 dans le fichier {file}!!!")

# Correction
dossier = "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\LaFormationCompletePython\\" \
          "ChercherDesInformationsDansUnDossier\\**"
files = glob.glob(dossier, recursive=True)

numero_de_compte = None
numero_securite_sociale = None

for f in files:
    if f.endswith(".json"):
        print(f)
        with open(f, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                numero_de_compte = contenu["Credit Mutuel"]["Numero de compte"]

    elif f.endswith(".txt"):
        with open(f, "r", encoding='UTF-8') as f:
            contenu = f.read()
            if "Numéro de sécurité sociale" in contenu:
                numero_securite_sociale = contenu.split(":")[-1]

print(numero_de_compte)
print(numero_securite_sociale)

