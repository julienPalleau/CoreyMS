from math import pi
import random
# Functions are first-class citizens in Python.

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.


def myfunc(a, b):
    return a + b


funcs = [myfunc]
print(funcs[0])
print(funcs[0](2, 3))
print(myfunc(2, 3))

list1 = range(3)
list2 = range(5)
print(list(list2))

prenom = 0
if (isinstance(prenom, str)):
    print("C'est une chaine de caractere")
else:
    print("Ce n'est pas une chaine de caractere")


phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
print(nouvelle_phrase)

chaine = "Tom, Matteo, Amedeo, Julien, Chloe, Lucie, Eliott".split(", ")
chaine.sort()
chaine = ", ".join(chaine)
print(chaine)

rayon = 10.0
volume = (4*pi)/3 * rayon**3
print(volume)
