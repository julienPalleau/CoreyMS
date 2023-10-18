import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()


class Liste(list):  # Liste herite de list
    def __init__(self, nom):
        self.nom = nom

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines de caracteres")

        if element in self:
            LOGGER.error(f"{element} est deja dans la liste.")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        try:
            with open(chemin, "w") as f:
                json.dump(self, f, indent=4)
        except FileNotFoundError:
            print("Le fichier est introuvable.")
        except UnicodeError:
            print("Impossible d'ouvrir le fichier.")

        return True


if __name__ == "__main__":
    liste = Liste("courses")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.sauvegarder()