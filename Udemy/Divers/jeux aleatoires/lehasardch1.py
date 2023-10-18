# La fonction randint(a,b) retourne un nombre entier entre a et b (bornes comprises).
# On peut ainsi facilement simuler le jet de de:
from random import randint, choice

print("50 jets de 3 des a 6 faces:")
for x in range(50):
    print(randint(1, 6)+randint(1, 6)+randint(1, 6), end=" ")

print("\n")

print("200 jets de 2 des a 8 faces:")
for x in range(200):
    print(randint(1, 8)+randint(1, 8), end=" ")

print("\n")
# En python, on peut creer et utiliser des listes (de lettres, de mots, de chiffres, ...).
# Il suffit de mettre les elements entre crochets:
# liste = ['a','b','c','d','e','f','g','h']
# print(choice(liste))
# produit comme resultat : b

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(choice(liste))

liste = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
for x in range(100):
    print(choice(liste), end=" ")
