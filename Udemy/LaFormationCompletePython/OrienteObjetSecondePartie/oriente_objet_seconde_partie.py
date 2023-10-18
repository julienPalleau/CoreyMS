# class Voiture:
#     voiture_crees = 0
#     def __init__(self, marque, vitesse, prix):
#         self.marque = marque
#         self.vitesse = vitesse
#         self.prix = prix
#
#     def __str__(self):
#         return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}."
#
#     @classmethod
#     def lamborghini(cls):
#         return cls(marque="Lamborghini", vitesse=250, prix=200000)
#
#     @classmethod
#     def porsche(cls):
#         return cls(marque="Porsche", vitesse=200, prix=180000)
#
#     @staticmethod
#     def afficher_nombre_voitures():
#         print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")
#
#
# lambo = Voiture.lamborghini()
# porshe = Voiture.porsche()
# print(porshe)


projets = ["pr_GammeOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projet(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        Utilisateur.__init__(self, nom, prenom)

paul = Junior("Paul", "Durand")
print(paul)
paul.afficher_projet()