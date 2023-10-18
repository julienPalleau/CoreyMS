import os

cur_dir = os.path.realpath(os.path.dirname(__file__)) # os.path.realpath elimine les liens symbolic et utilise le full path
fichier = os.path.join(cur_dir, "variable.txt")

with open(fichier, "r") as f:
    variable = f.read()

if variable:
    print("La variable est un boolean True")