class Voiture:

    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence")

    def faire_le_plein(self):
        self.essence = 100
        print(f"Vous pouvez repartir !")

    def roule(self, distance):
        self.essence = self.essence - (distance * 5) / 100

        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        elif self.essence < 10:
            print(f"Vous n'avez bientot plus d'essence !")

        self.afficher_reservoir()

voiture_01 = Voiture()
#voiture_01.essence
#voiture_01.afficher_reservoir()
#voiture_01.roule(100)

# Correction

# class Voiture:
#     def __init__(self):
#         self.essence = 100
#
#     def afficher_reservoir(self):
#         print(f"La voiture contient {self.essence}L d'essence.")
#
#     def roule(self, km):
#         if self.essence <= 0:
#             print("Vous n'avez plus d'essence, faites le plein !")
#             return
#
#         self.essence -= (km * 5) / 100
#
#         if self.essence < 10:
#             print("Vous n'avez bientôt plus d'essence !")
#
#         self.afficher_reservoir()
#
#     def faire_le_plein(self):
#         self.essence = 100
#         print("Vous pouvez repartir !")