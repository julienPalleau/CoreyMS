# Avec JSON
# import json
#
# fichier = "settings.json"
#
# # lecture d'un fichier json
# with open(fichier, "r") as f:
#     settings = json.load(f)
#
# print(settings["fontSize"])
#
#
# # ecriture d'un fichier json
# settings["fontSize"] = 15
#
# with open(fichier, "w") as f:
#     json.dump(settings, f, indent=4)

# Avec SQL
import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
    salaire int
)
""")

# ajout de donnees dans la db
d = {"prenom": "Paul", "nom": "Dupond", "salaire": 20000, }
c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

# Recuperation de donnees dans la db
c.execute("SELECT * FROM employees")
donees = c.fetchall()
""" comme pour les fichiers texte le curseur se trouve à la fin de la db
# il faut donc remettre le curseur au debut pour faire un nouveau fectchall. Pour mettre le curseur
# au debut on rejoue la requete: c.execute("SELECT * FROM employees")"""
print(donees)
# print("Recuperation des employes un par un")
# premier = c.fetchone()
# print(premier)
# deuxieme = c.fetchone()
# print(deuxieme)
# troisieme = c.fetchone()
# print(troisieme)
# quatrieme = c.fetchone()
# print(quatrieme)

# Mettre à jour des donnees
d = {"prenom": "Paul", "nom": "Dupond", "salaire": 10000}
c.execute("""UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom""", d)

# Recuperation de donnees dans la db
c.execute("SELECT * FROM employees")
donees = c.fetchall()
""" comme pour les fichiers texte le curseur se trouve à la fin de la db
# il faut donc remettre le curseur au debut pour faire un nouveau fectchall. Pour mettre le curseur
# au debut on rejoue la requete: c.execute("SELECT * FROM employees")"""
print(donees)

donees = c.fetchall()
conn.commit()
conn.close()

