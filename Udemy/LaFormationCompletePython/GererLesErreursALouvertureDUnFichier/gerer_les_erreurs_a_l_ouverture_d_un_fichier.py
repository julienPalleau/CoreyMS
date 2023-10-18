import os

file = input("Entrez un fichier à ouvrir:")


if not os.path.exists(file):
    print("Impossible d'ouvrir le fichier.")
else:
    try:
        with open(file, "r") as f:
            line = f.read()
    except UnicodeDecodeError:
        print("Impossible d'ouvrir le fichier.")
    finally:
        print("fermeture du fichier!")

    if (line):
        print(line)

#correction:
fichier = input("Entrez un fichier à ouvrir : ")

try:
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print("Le fichier est introuvable.")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier.")
else:
    f.close()

