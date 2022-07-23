# Exercices & corrections: https://drive.google.com/drive/folders/1l4XE7U4R2HkNku6AVRYiFG4cRZ0y4x8N

# # Exercice 1
# interval_min = 1
# interval_max = 1
#
# while (interval_min > 0 and interval_max > 0):
#     interval_min = int(input("Saisissez une borne inferieur : "))
#     if interval_min < 0:
#         break
#     interval_max = int(input("Saisissez une borne superieur : "))
#     if interval_max < 0:
#         break
#
#     if (interval_max < interval_min):
#         print("la borne maximum doit etre superieur à la borne minimum !")
#         continue
#
#     nombre = int(input("Entrer un nombre : "))
#     if nombre in range(interval_min, interval_max):
#         print("Vous etes dans l'interval")
#     else:
#         print("Vous n'etes pas dans l'interval")
# else:
#     exit


# # Exercice 2
# number1 = int(input("Entrez un premier entier positif ou negatif : "))
# number2 = int(input("Entrez un second entier positif ou negatif : "))
#
# if ((number1 >= 0 and number2 < 0) or (number1 < 0 and number2 >= 0)):
#     print("Le produit des deux nombres saisies sera negatif")
# else:
#     print("Le produit des deux nombres saisies sera positif")

# # Exercice 3
# nb_heures = int(input("Entrer le nombre d'heure effectuee : "))
# nb_heures_sup = 0
#
# if nb_heures <= 40:
#     nb_heures_sup = 0
# elif nb_heures <= 44:
#     nb_heures_sup = (nb_heures - 44)*0.5
# elif nb_heures <= 49:
#     nb_heures_sup = 5*0.5 + (nb_heures - 49)*0.75
# else:
#     nb_heures_sup = 5*0.5 + 5*0.75 + (nb_heures - 50)
#
#
# print(f"nombre d'heure supplementaire effectuees {nb_heures - 39}, nombre d'heures supplementaires payee {nb_heures_sup}")

# # Exercice 4
# heure = input("Saisir une heure sous la forme heure:minute : ")
# h, m = heure.split(":")
# h = int(h)
# m = int(m)
#
# if m < 59:
#     m += 1
# else:
#     h += 1
#     if h > 23:
#         h = 0
#     m = "00"
#
# print(f"{h}:{m}")

# # Exercice 5
# mention = int(input("Veuillez saisir votre note : "))
# if ( mention < 12 ):
#     print("Vous avez la mention Passable")
# elif( mention < 14):
#     print("Vous avez la mention AB")
# elif(mention < 16):
#     print("Vous avez la mention B")
# elif(mention <= 20):
#     print("Vous avez la mention TB")
# else:
#     print("Vous n'avez pas de mention")

# # Exercice 6
# nombre = int(input("Saisissez un entier : "))
#
# for i in range(nombre,nombre+10):
#     print(i)

# # Exercice corriges python serie2
# # Exercice 1
# Nb =int(input("Saisir un nombre: "))
# while Nb < 1 or Nb > 3:
#     Nb = int(input(" saisir un nombre "))
# print("bravo")

# # Exercice 2
# Nb = int(input("Saisir un nombre entier compris entre 10 et 20 : "))
# while Nb <= 14 or Nb >= 16:
#     if Nb < 10:
#         print("Plus grand !")
#     elif Nb > 20:
#         print("Plus petit")
#
#     Nb =int(input("Saisir un nombre entier compris entre 10 et 20 : "))
# print("bravo")

# # Exercice 3
# nombre = 0
# compteur = 0
# sum = 0
# ma_liste = []
# while (nombre != -1):
#     nombre = int(input("Veuillez saisir un entier positif et taper -1 pour terminer : "))
#     if nombre != -1:
#         ma_liste.append(nombre)
#
# ma_liste.sort()
# print(f"Voici la liste des nombres saisies triee par ordre croissant : {ma_liste}")
# for nombre in ma_liste:
#     sum += nombre
#     compteur += 1
# print(f"La somme des nombres saisies est {sum}")
# print(f"La monyenne des nombre saisies est {sum/compteur}")

# Exercice 4
S1 = 1
N = int(input("Saisir un entier: "))
signe = -1
for i in range(1, N+1):
    S1 += N**i

print(S1)

