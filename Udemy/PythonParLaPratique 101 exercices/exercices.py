###################
# Niveau Debutant #
###################
import os.path

print("Exercice 1")
# https://www.udemy.com/course/python-exercices/learn/quiz/5365478#overview
"""
001 - Déclarer des variables
+ Notions abordées: les variables
On commence simple avec ce premier exercice, qui consiste à declarer differents types de variables.

La variable 'prenom' qui doit contenir la chaine de caractere Pierre.
La variable 'age' qui doit contenir 20.
La variable 'majeur' qui doit contenir un boolean vrai.
La variable 'compte_en_banque' qui doit contenir le nombre à virgule 20135,384.
La variable 'amis' qui doit contenir une liste contenant trois chaines de caracteres: Marie, Julien, Adrien.
La variable 'parents' qui doit contenir un tuple contenant deux chaines de caracteres: Marc et Caroline
"""
##
# prenom = "Pierre"
# age = 20
# majeur = True
# compte_en_banque = 20135.384
# amis = ["Marie", "Julien", "Adrien"]
# parents = ("Marc", "Caroline")
# print(prenom)
# print(age)
# print(majeur)
# print(compte_en_banque)
# print(amis)
# print(parents)
"""
        EXPLICATION

   Dans cet exercice, il suffisait de déclarer les différents types de variable demandés.

       POINTS IMPORTANTS À RETENIR

   - Une chaîne de caractère doit être entourée de deux guillemets. Les guillemets peuvent être simples (') ou doubles 
   ("). Vous ne pouvez pas commencer avec des guillemets simples et finir avec des guillemets doubles et vice-versa.

   - Un booléen commence par une majuscule et peut contenir deux valeurs, True ou False.

   Si vous essayez de créer un booléen en écrivant true ou false vous obtiendrez une erreur de syntaxe.

   - Pour définir un nombre décimal, on utilise le point (.) et non pas la virgule.

   La virgule sert à séparer les éléments les uns des autres.

   Si vous essayez de créer un nombre à virgule avec une virgule au lieu d'un point, vous vous retrouverez avec un tuple
    contenant les deux nombres de chaque côté de la virgule.

   Voyez plutôt :

       nombre = 123,456
       >>> (123, 456)
       nombre = 123.456
       >>> 123.456

   - Pour définir une liste, on utilise les crochets : [ ]
   - Pour définir un tuple, on utilise les parenthèses : ( )
   """

print("\nExercice 2")
"""
002 - Errer déclaration variable
+ Notion abordées: les variables
Une erreur s'est glissée dans la déclaration de la variable 'site_web', à vous de la trouver et de la corriger pour
que le script affiche le nom du site web.
"""

# site_web = 'Udemy"
# print(site_web)
##
# site_web = "Udemy"
# print(site_web)
"""
    SOLUTION

    site_web = "Udemy"
    print(site_web)

    EXPLICATION

Quand vous déclarez une variable de type chaîne de caractères, vous devez utiliser le même type de guillemet en 
ouverture et fermeture. Il existe deux types de guillemets, les simples et les doubles. Vous pouvez utiliser les deux 
sans problèmes tant que vous ne les mélangez pas.

    POINTS IMPORTANTS À RETENIR

    Pour définir une chaîne de caractère, il faut utiliser le même type de guillemet en ouverture et fermeture.
"""

print("\nExercice 3")
# Exercice 3
# Notions abordees: les variables
# Dans cet exercice, nous allons afficher un nombre à l'interieur d'une chaine de caractere.
# Pythom ne permet pas de concatener une chaine de caracteres avec un nombre, il va donc falloir convertir le nombre
# en chaine de caractere.
# nombre = 15
# print("Le nombre est " + str(nombre))
"""
    SOLUTION

    nombre = 15
    print("Le nombre est " + str(nombre))

    EXPLICATION

Là encore un exercice très simple pour ceux qui sont habitués à Python.

Dans Python, on ne peut pas concaténer des variables de différents types. Ainsi, si on essaie d'additionner une chaîne 
de caractères avec un nombre, on se retrouve avec une erreur :

    >>> nombre = 15
    >>> print("Le nombre est " + nombre)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not int

L'erreur ci-dessus nous indique que le type de la variable 'nombre', pour être concaténé avec la chaîne de caractère 
'Le nombre est ', doit être de type 'str' (chaîne de caractère) et non pas 'int' (nombre entier).

Pour remédier à ce problème, on convertit donc notre nombre 15, par la chaîne de caractère '15', grâce à la fonction str.

    POINTS IMPORTANTS À RETENIR

- Pour convertir un nombre en chaîne de caractère, on utilise la fonction str.

- Pour convertir une chaîne de caractère en nombre, on utilise la fonction int.
Attention : si vous essayez de convertir une chaîne de caractère qui ne contient pas un nombre en 'integer' avec la 
fonction int, vous aurez une erreur :

    >>> int("Udemy")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'Udemy'

Pour vérifier si une chaîne de caractère ne contient que des chiffres, vous pouvez utiliser la méthode isdigit :

    >>> "Udemy".isdigit()
    False
    >>> "2018".isdigit()
    True
    >>> 
"""

print("\nExercice 4")
# Exercice 4
# Notions abordees: les variables
# Pour reussir l'exercice, vous devez printer la valeur que contient la variable 'a'.
##
# a = 3
# b = 6
# a = b
# b = 7
# # trouver la valeur de a
# print(6)

"""
    SOLUTION

    a = 3
    b = 6
    a = b
    b = 7
     
    print(6)

    EXPLICATION

Ici, on déclare deux variables, a et b, qui contiennent des valeurs différentes.

On déclare de nouveau la variable a à la troisième ligne et on lui assigne la valeur de b (donc 6).

Ensuite on modifie la valeur de la variable b, mais cela ne modifie en rien la valeur de la variable a.
Les deux variables sont distinctes et on peut modifier les valeurs contenues dans l'une et dans l'autre sans affecter 
l'autre variable.
"""

print("\nExercice 5")
# # Exercice 5
# # Notions abordees: La fonction print.
# # Dans cette exercice, nous allons utiliser les nouvelles fonctionnalites de python 3, afin de printer les 3 variables
# a, b et c, separees par un symbole d'addition(+)
# a = 2
# b = 6
# c = 3
# print(a, b, c, sep=" + ")

"""
    SOLUTION

    a = 2
    b = 6
    c = 3
    print(a, b, c, sep=" + ")

    EXPLICATION

Depuis la version 3 de Python, la fonction print accepte un paramètre 'sep' qui permet de séparer les éléments que l'on 
print par une chaîne de caractère.

Ici, nous séparons donc les trois variables que nous affichons avec la fonction print, par la chaîne de caractère " + ",
 ce qui permet d'afficher le résultat suivant : 2 + 6 + 3 
"""

print("\nExercice 6")
# Exercice 6
# Notions abordees: les variables
# Le but de cet exercice est de trouver et reparer l'erreur presente dans le code.
# Vous devez modifier le code dans la console afin de ne plus avoir d'errers lors de l'execution du script.
# Vous ne devez pas toucher à la fonction print, juste a declaration des variables
# list = range(3)
# list2 = range(5)
# print(list(list2))

"""
    SOLUTION

    list1 = range(3)
    list2 = range(5)
    print(list(list2))

    EXPLICATION

Le problème qui survient dans le script de départ vient du fait que nous assignons 'range(3)' dans une variable qui est 
déjà utilisée par Python pour convertir un objet en liste (la fonction list).

Ainsi, quand nous essayons de convertir la liste 'list2', avec la fonction list, nous avons une erreur :

    >>> list = range(3)
    >>> list2 = range(5)
    >>> list(list2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'range' object is not callable

En écrasant le mot réservé 'list' par 'range(3)', nous écrasons la fonction list et quand nous voulons l'utiliser plus 
loin dans notre script, Python essaie de convertir notre liste 'list2' avec l'objet 'range' contenu à l'intérieur de la 
variable 'list' au lieu d'utiliser la fonction list.

    POINTS IMPORTANTS À RETENIR

- Il faut faire très attention à ne pas écraser des noms réservés par Python.

- Voici une liste non-exhaustive des noms réservés par Python :

    False               def                 if                  raise
    None                del                 import              return
    True                elif                in                  try
    and                 else                is                  while
    as                  except              lambda              with
    assert              finally             nonlocal            yield
    break               for                 not                 
    class               from                or                  
    continue            global              pass 

À cette liste vous pouvez ajouter toutes les fonctions de base de Python, comme la fonction str, la fonction int, la 
fonction dict, la fonction print, la fonction list etc...
"""

print("\nExercice 7")
# Exercice 7
# Notions abordées: Les variables
# Dans cette exercice, vous allez devoir verifier que la variable 'prenom' est bien une chaine de caracteres.
# La variable prenom est definie au debut du script par une chaine de caractere.
# Votre script doit donc printer une premiere fois la phrase "La varaible est une chaine de caracteres".
# La variable prenom est ensuite redefinie est assignee au nombre 0.
# Vous devez donc tester de nouveau votre condition mais cette fois-ci, votre script ne doit pas printer la phrase.
# prenom = "Pierre"
# INSERER VOTRE CONDITION ICI.
# Votre condition doit verifier si la variable est bien une chaine
# de caractere. Ici c'est le cas,
# votre condition doit donc etre vraie et printer la phrase "La variable
# est une chaine de caracteres".
# prenom = 0
# INSERER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas egale à une chaine de caractere.
# Votre condition doit donc etre fausse et la phrase ne doit pas s'afficher.
##
# prenom = "Pierre"

# if (isinstance(prenom, str)):
#     print("La variable est une chaîne de caractères")
# elif (isinstance(prenom, int)):
#     pass

# prenom = 0
# if (isinstance(prenom, str)):
#     print("La variable est une chaîne de caractères")
# elif (isinstance(prenom, int)):
#     pass
"""
    SOLUTION

    prenom = "Pierre"
     
    if type(prenom) == str:
        print("La variable est une chaîne de caractères")
     
    prenom = 0
     
    if isinstance(prenom, str):
        print("La variable est une chaîne de caractères")

    EXPLICATION

Pour vérifier si une variable est d'un certain type, on peut utiliser la fonction type ou la fonction isinstance.

On vérifie une première fois si la variable "prenom" est de type "str", c'est le cas, la phrase "La variable est une 
chaîne de caractères" s'affiche donc bien à l'écran.

On redéfinie ensuite la variable "prenom" pour lui assigner le nombre 0.

On vérifie ensuite une deuxième fois avec la fonction isinstance, que la variable "prenom" est bien une instance de la 
classe "str". Cette fois-ci, la variable "prenom" étant égale à un nombre entier (int), la phrase ne s'affiche pas.

Dans un exemple simple comme celui-ci, le résultat est similaire. Il est cependant préférable d'utiliser la fonction 
isinstance, car elle fonctionnera également si vous vérifier le type d'une variable qui hérite d'une classe qui est du 
type que vous cherchez.

    >>> default_dict = {}
     
    >>> type(default_dict)  # Notre dictionnaire est bien de type 'dict'
    <type 'dict'>
     
    >>> class CustomDict(dict):  # On créé une classe custom, qui hérite de la classe 'dict'
    ...     pass
     
    >>> custom_dict = CustomDict()
     
    >>> type(custom_dict)
    <class '__main__.CustomDict'>
     
    # Avec la fonction type(), notre dictionnaire custom n'est pas reconnu comme étant de type 'dict'
    >>> type(custom_dict) == dict
    False                     
     
    # La fonction isinstance en revanche comprend que notre dictionnaire custom hérite de la classe 'dict'
    >>> isinstance(custom_dict, dict)
    True                      

    POINTS IMPORTANTS À RETENIR

- Pour vérifier le type d'une variable, on peut utiliser la fonction type ou la fonction isinstance. On préfèrera la 
fonction isinstance qui gère l'héritage.
"""

# print("\nExercice 8")


# Exercice 8
# Notions abordées: Les chaines de caractere.
# Dans cet exercice, vous devez remplacer le mot 'Bonjour' dans la variable 'phrase' par le mot 'Bonsoir' à l'aide d'une
# fonction Python.
# Vous devez donc modifier la variable 'phrase'!
# phrase = "Bonjour tout le monde."
# nouvelle_phrase =
# print(nouvelle_phrase)
##
# phrase = "Bonjour tout le monde."
# nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
# print(nouvelle_phrase)
"""

    SOLUTION 

    phrase = "Bonjour tout le monde."
    nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
    print(nouvelle_phrase)

    EXPLICATION

Pour remplacer un mot par un autre en Python on utilise la fonction replace.

Le premier argument est le mot à chercher et le second contient ce par quoi on veut le remplacer.

La fonction replace va remplacer toutes les instances de la chaîne de caractère qu'elle trouve dans la phrase. Si vous 
avez 3 fois le mot "Bonjour", les trois occurrences du mot seront remplacées.

    POINTS IMPORTANTS À RETENIR

Pour remplacer un mot par un autre on utilise la fonction replace.
"""

print("\nExercice 9")
# Exercice 9
# Notions abordées: Les chaines de caracteres.
# Le but de cet exercice est de remettre en ordre alphabetique les prenoms presents dans la chaine de caractere.
# Vous devez donc printer à la fin de l'exercice, la chaine de caractere suivante:
# "Anne, Julien, Lucien, Marie, Pierre"
# chaine = "Pierre, Julien, Anne, Marie, Lucien"
##

"""
    SOLUTION

    chaine = "Pierre, Julien, Anne, Marie, Lucien"
     
    chaine_liste = chaine.split(", ")
    chaine_liste.sort()
    chaine_en_ordre = ", ".join(chaine_liste)
    print(chaine_en_ordre)

    EXPLICATION

Tout d'abord, il faut séparer les différents prénoms de la chaîne de caractère pour les mettre dans une liste.

En effet, on ne peut pas trier une chaîne de caractère, il va donc falloir passer par une liste.

Pour séparer les différents prénoms, on utilise la fonction split, qui permet de séparer la chaîne de caractère en 
plusieurs éléments, en opérant la séparation sur la virgule. Vous noterez qu'on a ajouté un espace après la virgule pour
 ne pas récupérer l'espace dans les prénoms de notre liste.

À ce stade-ci, nous avons donc la liste suivante :

['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien'] 

Il faut maintenant ordonner cette liste, ce que nous faisons à la ligne suivante avec la fonction sort.

chaine_liste.sort() 

Il ne reste plus qu'à joindre de nouveaux les prénoms de la liste avec le caractère que nous avons utilisé précédemment pour réaliser la séparation (une virgule suivie d'un espace). Pour cela, nous utilisons la méthode join.

chaine_en_ordre = ", ".join(chaine_liste) 

    POINTS IMPORTANTS À RETENIR

    On ne peut pas trier une chaîne de caractère.
    Pour séparer une chaîne de caractère en plusieurs éléments, on utilise la fonction split.
    Pour trier une liste, on utilise la fonction sort.
    Pour joindre différents éléments d'une liste par une chaîne de caractère, on utilise la méthode join.
"""

print("\nExercice 10")
# Exercice 10
# Notions abordées: Les operateurs mathematiques.
# Dans cet exercice, nous allons calculer le volume d'une sphere ayant pour rayon 10 centimetres.
# La formule pour calculer le volume d'une sphere est:
# (4pi/3)*rayon au cube
# rayon representant la valeur du rayon (defini dans le code par la variable 'rayon').
# Pour reussir l'exercice, vous devez uniquelment afficher le volume de la sphere, si vous rajoutez du texte en plus l'exercice ne sera pas
# valide (donc il suffit de laisser print(volume) à la fin et de calculer le volume à la ligne d'avant)
##
# rayon = 10.0
# volume = (4*pi)/3 * rayon**3
# print(volume)
"""
SOLUTION

    import math
    rayon = 10.0
    volume = (4.0 * math.pi / 3.0) * (rayon ** 3)
    print(volume)

EXPLICATION

Peu de difficulté dans cet exercice, le seul point sur lequel il fallait porter attention était l'import du module math, 
qui permet d'obtenir une valeur précise de pi, sans avoir besoin d'entrer le nombre à la main.

Le reste est assez simple, le symbole * permet de multiplier, tandis que le symbole ** permet de calculer le rayon 
puissance 3. Le symbole pour la division est la barre oblique (/). Pour obtenir le bon résultat, il fallait faire 
attention également aux parenthèses dans votre calcul.

POINTS IMPORTANTS À RETENIR

    Pour obtenir la valeur de pi, on importe le module math.

    Pour multiplier, on utilise *, pour mettre le rayon à la puissance 3 on utilise ** et pour diviser on utilise /
"""

print("\nExercice 11")
# Exercice 11
# Notions abordées: structures conditionnelles.
# Dans cet exercice, nous allons utiliser une structure conditionnelle pour verifier si a est plus grand ou non que 10.
# Dans ce cas-ci, a est egal à 12, votre script devra donc afficer 'a est plus grand que 10'
# Aller plus loin: Vous pouvez egalement rajouter une condition pour tester si la variable a contient bien un nombre.
# a = 12
##
# a = 12
# if a > 10:
#     print("a est plus grand que 10")
# elif a <= 10:
#     print("a est inferieur ou egal a 10")
"""
    SOLUTION

    a = 12
    if a > 10:
        print("a est plus grand que 10")
    elif a < 10:
        print("a est plus petit que 10")

    EXPLICATION

Exercice très simple pour ceux d'entres-vous qui sont habitués à Python.

Il s'agissait ici de faire une structure conditionnelle de base afin de vérifier si le nombre a était plus grand ou plus 
petit que 10.

La première condition if a > 10  sera exécutée si a est plus grand que 10.

La seconde condition, exécutée avec le elif a < 10 sera exécutée si a est plus petit que 10.

    POINTS IMPORTANTS À RETENIR

    Pour tester plusieurs conditions, on utilise la structure conditionnelle if, elif.
"""

print("\nExercice 12")
# Exerice 12
# Notions abordees: Les listes.
# Dans cet exercice, on contiue avec des operations assez simples utilisant les bases du langage Python.
# Le but ici est de crrer une liste de nombres allant de 5 à 15 en utilisant une fonction de base de Python.
# Pour valider l'exercice, vous devez afficher cette liste, en utilisant la fonction print.
##
# list1 = []
# for i in range(5, 16):
#     list1.append(i)
# print(list(list1))

"""
    SOLUTION

    liste_de_nombres = range(5, 16)
    print(list(liste_de_nombres))

    EXPLICATION

Pour créer facilement et rapidement des listes de nombres, on utilise la fonction range.

On peut l'utiliser en passant un seul nombre en argument, auquel cas la fonction range va créer une liste allant de 0 
jusqu'au nombre indiqué - 1 :

    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Vous voyez dans l'exemple ci-dessus, que la liste s'arrête à 9.

On peut également passer deux arguments, pour indiquer à la fonction à partir de quel nombre commencer, comme dans cet 
exercice :

    >>> list(range(5, 16))
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Là encore, vous remarquerez que la liste s'arrête à 15. Si nous voulons inclure le nombre 15 dans la liste, il faut donc 
passer en deuxième argument le nombre 16.

Attention ! Depuis Python 3, la fonction range ne retourne pas une liste mais un objet de type 'range'.

Ainsi, si vous voulez afficher cet objet en tant que liste, il vous faudra utiliser la fonction list pour convertir 
l'objet range en liste.

    POINTS IMPORTANTS À RETENIR

    La fonction range permet de générer une liste de nombres rapidement.
    Depuis Python 3, il faut utiliser la fonction list pour convertir le résultat de la fonction range en liste.
"""

print("\nExercice 13")
# Exercice 13
# Notions abordees: les listes.
# Dans cet exercice, on continue avec la fonction range, cette fois-ci pour creer une liste de nombres pairs allant de
# 1 à 100.
# Votre script doit afficher la liste, pensez donc à faire un print à la fin, si vous faites juste declarer la liste,
# l'exercice ne sera pas valide
##
# list1 = []
# for i in range(2, 101, 2):
#     list1.append(i)
# print(list(list1))
"""
    SOLUTION

    liste_nombre_pairs = range(2, 101, 2)
    print(list(liste_nombre_pairs))

    EXPLICATION

Dans cet exercice, on pousse un peu plus loin encore la fonction range, en fournissant un troisième argument, qui va 
indiquer à la fonction range l'écart que l'on veut entre chaque nombre.

Dans cet exemple-ci, on indique un écart de 2, ce qui aura comme effet de ne pas inclure les nombres impairs dans notre 
liste (puisque l'on commence à 2).

Un dernier point auquel il fallait faire attention là encore : pour intégrer le nombre 100 dans la liste, il fallait 
indiquer 101 comme deuxième argument, car la fonction range s'arrête à n - 1.

    POINTS IMPORTANTS À RETENIR

    On peut spécifier un écart à la fonction range en passant un nombre en troisième argument.
"""

print("\nExercice 14")
# Exercice 14
# Notions abordees: Les modules, la boucle for.
# Le but de cet exercice est de generer 6 lancer de des aleatoires, allant de 1 à 6.
# Votre script devra donc par exemple retour les lancer suivants:
# 1
# 2
# 3
# 4
# 5
# 6
##
# for i in range(1, 7):
#     j = random.choice(range(1, 7))
#     print(j)

"""
    SOLUTION

    import random
     
    for _ in range(6):
        nombre = random.choice(range(1, 7))
        print(nombre)

    EXPLICATION

Pour générer des nombres aléatoires, on utilise le module random qui dispose de plusieurs fonctions nous permettant de générer des nombres aléatoires.

Celle que nous utilisons dans le cadre de cette exercice est la fonction 'choice'. Cette fonction nous permet de choisir un élément aléatoire parmi une liste de plusieurs éléments.

Pour générer un nombre aléatoire de 1 à 6, nous utilisons donc la ligne de code suivante :

nombre = random.choice(range(1, 7)) 

Si vous ne voulez pas passer par une liste, vous pouvez également utiliser la fonction randint, comme ceci :

nombre = random.randint(1, 6) 

La deuxième indication de l'exercice était de générer 6 lancer de dés.

Pour cela, on utilise une boucle for et encore une fois la fonction range, pour répéter l'opération 6 fois :

    for _ in range(6):
        # Opération à répéter

Vous remarquerez que nous utilisons un nom de variable assez spécifique (un tiret du bas). En effet, ce nom de variable 
est une convention en Python lorsque l'on génère une variable que l'on ne compte pas utiliser. Ici, on veut juste 
répéter une opération un certain nombre de fois, mais nous ne faisons aucun usage de cette variable, nous utilisons donc 
un tiret du bas pour signifier à quelqu'un qui pourrait lire notre script que cette variable n'est pas utilisée à 
l'intérieur de la boucle.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément aléatoire dans une liste, on utilise la fonction choice du module random.
"""

print("\nExercice 15")
# https://www.udemy.com/course/python-exercices/learn/quiz/5365768#overview
"""
015 - Compter le nombre d'occurences d'une lettre dans une phrase

Notions abordees: Les chaines de caractere.
Dans cet exercice, nous cherchons à compter le nombre d'occurrence d'une lettre dans une chaine de caractere.
Ici, nous cherchons le nombre de fois que la lettre "o" apparait dans la phrase "Bonjour tout le monde".
Votre script devra donc retourner dans ce cas-ci le nombre 4 !
"""

# phrase = "Bonjour tout le monde"
# lettre_a_chercher = "o"
# compteur = 0
# for lettre in phrase:
#     if lettre == lettre_a_chercher:
#         compteur += 1
# print(compteur)

# # Here is a more pythonic solution
# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"
# print(phrase.lower().count(lettre_a_chercher))

"""
    SOLUTION

    lettre_a_chercher = "o"
    phrase = "Bonjour tout le monde"
    print(phrase.lower().count(lettre_a_chercher))

    EXPLICATION

Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.

Afin d'éviter toute confusion quant aux majuscules et minuscules, nous prenons le soin de convertir auparavant notre 
chaîne de caractère en minuscule avec la fonction lower.

    POINTS IMPORTANTS À RETENIR

    Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.
    Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.
"""

print("\nExercice 16")
# https://www.udemy.com/course/python-exercices/learn/quiz/5365770#overview
"""
016 - Récupérer un élément dans une liste

Notions abordees: les listes.
On retourne aux bases de Python dans cet exercice dans lequel vous devez tout simplement recuperer le premier element
de la liste.
Dans cet exemple, vous devez printer la chaine de caractere 'Pierre'
ma_liste = ["Pierre", "Paul", "Marie"]
"""
# ma_liste = ["Pierre", "Paul", "Marie"]
# print(ma_liste[0])
"""
    SOLUTION

    ma_liste = ["Pierre", "Paul", "Marie"]
    print(ma_liste[0])

    EXPLICATION

Exercice très simple pour les gens habitués à utiliser Python.

Pour récupérer un élément dans une liste basé sur sa position dans la liste, on utilise les crochets : []

Il suffit ensuite d'indiquer à l'intérieur des crochets l'indice de l'élément qu'on veut récupérer.

Ici, pour récupérer le premier élément de la liste, on utilise donc la syntaxe suivante :

ma_liste[0] 

Le seul point sur lequel il fallait être attentif est le fait qu'en programmation on commence toujours à compter à 
partir de 0.

Ainsi, pour récupérer le premier élément de la liste, on utilise l'indice 0 et non 1.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer le premier élément de la liste, on utilise les crochets et l'indice 0.
"""

print("\nExercice 17")

"""
017 - Récupérer des éléments dans une liste

Notions abordees: les listes.
On monte d'un cran dans cet exercice, dans lequel vous devez recuperer plusieurs elements de la liste.
Pour reussir cet exercice, vous devez printer le premier element ('Pierre'), le dernier element('Marie'), les deux premieres elements ('[Pierre','Paul]')
et les deux derniers elements (['Paul','Marie])
"""

# ma_liste = ["Pierre", "Paul", "Marie"]
# print(ma_liste[0])
# print(ma_liste[-1])
# print(ma_liste[0:2])
# print(ma_liste[1:])

"""
    SOLUTION

    ma_liste = ["Pierre", "Paul", "Marie"]
     
    print(ma_liste[0])
    print(ma_liste[-1])
    print(ma_liste[:2])
    print(ma_liste[-2:])

    EXPLICATION

Pour récupérer le premier élément, nous l'avons-vu précédemment, on utilise les crochets et l'indice 0.

Pour récupérer le dernier élément, peu importe la taille de la liste, on utilise l'indice -1 !

Pour récupérer les deux premiers éléments de la liste, on utilise une syntaxe un peu spéciale, qui se nomme 'slicing'.

En effet, plutôt que de spécifier un seul indice entre les crochets, on peut spécifier un indice de départ et un indice 
de fin.

Ainsi, pour récupérer les deux premiers éléments, on peut utiliser la syntaxe suivante :

ma_liste[0:2] 

Et puisque nous commençons depuis le début de la liste, on n'a même pas besoin d'indiquer le 0 et Python comprendra 
qu'on veut commencer depuis le début de la liste, jusqu'au deuxième élément inclus :

ma_liste[:2] 

Pour récupérer les deux derniers éléments, peu importe la taille de la liste, on utilise là encore un indice négatif et 
toujours le même principe de 'slicing' :

ma_liste[-2:] 

Encore une fois, pas besoin d'indiquer un indice après les deux points, on peut tout simplement laisser le deuxième 
indice vide, et le slice ira jusqu'à la fin de la liste.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer plusieurs éléments à l'intérieur d'une liste, on utilise le slicing : ma_liste[début:fin]
    Pour récupérer des éléments en partant de la fin, on peut utiliser des indices négatifs.
"""

print("\nExercice 18")
# # Exercice 18
# # Notions abordees: les listes.
# # On continue avec les listes. Cetter fois-ci, l'objectif de l'exercice est de recuperer un element sur deux dans la
# liste.
# # Votre scritp doit donc printer la liste suivante: [1, 3, 5, 7, 9]
# #
# ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(ma_liste[0:11:2])
"""
    SOLUTION

    ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(ma_liste[::2])

    EXPLICATION

Encore une fois, nous utilisons ici le 'slicing' pour récupérer uniquement un élément sur deux dans notre liste.

Nous pouvons indiquer en effet un troisième nombre entre les crochets et ce nombre indique le pas avec lequel nous 
voulons récupérer les éléments de notre liste.

Là encore, pas besoin d'indiquer d'indice spécifique pour les deux premiers nombres : en n'indiquant aucun indice, le 
slicing commencera automatiquement au début de la liste, ira jusqu'à la fin, en prenant seulement un élément sur deux :

    ma_liste[::2]

La syntaxe complète du slicing est donc la suivante :

ma_liste[indice_de_depart:indice_de_fin:pas] 

Si on veut récupérer les éléments de 4 à 25 avec un pas de 3 on fera donc :

    >>> ma_liste = range(100)
    >>> ma_liste[4:26:3]
    [4, 7, 10, 13, 16, 19, 22, 25]

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément sur deux, on utilise le slicing et on indique un pas de 2 à l'intérieur des crochets.
"""

print("\nExercice 19")
# Exercice 19
# Notions abordeeL les listes.
# Un autre petit exercice assez simple avec les listes, qui utilise une fonction qui n'est pas forcement connue de tous.
# Le but de cette exercice est d'ajouter plusieurs elements dans une liste en une seule fois !
# Mais attention, vous devez ajouter plusieurs elements dans la liste original, et non pas imbriquer une liste dans une
# autre.
# La liste de depart contient les elements 1, 2 et 3.
# La liste finale doit contenir les elements 1, 2, 3, 4, 5 et 6. Vous devez donc ajouter les elements 4, 5 et 6 à la
# liste originale.
# #
# ma_liste = [1, 2, 3]
# ma_liste = [1, 2, 3] + [4, 5, 6]
# print(ma_liste)
# # In a more pythonic way
# ma_liste = [1, 2, 3]
# ma_liste.extend([4, 5, 6])
# print(ma_liste)
"""
    SOLUTION

    ma_liste = [1, 2, 3]
    ma_liste.extend([4, 5, 6])
    print(ma_liste)

    EXPLICATION

Pour ajouter plusieurs éléments dans une liste en une seule fois, on utilise la fonction extend.

En effet, si vous utilisez la fonction append, vous allez ajouter une liste à l'intérieur de votre liste.

Pour ajouter plusieurs éléments d'un coup sans créer une sous-liste, il faut donc utiliser la fonction extend, qui va 
ajouter à la fin de votre liste les différents éléments que vous lui passez.

Il peut y avoir de la confusion dans le fait que vous devez passer une liste à la fonction extend.

Ainsi vous ne pouvez pas faire :

ma_liste.extend(4, 5, 6) 

Il faut à la place faire :

ma_liste.extend([4, 5, 6]) 

Bien que l'on passe une liste en argument de la fonction extend, cette fonction va bien ajouter les éléments à 
l'intérieur de votre liste sans créer de sous-liste.

    POINTS IMPORTANTS À RETENIR

    Pour ajouter plusieurs éléments dans une liste en une seule fois, on utilise la fonction extend.
"""

print("\nExercice 20")
# Exercice 20
# Dans cet exercice, vous allez devoir recuperer les elements communs aux deux listes.
# Dans ce cas-ci, votre liste commune devra contenir les nombres 5, 7, 10
# Vous pouvez utiliser les sets pour cet exercice
# Pour aller plus loin essayez de faire cet exercice sans utiliser les sets
# #
# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]
# print(list(set(liste_01).intersection(set(liste_02))))

# # le meme exercice avec deux boucles à la place du set()
# print("")
# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]
# ma_liste = []
# i, j = 0, 0
# for j in liste_01:
#     result = 0
#     for i in liste_02:
#         if (i == j):
#             ma_liste.append(i)
# print(ma_liste)

"""
    SOLUTION

    liste_01 = [1, 5, 6, 7, 9, 10, 11]
    liste_02 = [2, 3, 5, 7, 8, 10, 12]
     
    sliste_01 = set(liste_01)
    sliste_02 = set(liste_02)
     
    intersect = sliste_01.intersection(sliste_02)
    print(list(intersect))

    EXPLICATION

Dans cet exercice, nous passons par les sets pour récupérer les éléments communs à deux liste.

Pour convertir une liste en set, rien de plus facile, on utilise la fonction set :

sliste_01 = set(liste_01) 

Une fois que nos deux listes sont converties en set, nous pouvons utiliser des méthodes pour récupérer l'intersection, 
la différence et plein d'autres opérations du même style :

intersect = sliste_01.intersection(sliste_02) 

Il ne nous reste plus qu'à re-convertir notre set résultant en liste avec la fonction list :

resultat = list(intersect) 

    POINTS IMPORTANTS À RETENIR

    Pour convertir une liste en set, on utilise la fonction set.

    Pour récupérer les éléments communs à deux set, on utilise la méthode intersection.
"""

print("\nExercice 21")
# # Exercice 21
# # Dans cet article, l'objectif est de trier une liste qui contient des tuples:
# # liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# # Comme vous pouvez le voir, la liste contient des tuples qui ont comme premier element le nom d'un film, et comme
# deuxieme element leur note sur 5.
# # Le but de l'exercice est de trier ces tuples en fonction de la note qui leur a ete attribuee.
# # Votre script doit donc retourner la liste suivante:
# # [('Wall-E, 3), ('Blade Runner', 4), ('Harry Potter', 5)]
# #
# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# liste = sorted(liste, key=lambda colonnes: colonnes[1])
# print(liste)
"""
    SOLUTION

    liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
    liste.sort(key=lambda x: x[1])
    print(liste)

    EXPLICATION

Pas besoin d'aller chercher très loin pour résoudre cet exercice. En effet, la fonction sort accepte un argument dénommé 
'key', qui va vous permettre de trier la liste selon des critères spécifiques.

Dans ce cas-ci, nous donnons comme argument au paramètre key une fonction anonyme, qui elle même nous retourne l'élément
 1 de la variable qui est passée à x.

L'élément 1 du tuple correspond à la note du film, la fonction sort va donc trier les éléments de notre liste en 
fonction de cette élément et donc trier notre liste en fonction de la note accordée à chaque film.
"""

print("\nExercice 22")
# # Exercice 22
# # Dans cet exercice, nous allons recuperer la valeur de la cle 'prenom', contenue dans le dictionnaire 'employe'.
# # Votre script doit donc retourner la chaine de caractere 'Pierre'.
# # Aller plus loin : contstruisez votre script de sorte à ce qu'il ne produise aucune erreur si les cles du dictionnaire
# # venaient à etre modifiees.
# employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# # si la clef n'est pas trouve le script plante, imaginons que l'on cherche la clef 1 au lieu de 01
# print(employes['01']["identite"]["prenom"])
# # on retourne rien si la clef n'est pas trouve
# print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

"""
    SOLUTION

    employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
    print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

    EXPLICATION

Bien que cette ligne de code semble complexe, elle ne l'est pas tant que ça, car elle répète trois fois de suite le même
 principe.

Pour récupérer une valeur dans un dictionnaire, on peut tout d'abord utiliser les crochets de cette façon :

employes["01"] 

L'inconvénient de cette façon de faire c'est que notre script va retourner une erreur si la clé n'existe pas.

Afin de palier à ce problème nous utilisons à la place la méthode get, qui va par défaut nous retourner None si la clé 
n'existe pas.

Mais encore mieux, il est possible de spécifier un élément par défaut à retourner, autre que None, si la clé n'existe 
pas.

C'est ce principe que nous mettons en place ici. Nous récupérons la première clé et si celle-ci n'existe pas, nous 
retournons un dictionnaire vide :

employes.get("01", {}) 

Ainsi, nous pouvons chaîner plusieurs get à la suite, sans risquer de faire planter le script. En effet, si nous ne 
retournions pas de valeur par défaut et que la clé n'existe pas dans le dictionnaire, la 2e méthode 
get ne fonctionnerait pas car elle s'exécuterait sur None.

Donc si la première clé n'est pas trouvée, le get va agir sur un dictionnaire vide et ainsi de suite, évitant tout 
risque d'erreur.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer la valeur associée à une clé dans un dictionnaire, on peut utiliser la fonction get, qui permet de 
    spécifier une valeur par défaut à retourner si la clé n'est pas trouvée.
"""

print("\n Exercice 23")
# Exerice 23
# Notions abordees: les dictionnaires.
# On continue avec les dictionnaires ! Dans cet exercice, vous devez aaditionner toutes les valeurs
# du dictionnaire ensemble. Votre script doit donc retourner le nombre 8700.
# Allez plus loin: Esseayer de faire tenir votre scipt en une seule ligne
# #
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
# values = 0
# for value in employes.values():
#     result += value
# print(result)

# print("Exercice 23 bis")
# # autre solution:
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
# print(sum(employes.values()))
"""
    SOLUTION

    employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
    print(sum(employes.values()))

    EXPLICATION

Encore une fois un exercice assez simple pour qui connait bien Python.

Pour récupérer toutes les valeurs d'un dictionnaire, on peut utiliser la méthode values :

    >>> employes.values()
    dict_values([2500, 5000, 1200])

Et pour obtenir la somme de toutes ces valeurs, rien de plus simple que d'utiliser la fonction sum :

    >>> sum(employes.values())
    8700

    POINTS IMPORTANTS À RETENIR

    Pour récupérer toutes les valeurs d'un dictionnaire, on utilise la méthode values.
    Pour faire la somme de plusieurs nombres, on utilise la fonction sum.
"""

print("\n Exercice 24")
# # Notions abordees: Les modules.
# # Nous passons maintenant avec un exercice simple sur les modules.
# # Le script actuel ne fonctionne pas et vous retournera une erreur. A vous de trouver où se situe l'erreur afin que le script fonctionne.
# # Votre script doit au final retourner un nombre aleatoire compris entre 0 et 5.
# #
# nombre_aleatoire = random.randint(0, 5)
# print(nombre_aleatoire)
"""
    SOLUTION

    import random
     
    nombre_aleatoire = random.randint(0, 5)
    print(nombre_aleatoire)

    EXPLICATION

Pour utiliser une fonction contenue à l'intérieur d'un module, il est impératif de préfixer cette fonction par le nom du 
module.

Dans cet exercice, on import le module comme suit :

import random

Pour utiliser la fonction randint, il faut donc faire :

random.randint(0, 5)

Si nous voulons utiliser directement la fonction randint, il est possible de le faire avec une syntaxe d'import 
légèrement différente :

from random import randint   

De cette façon, on importe directement la fonction randint et non pas tout le module random. La fonction randint est 
donc directement accessible dans l'espace global de notre script :

randint(0, 5) 

    POINTS IMPORTANTS À RETENIR

    Pour utiliser une fonction à l'intérieur d'un module, il ne faut pas oublier de préfixer la fonction par le nom du module.
    Pour importer une fonction à l'intérieur d'un module directement dans l'espace global de notre script, on peut 
    utiliser la syntaxe from module import fonction .
"""

print("\n Exercice 25")
# # Notions abordees: syntaxe.
# # On continue avec les erreurs et la syntaxe. Le script suivant ne fonctionne pas, à vous de trouver pourquoi et le
# corriger.
# # Votre script doit retourner la liste [2, 6, 12, 20, 42, 56, 90]
# liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

# resultat = [i*(i+1 % (i*5)) for i in sorted(list(set(liste)))]
# print(resultat)

"""
    SOLUTION

    liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]
    resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
    print(resultat)

    EXPLICATION

Il est courant de faire ce genre d'erreurs dans des scripts qui contiennent beaucoup de parenthèses et crochets.

Une bonne façon de vérifier si vous n'avez pas oublié une parenthèse ou un crochet est de compter dans un sens le nombre
 de parenthèse / crochet ouvrant, et ensuite de compter dans l'autre sens si vous avez bien le 
même nombre de parenthèse / crochet fermant.

POINTS IMPORTANTS À RETENIR

    Une seule chose : attention à la syntaxe !
"""

print("\n Exercice 26")
# # Notions abordees: Les modules, les variables.
# # Dans cette exercice, nous allons importer une variable d'un autre module dans notre script principal.
# # Dans le fichier constants.py se trouve une variable 'nom' qui contient le mot 'Udemy'.
# # Le but de l'exercice est d'importer cette variable dans le fichier exercice.py pour l'afficher grace à la fonction
# print.
# #
# print(constants.nom)

"""
    SOLUTION

    import constants
    print(constants.nom)

    EXPLICATION

Rien de plus simple dans cet exercice ! Il suffisait d'importer le module constants et de faire un print de la variable 
'nom' contenue à l'intérieur de ce module. Un exercice simple, mais qui nécessite de bien comprendre le fonctionnement 
des modules et les possibilités qu'ils offrent.

    POINTS IMPORTANTS À RETENIR

    Pour importer une variable d'un module, il suffit d'importer le module dans lequel la variable est contenue.
"""

print("\n Exercice 27")
# # Afficher le chemin du script python en cours
# #
# fichier_courant = __file__
# dossier_parent = os.path.dirname(fichier_courant)
# dossier_image = os.path.join(dossier_parent, "images")
# print(dossier_image)

print("\n Exercice 28")
# https://www.udemy.com/course/python-exercices/learn/quiz/5365858#overview
"""
028 - Récupérer l'extension d'un fichier

+ Notions abordees: le module OS.
Le but de cet exercice est de recuperer l'extension d'un fichier à l'aide du module OS.
Dans cas-ci, vous devez recuperer l'extension du fichier python.exe
Votre script doit retourner l'extension sans le point. Vous devez donc recuperer 'exe'.
"""

# fichier = "C:/Python36/python.exe"

# _, ext = os.path.splitext('C:/Python36/python.exe')
# print(ext)

"""
    SOLUTION

    import os
     
    fichier = "C:/Python36/python.exe"
     
    extension = os.path.splitext(fichier)[1]
    extension = extension.strip(".")
     
    print(extension)

    EXPLICATION 

Dans cet exercice, nous utilisons le module os, qui contient déjà des fonctions qui nous permettent de gérer ce genre de
 situations.

Depuis le module os, nous pouvons importer le module path, qui donne accès à tout un tas de fonctions permettant de 
manipuler des chemins.

La fonction splitext nous permet de séparer un chemin de son extension. Cette fonction nous retourne donc un tuple, qui 
contient le chemin sans l'extension en premier élément, et l'extension seule en deuxième 
élément :

    >>> import os
    >>> fichier = "C:/Python36/python.exe"
    >>> extension = os.path.splitext(fichier)[1]
    '.exe'

Pour récupérer l'extension sans le point, il ne nous reste qu'à utiliser la fonction strip :

    extension = extension.strip(".")

    POINTS IMPORTANTS À RETENIR 

    Pour manipuler des chemins de dossier, on utilise le module os.path.

    Pour séparer un chemin de son extension, on utilise la fonction os.path.splitext.
"""

print("\n Exercice29")
# https://www.udemy.com/course/python-exercices/learn/lecture/11364990#overview
"""
Exercice 29
Acceder à une variable d'environnement PATH et HOME
"""
# #
# print(os.environ.get('PATH'))
# print("")
# print(os.environ.get)  # retourne toutes les variables d'environnement


"""
    SOLUTION

    import os
     
    home_var = os.environ.get("HOME")
    print(home_var)
"""

print("\n Exercice30")
# # Exercice 30
# # Calculer le temps d'execution d'un script
# #
# start_time = time.time()
# _ = [i*2 for i in range(9999999)]
# print("Temps d'execution: %s secondes ---" % (time.time()-start_time))
"""
    SOLUTION

    from time import time
     
    a = time()
    _ = [i*2 for i in range(9999999)]
    print(f"Temps d'exécution: {time() - a}s")
"""

print("\n Exercice31")
# # Exercice 31
# # Notions abordees: les structures conditionnelles, les nombres.
# #
# a = 0
# if a is not None:
#     print("la valeur de a est %i:" % a)
"""
    SOLUTION

    a = 0
    if a is not None:
        print(a)

    EXPLICATION

Exercice qui s'attaque à une erreur assez sournoise et courante.

Dans ce cas-ci, on veut vérifier que la variable a contient bien un nombre.

Pour rapidement vérifier qu'une variable contient des données, on peut utiliser une structure conditionnelle de base.

Par exemple pour vérifier qu'une liste n'est pas vide, on peut faire :

    ma_liste = [1, 2, 3]
    if ma_liste:
        print("La liste n'est pas vide")

Au lieu de :

    ma_liste = [1, 2, 3]
    if len(ma_liste) > 0:
        print("La liste n'est pas vide")

Vous conviendrez que la première façon de faire est plus concise est lisible. Cependant, en prenant l'habitude de cette 
syntaxe, on peut tomber dans l'écueil qu'il fallait résoudre dans cet exercice.

En effet, imaginons qu'à la place d'une liste, nous récupérons cette fois-ci un nombre entier. Si le nombre récupéré est
 0, alors la structure conditionnelle ne sera pas vérifiée, car 0 est équivalant à False.

C'est pourquoi dans ce cas-ci, nous ne pouvons pas utiliser la syntaxe simplifiée if variable, il faut donc vérifier 
explicitement que la variable n'est pas égale à None :

    a = 0
    if a is not None:
        print("La variable n'est pas égale à None")

    POINTS IMPORTANTS À RETENIR

    Le nombre 0 est équivalant au boolean False.

    Pour vérifier explicitement qu'une variable n'est pas égale à None, il vaut mieux utiliser la syntaxe if variable is
     not None.
"""

# print("\n Exercice32")


# # Exercice 32
# # Notions abordees: Les chaines de caracteres.
# # Le but de cet exercice est d'afficher dans le print le nom et le prenom contenu dans les variables respectives.
# # Vous devez pour ceci utiliser la fonction format afin.
# # Votre script doit donc afficher au final: "Bonjour je m'appelle Pierre Dupont"
# # https://vbaforexcel.wordpress.com/2015/05/19/affichage-fonction-print/
# #
# prenom = "Pierre"
# nom = "Dupont"
# print("Bonjour je m'appelle Mr " + nom + " " + prenom)
# print("Bonjour je m'appelle Mr {0} {1}" .format(nom, prenom))
# print("Bonjour je m'appelle Mr %s, %s" % (nom, prenom))

"""
    SOLUTION

    prenom = "Pierre"
    nom = "Dupont"
    print("Bonjour je m'appelle {prenom} {nom}".format(prenom=prenom, nom=nom))

    EXPLICATION

Il est possible de réussir cet exercice sans utiliser la fonction format, en concaténant des chaînes de caractère avec 
le symbole +.

Cependant, vous remarquerez que la méthode format est souvent plus facile à utiliser et procure un résultat plus facile 
à décoder.

La méthode format s'applique directement sur une chaîne de caractère et fonctionne avec les accolades. On peut indiquer 
des indices à l'intérieur des accolades :

    "Bonjour je m'appelle {0} {1}".format(prenom, nom)

Mais aussi utiliser directement, comme dans le cas de cet exercice, des 'tags' qui vont nous permettre de remplir les 
espaces occupés par les accolades avec des variables :

    "Bonjour je m'appelle {prenom} {nom}".format(prenom="Pierre", nom="Dupont")

    POINTS IMPORTANTS À RETENIR

    Pour concaténer des chaînes de caractère, on peut utiliser directement la fonction format avec les accolades pour 
    insérer des variables à l'intérieur d'une chaîne de caractère.
"""

print("\n Exercice33")
# # Exercice 33
# # Notions abordees: Les chaines de caractere.
# # Dans cet exercice, vous allez devoir inverser l'ordre des lettres d'un mot.
# # Dans cet exemple-ci, le mot est 'Udemy' votre script doit donc retourner la chaine de caractere 'Ymedu'
# # Pour valider l'exercice, il faut que la premiere lettre de votre chaine de caractere resultat soit
# # en majuscule("Ymedu" et non 'ymedU')
# # Aller plus loin: Faites tenir votre script en une seule ligne
# #
# mot = "Udemy"
# print(mot[::-1].capitalize())

# # autre possibilite:
# mot = "Udemy"
# resultat = []
# for lettre in reversed(mot):
#     resultat.append(lettre)
# resultat_formate = "".join(resultat)
# print(resultat_formate.capitalize())
"""
    SOLUTION

    mot = "Udemy"
     
    resultat = []
     
    for lettre in reversed(mot):
        resultat.append(lettre)
     
    resultat_formate = "".join(resultat)
    print(resultat_formate.capitalize())

    EXPLICATION

Tout d'abord, commençons par dire qu'il est possible de réaliser cet exercice en une seule ligne, avec les slices :

    >>> mot = "Udemy"
    >>> print("Udemy"[::-1].capitalize())
    "Ymedu"

Mais pour faire durer un peu le plaisir, je vous montre une façon de faire un peu moins directe et qui vous permettra 
d'utiliser un peu plus de fonctions natives de Python.

Tout d'abord, pour inverser l'ordre des lettres, nous utilisons la fonction reversed :

    >>> mot = "Udemy"
    >>> print(reversed(mot))
    <reversed object at 0x10386b278>

Cette fonction nous retourne un object 'reversed', qui est en fait un itérateur. Nous pouvons donc passer à travers cet 
itérateur avec une boucle for et ajouter chaque lettre dans une liste :

    for lettre in reversed(mot):
        resultat.append(lettre)

Nous nous retrouvons ainsi avec une liste contenant chaque lettre dans l'ordre inverse.

Pour terminer, nous pouvons utiliser la fonction join pour joindre les éléments de la liste ensemble et la fonction 
capitalize pour mettre une majuscule au début du mot :

    resultat_formate = "".join(resultat)
    print(resultat_formate.capitalize())

    POINTS IMPORTANTS À RETENIR

    Pour inverser une chaîne de caractère, on peut utiliser le slicing [::-1] ou la fonction reversed.
    Pour joindre les éléments d'une liste ensemble, on utilise la fonction join.
    Pour mettre une majuscule sur la première lettre d'un mot, on utilise la fonction capitalize.
"""

print("\n Exercice34")
# # Exercice 34
# # Notions abordees: le module random.
# # Dans cet exercice, nous allons melanger les lettres d'un mot grace au module random.
# # Le mot resultant devra commencer par une majuscule. Dans cet exercice nous allons melanger le mot 'Bonjour'.
# # Votre script devra melanger les lettres de ce mot pour donner par exemple: 'Ojoubr'.
# #
# a = list("bonjour")
# random.shuffle(a)
# print(("".join(a)).capitalize())

"""
    SOLUTION

    import random
     
    mot = "Bonjour"
    mot = list(mot)
     
    random.shuffle(mot)
     
    mot_random = "".join(mot).capitalize()
    print(mot_random)

    EXPLICATION

Pour facilement mélanger les lettres d'un mot, nous allons utiliser le module random et la fonction shuffle.

La fonction shuffle fonctionne sur des listes et permet de mélanger les éléments de la liste qui lui est passée.

Nous allons donc commencer par convertir notre mot en liste avec la fonction list :

    mot = list(mot)

Nous utilisons ensuite la fonction shuffle du module random pour mélanger la liste :

    random.shuffle(mot)

Il ne reste plus qu'à rassembler tous les éléments de la liste avec la fonction join et de remettre la majuscule à la bonne place avec la fonction capitalize :

    mot_random = "".join(mot).capitalize()

    POINTS IMPORTANTS À RETENIR

    Pour mélanger les éléments d'une liste, on utilise la fonction shuffle du module random.
    Pour convertir une chaîne de caractères en liste, on utilise la fonction list.
"""

print("\n Exercice35")
# # Exercice 35
# # Notions abordees: la fonction format.
# # Dans cet exercice, nous voulons tronquer le nombre de decimales contenues apres la virgule dans la variable 'nombre', par le nombre
# # contenu dans la variable 'decimales'.
# # votre script doit donc afficher: 'Nombre tronque:2938.489'
# #
# nombre = 2938.48872
# decimale = 3
# print("Nombre tronqué: {nombres:.{decimales}f}".format(
#     nombres=nombre, decimales=decimale))

# print("test de la valeur toto: {toto}".format(toto=decimale))
"""
    SOLUTION

    nombre = 2938.48872
    decimales = 3
     
    print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))

    EXPLICATION

Dans cet exercice, nous continuons d'explorer cette fabuleuse fonction format qui cache de nombreuses fonctionnalités assez avancées.

En effet, il est possible d'utiliser la syntaxe suivante pour tronquer le nombre de décimales après la virgule d'un nombre :

{nombre:.3f} 

'nombre' correspond au nom du tag que l'on utilise comme nom de paramètre dans la fonction format.

Nous avons ensuite deux points, un point, un nombre qui détermine le nombre de décimales après la virgule que l'on 
souhaite conserver (ici 3) et pour finir la lettre f.

Je l'avoue, ce n'est pas la syntaxe la plus facile à retenir, mais c'est vraiment très efficace pour pouvoir rapidement 
afficher un nombre tronqué dans une chaîne de caractère.

    SOLUTION ALTERNATIVE

Vous pouvez également utiliser la fonction round afin de tronquer le nombre de décimales :

    nombre = 2938.48872
    decimales = 3
     
    solution = round(nombre, decimales)
     
    print("Nombre tronqué: {}".format(solution))

Il vous faudra cependant tout de même utiliser la méthode format afin d'insérer le nombre tronqué à l'intérieur de la 
chaîne de caractères.

    POINTS IMPORTANTS À RETENIR

    On peut tronquer directement un nombre pour n'afficher qu'une certaine parties des décimales après la virgule grâce 
    à la fonction format et la syntaxe {nombre:.3f}.
"""

print("\n Exercice36")
# # Exercice 36
# # Notions abordees: structures conditionnelles.
# #
# a = 20
# print("Vous etes majeur !") if a >= 18 else print("Vous etes minieur")
"""
    SOLUTION

    a = 20
    majeur = print("Vous êtes majeur !") if a >= 18 else print("Vous êtes mineur")

    EXPLICATION

Pour résoudre cet exercice, il fallait utiliser ce qu'on appelle un opérateur ternaire.

De cette façon, nous pouvons réaliser une condition if, else sur une seule ligne.

Il est important de noter qu'il n'est possible d'inclure des print dans un opérateur ternaire que depuis la version 3 de
 Python.

À noter aussi, il n'est pas possible d'inclure un elif dans un opérateur ternaire.
Nous n'avons donc que deux choix possibles avec le if et le else, en suivant la syntaxe suivante :

variable = expression if condition else expression 

    POINTS IMPORTANTS À RETENIR

    Pour réaliser une structure conditionnelle sur une seule ligne, on utilise un opérateur ternaire.
"""

print("\n Exercice37")
# # Exercice 37
# # Age du chien
# #
# age = int(input("Entrer l'age du chien: "))
# result = 0
# if (age < 0):
#     print("Vous devez entrer un age positif!")
# elif (age <= 2):
#     result = age * 10.5
#     print("l'age du chien est {0} ans a l'echelle humaine".format(result))
# else:
#     result = 21 + (age - 2) * 4
#     print("l'age du chien est %d ans a l'echelle humaine" % result)

"""
    age = int(input("Entrez l'âge du chien: "))
     
    if age < 0:
        print("Vous devez entrer un âge positif!")
        exit()
    elif age <= 2:
        d_age = age * 10.5
    else:
        d_age = 21 + (age - 2) * 4
     
    print("L'âge du chien en âge humain est", d_age)
"""

print("\n Exercice38")
"""
038 - Trier trois nombres sans conditions

Notions abordees: Fonctions de base.
Dans cet exercice, nous allons trier trois nombres sans avoir recours à l'utilisation de structures conditionnelles
ni à la fonction sort(). A l'aide des fonctions de base de Python, vous allez devoir trouver un moyen de trier les
variables 'a', 'b', 'c' du plus petit au plus grand.
Dans le cas de cet exercice, avec a = 4, b = 6 et c = 2, votre script doit printer:'les nombres dans l'ordre sont
2, 4 et 6'.
"""

# a = 4
# b = 6
# c = 2
# a1 = min(a, b, c)
# a3 = max(a, b, c)
# a2 = (a + b + c) - a1 - a3
# print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))
"""
    SOLUTION

    a = 4
    b = 6
    c = 2
     
    a1 = min(a, b, c)
    a3 = max(a, b, c)
    a2 = (a + b + c) - a1 - a3
     
    print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))

    EXPLICATION

Dans cet exercice, il fallait penser un peu plus à la solution car il était interdit d'utiliser les structures 
conditionnelles.

Pour résoudre ce problème, nous commençons par trouver le nombre le plus petit et le nombre le plus grand entre les 
trois variables a, b et c grâce aux fonctions min et max.

Cela nous donne donc la variable a1 et la variable a3 :

    a1 = min(a, b, c)
    a3 = max(a, b, c)

Puisque nous ne pouvons pas savoir d'avance quelles variables parmi a, b et c vont correspondre à la valeur la plus 
petite et la valeur la plus grande, il nous faut faire un peu d'arithmétique pour trouver la valeur du milieu.

Pour se faire, nous additionnons les trois valeurs ensemble (a, b et c) puis nous soustrayons les deux variables 
précédemment trouvées avec la fonction min et max :

    a2 = (a + b + c) - a1 - a3

    POINTS IMPORTANTS À RETENIR

    Pour trouver la valeur maximale ou minimale entre plusieurs variables, on utilise les fonctions min et max.
"""

print("\n Exercice39")
# # Dans cet exercice, nous sommes en presence d'une boucle while infinie! En l'etat actuel, le script ne s'arretera
# jamais et la phrase 'Exercice reussi!'
# # ne s'affichera jamais.
# # Vous devez modifier la boucle while afin de sortir et d'afficher la phrase 'Exercice reussi !'
# i = 0
# while i < 10:
#     i+=1
# print("Exercice reussi!")
"""
    SOLUTION

    i = 0
     
    while i < 10:
        pass
        i += 1
     
    print("Exercice réussi !")

    EXPLICATION

Une erreur courante que font beaucoup de débutants est de créer une boucle infinie.

La boucle while, bien que très pratique, est également assez dangereuse à manipuler pour qui ne fait pas attention à la 
condition de sortie.

C'était le cas dans cet exercice, dans lequel la variable i n'était jamais incrémentée et donc toujours plus petite que 
10.

Il fallait donc incrémenter la valeur de i pour pouvoir arriver à un moment dans le script où i soit plus grand que 10 
et que la condition du while soit fausse.

Peu importe la boucle while que vous comptez faire, je vous conseille toujours de vous prévoir une porte de sortie de ce
 genre : incrémentez une variable à chaque itération de la boucle et sortez de la boucle une fois que la variable 
 atteint un nombre trop élevé, afin d'éviter de faire planter votre script si votre condition initiale n'est jamais 
 fausse.

    POINTS IMPORTANTS À RETENIR

    Pour incrémenter un nombre entier, on utilise la syntaxe variable += 1.
"""

print("\n Exercice40")
# # Exercice 40
# # On continue avec les boucles, cette fois-ci la boucle for.
# # Le but de cet exercice est de printer l'index de chaque lettre du mot 'Python'.
# # Votre script doit donc retourner:
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# #
# mot = "Python"
# for i in range(len(mot)):
#     print(i)

"""
    SOLUTION

    mot = "Python"
    for i in range(len(mot)):
        print(i)

    EXPLICATION

La fonction range a besoin d'un nombre pour créer une liste de nombres de la longueur du nombre passé en argument.

Ici dans le script, nous passions directement la variable mot - qui est une chaîne de caractère - à la fonction range, 
ce qui nous retournait logiquement une erreur.

À la place, il fallait utiliser la fonction len pour calculer la longueur de la chaîne de caractère et ainsi passer ce 
nombre à la fonction range pour pouvoir itérer sur la liste obtenue.


    POINTS IMPORTANTS À RETENIR

    Pour calculer la longueur d'une chaîne de caractère, on utilise la fonction len.
"""

print("\n Exercice41")

# # Exercice 41 Dans cet exercice, la fonction 'multiplicateur_mot' retourne une erreur. Trouvez cette erreur et
# # modifiez la fonction pour qu'elle ne retourne plus d'erreur. Il y a plusieurs facons de fixer cetter erreur. Votre
# # script doit afficher 5 fois le mot 'Bonjour' à la suite (parce que dans la vie, il est important de faire des
# # scripts bien eleves...)
#
# def multiplicateur_mot(mot, mult=5):
#     """
#
#     Args:
#         mot: chaine de caracteres
#         mult: entier
#
#     Returns: n (mult) fois le mot (mot)
#
#     """
#     return mot * mult
#
#
# mot_multiplie = multiplicateur_mot(mot="Bonjour")
# print(mot_multiplie)

"""
    SOLUTION

    def multiplicateur_mot(mot, mult=5):
        return mot * mult
     
    mot_multiplie = multiplicateur_mot(mot="Bonjour")
    print(mot_multiplie)

    EXPLICATION

L'ordre des paramètres par défaut dans une fonction a son importance ! En effet, si vous définissez une valeur par 
défaut pour un paramètre qui se trouve en première position, vous avez l'obligation de définir une valeur par défaut 
pour tous les paramètres qui suivent.

La façon rapide de régler l'erreur qui se trouvait dans ce script était donc soit de définir une valeur par défaut pour 
les deux paramètres de la fonction, soit d'inverser l'ordre des paramètres, ce que nous avons fait dans la solution 
proposé ci-dessus.

    POINTS IMPORTANTS À RETENIR

    L'ordre des paramètres dans une fonction a son importance ! Vous ne pouvez pas mettre un paramètre sans valeur par 
    défaut après un paramètre qui en a une.
"""

print("\n Exercice42")
# # Exercice 42
# # On continue avec les erreurs à trouver dans les fonctions !
# # Cette fois-ci, le script ne retourne pas d'erreur mais n'affiche pas le resultat escompte.
# # La fonction addition devrait nous permettre d'additionner deux nombres ensemble. Cependant, quand on print la
# variable 'resultat'.
# # Python nous retourne 'None', au lieu du resultat de l'addition(ici 15).
# # Modifiez la fonction pour le print de 'resultat affiche le resultat de l'addition
# # def addition(a, b):
# #   c = a + b
# #
# # resultat = addintion(5, 10)
# # print(resultat)
# #
#
# def addition(a, b):
#     c = a + b
#     return c
#
#
# resultat = addition(5, 10)
# print(resultat)

"""
    SOLUTION

    def addition(a, b):
        c = a + b
        return c
     
    resultat = addition(5, 10)
    print(resultat)

    EXPLICATION

Une fonction peut, dans certains cas, ne pas retourner de résultat (par exemple, une fonction qui exécute plusieurs 
print à la suite, pour afficher un message de bienvenue par exemple, n'a pas besoin de retourner 
de valeur spécifique).

Cependant, ici, la fonction sert à calculer la somme de deux valeurs. Il faut donc retourner d'une façon où d'une autre 
le résultat de cette addition.

Pour retourner une valeur dans une fonction, on utilise le mot clé return, comme ici :

    return c

Cela nous permet de récupérer la valeur de l'addition lors de l'appel de la fonction dans une variable :

    resultat = addition(5, 10)

    POINTS IMPORTANTS À RETENIR

    Pour retourner une valeur à l'intérieur d'une fonction, on utilise le mot clé return.
"""

print("\n Exercice43")
# # Exercice 43
# # Notions abordees: boucle for, fonction range.
# # On continue avec la boucle for, cette fois-ci pour afficher la table de multiplication d'un nombre.
# # Dans ce cas-ci, votre script doit afficher la table de multiplication du nombre 7.
# # 0 * 7 = 0
# # 1 * 7 = 7
# # 2 * 7 = 14
# # 3 * 7 = 21
# # 4 * 7 = 28
# # 5 * 7 = 35
# # 6 * 7 = 42
# # 7 * 7 = 49
# # 8 * 7 = 56
# # 9 * 7 = 63
# # 10 * 7 = 70
# # Attention aux espaces entre chaque nombre et symbole !
# #
# number = 7
# for i in range(11):
#     print("{i} x {number} = {result}".format(
#         i=i, number=number, result=i * 7))

"""
    SOLUTION

    nombre = 7
     
    for i in range(11):
        print("{i} x {nombre} = {resultat}".format(i=i, nombre=nombre, resultat=i*nombre))

    EXPLICATION

Ici, nous faisons tous les calculs nécessaires directement à l'intérieur de la méthode format.

Pour commencer, nous bouclons à travers une liste contenant les nombres de 0 à 10, grâce à la fonction range :

    for i in range(11):

Nous affichons ensuite dans la chaîne de caractère formattée, le nombre courant de la boucle, contenu dans la variable 
i, le nombre pour lequel nous affichons la table de multiplication, contenu dans la variable 
nombre, puis la multiplication de l'un par l'autre (i * nombre).

    POINTS IMPORTANTS À RETENIR

    Il est possible de faire des opérations mathématiques directement à l'intérieur de la méthode format, afin d'insérer
     le résultat de ces opérations à l'intérieur d'une chaîne de caractère.
"""

print("\n Exercice44")
# # Exercice 44
# # Notions abordees: boucle for
# # Les boucles for, encore et toujours, cette fois-ci, un exercice dans lequel nous allons recuperer à la fois l'indice
# et l'element
# # sur lequel nous bouclons dans chaque iteration de la boucle for.
# # votre script doit donc retourner dans ce cas-ci:
# # 0 Pierre
# # 1 Paul
# # 2 Marie
# # solution 1
# #
# liste = ["Pierre", "Paul", "Marie"]
# index = 0
# for name in liste:
#     print("{index} {name}".format(index=index, name=name))
#     index += 1

# # solution 2:
# liste = ["Pierre", "Paul", "Jacques"]
# for i in range(len(liste)):
#     print("%d %s" % (i, liste[i]))

# # Correction:
# liste = ["Pierre", "Paul", "Marie"]
# for i, nom in enumerate(liste):
#     print(i, nom)

"""
    SOLUTION

    liste = ["Pierre", "Paul", "Marie"]
    for i, nom in enumerate(liste):
        print(i, nom)

    EXPLICATION

Pour récupérer un élément dans une liste ainsi que son indice dans une boucle for, une erreur souvent faite par les 
débutants, est de passer par la fonction range et la fonction len, ce qui alourdit le code et le rend difficilement 
lisible :

    for i in range(len(liste)):
        print(i, liste[i]))

Pour récupérer dans une boucle for à la fois l'élément sur lequel on boucle ainsi que son indice, on préfère utiliser la
 fonction enumerate :

    for i, nom in enumerate(liste):
        print(i, nom)

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément et son indice dans une boucle for, on utilise la fonction enumerate.
"""

print("\n Exercice45")
# # Exercice 45
# # Notions abordees: boucle for, structure conditionnelle.
# # Le but de cet exercice est de recuperer dans une seconde liste, la liste 'nombre_pairs', uniquelment les nombres
# # pairs de la premiere liste.
# # votre script doit donc printer la liste suivante:
# # [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48]
# #
# nombres = range(50)
# nombres_pairs = []
# for i in nombres:
#     if (i % 2) == 0:
#         nombres_pairs.append(i)

# print(nombres_pairs)

"""
    SOLUTION

    nombres = range(50)
    nombres_pairs = []
     
    for i in nombres:
        if i % 2 == 0:
            nombres_pairs.append(i)
     
    print(nombres_pairs)

    EXPLICATION

Pour résoudre cet exercice, il fallait faire appel à un opérateur mathématique quelque peu méconnu : l'opérateur modulo.

Cet opérateur est un peu l'alter égo de l'opérateur division, puisqu'il nous permet de récupérer le reste de la division
 d'un nombre par un autre.

Par exemple, 10 % 2 retournera 0, car 10 / 2 est égal à 5 et la division ne laisse aucun reste.

Par contre, 11 % 2 retournera 1, car 11 / 2 est égal à 5 et il reste 1.

Le modulo est donc un opérateur mathématique très utilisé pour vérifier si un nombre est pair ou non.
En effet, un nombre divisible par 2 et ne laissant aucun reste, est pair.

On utilise donc le modulo dans cet exercice pour tester chaque élément de la liste dans une boucle for en vérifiant si 
le modulo du nombre par 2 est égal ou non à 0 :

    for i in nombres:
        if i % 2 == 0:
            nombres_pairs.append(i)

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si un nombre est pair, on utilise l'opérateur mathématique modulo, en vérifiant si le modulo de notre 
    nombre par 2 est égal ou non à 0.
"""

print("\n Exercice46")
# # Exercice 46
# # Notions abordees: boucle for, structure conditionnelle, comprehension liste.
# # On continue avec le meme exercice qui consiste à recuperer seulement les nombres pairs d'une liste.
# # Cette fois-ci, nous allons effectuer le meme code que precedemment mais en une seule ligne, grace
# # aux comprehensions de liste.
# # Votre script, pour etre valide, doit donc tenir en 3 lignes: une ligne pour declarer la liste, une ligne
# # pour la trier, et une derniere ligne pour printer la liste.
# #
# nombres = range(50)
# nombre_pairs = [i for i in nombres if i % 2 == 0]
# print(nombre_pairs)

"""
    SOLUTION

    nombres = range(50)
    nombres_pairs = [i for i in nombres if i % 2 == 0]
    print(nombres_pairs)

    EXPLICATION

Dans cet exercice, nous récupérons les nombres pairs de la liste, toujours avec l'opérateur modulo, mais cette fois-ci 
en utilisant une compréhension de liste, ce qui permet de faire tenir le code en une seule ligne.

La syntaxe de la compréhension de liste est assez simple :

    [expression for expression in liste if condition]

La compréhension de liste nous permet donc d'exécuter une boucle for sur une seule ligne :

    [i for i in nombres]

La compréhension de liste retourne une nouvelle liste, que l'on peut stocker dans une variable :

    nouvelle_liste = [i for i in nombres]

Pour finaliser cet exercice, il ne reste plus qu'à ajouter la condition qui permet de vérifier si un nombre est pair ou non dans la compréhension de liste :

    nouvelle_liste = [i for i in nombres if i % 2 == 0]

    POINTS IMPORTANTS À RETENIR

    Pour exécuter une boucle for sur une seule ligne et ainsi trier les éléments d'une liste, on utilise une compréhension de liste.
"""

########################
# Niveau intermediaire #
########################
print("\n Exercice47")
# Exercice 47
# Notion abordees: boucle for.
# Le but de cet exercice est de calculer la somme de chaque chiffre d'un nombre.
# Dans ce cas-ci, votre script doit retourner le nombre 22(2 + 0 + 9 + 8 + 1 + 2)
# #
# nombre = 209812
# somme = 0
# for c in str(nombre):
#     somme += int(c)
# print(somme)

# # Aller plus loin : Essayez de faire tenir votre script en une seule ligne, grace aux comprehensions de liste.
# nombre = 209812
# print(sum([int(i) for i in str(nombre)]))

"""
    SOLUTION

    nombre = 209812
    somme = sum([int(i) for i in str(nombre)])
    print(somme)

    EXPLICATION

Ici, nous utilisons une compréhension de liste pour additionner chaque chiffre du nombre 209812.

Premièrement, pour pouvoir boucler à travers chaque chiffre du nombre, on convertit notre nombre entier en chaîne de caractère :

    str(nombre)

Ce qui nous permet ensuite, à l'aide d'une compréhension de liste, de boucler à travers chaque chiffre :

    [int(i) for i in str(nombre)]

Au passage, nous convertissons chaque chiffre en nombre avec la fonction int.
En effet, vu que nous avons converti notre nombre en chaîne de caractère, les éléments sur lesquels nous bouclons avec la boucle for sont des nombres en chaîne de caractère. Pour pouvoir les additionner 
ensemble il faut donc les convertir en integer.

Pour finir, on utilise la fonction sum, pour faire la somme de tous les nombres contenus dans la liste :

    somme = sum([int(i) for i in str(nombre)])

    POINTS IMPORTANTS À RETENIR

    Pour boucler sur chaque chiffre d'un nombre, on convertit le nombre en chaîne de caractère.
    Pour additionner ensemble tous les nombres contenus dans une liste, on utilise la fonction sum.
"""

print("\n Exercice48")
# # Exercice 48
# # Notion abordees: comprehension liste.
# # On continue avec l'utilisation des comprehensions de liste, cette fois-ci pour remplacer une chaine de caractere dans les elements
# # d'une liste par une autre chaine de caractere.
# # Votre script doit donc afficher la liste suivante:
# # ['Pierre','Marie','Julien','Adrien','Julien']
# #
# liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
# nom_a_chercher = "Julie"
# nouveau_nom = "Julien"

# liste = [name.replace(nom_a_chercher, nouveau_nom) if (name == nom_a_chercher) else (name)
#          for name in liste]
# print(liste)

"""
    SOLUTION

    liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
     
    nom_a_chercher = "Julie"
    nouveau_nom = "Julien"
     
    liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
    print(liste)

    EXPLICATION

On continue dans cet exercice avec les compréhensions de liste que vous devez commencer à maîtriser.

Encore une fois, on commence par boucler à travers chaque élément de la liste grâce à la compréhension de liste :

    liste = [x for x in liste]

En l'état, la compréhension de liste ci-dessus ne change absolument rien à la liste. Il faut donc utiliser la fonction replace pour remplacer le nom à chercher par le nouveau nom :

    liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]

Ainsi, directement en bouclant sur la liste, on remplace toutes les occurrences de 'Julie' par 'Julien'.

    POINTS IMPORTANTS À RETENIR

    Pour remplacer un mot par un autre, on utilise la fonction replace.
"""

print("\n Exercice49")
# # Exercice 49
# # Le but de cet exercice est d'enlever les doublons de la liste.
# # Pour reussir l'exercice, vous devez utiliser une autre methode que celle qui consiste à convertir la liste en set pour enlever les
# # doublons.
# # Votre script doit donc afficher la liste suivante:
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
# resultat = []
# for i in nombres:
#     if i not in resultat:
#         resultat.append(i)
# print(resultat)

"""
    SOLUTION

    nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
     
    nombres_sans_duplicats = []
     
    for i in nombres:
        if i not in nombres_sans_duplicats:
            nombres_sans_duplicats.append(i)
     
    print(nombres_sans_duplicats)

    EXPLICATION

Dans cet exercice, il fallait trouver une façon d'enlever les doublons d'une liste sans passer par les set.

Pour se faire, nous commençons par créer une liste vide, que nous allons remplir petit à petit par les nombres de la liste initiale.

À chaque itération de la boucle, nous vérifions avec une structure conditionnelle, que le nombre courant sur lequel on boucle  n'est pas déjà présent dans la liste avec la syntaxe if i not in liste  :

    for i in nombres:
        if i not in nombres_sans_duplicats:
            nombres_sans_duplicats.append(i)

Si le nombre n'est pas déjà présent dans la liste vide que nous avons initialisé, nous l'ajoutons alors à cette liste.

De cette façon, si on tombe une seconde fois sur le même nombre, la structure conditionnelle ne sera pas vérifiée et le nombre ne sera pas ajouté une deuxième fois dans la liste.

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si un élément est déjà présent ou non dans une liste, on utilise la syntaxe i in liste. Si le nombre est déjà dans la liste, cette syntaxe retournera True, si non, False.
"""

print("\n Exercice50")
# # Exercice 50
# # Printer un phrase autant de fois qu'un utilisateur le demande
# #
# res = 'o'
# compteur = 0
# while(res == 'o'):
#     print(f"Le compteur est maintenant à {compteur}")
#     compteur += 1
#     res = input("Voulez vous continuer ? o/n: ")

"""
    SOLUTION

    i = 0
    continuer = "o"
     
    while continuer == "o":
    	print(f"Le compteur est maintenant à {i}")
    	continuer = input("Voulez-vous continuer ? o/n ")
    	i += 1
"""

print("\n Exercice51")
# # Notions abordees: les dictionnaires, boucle for.
# # On s'attaque maintenant aux dictionnaires, toujours avec un peu de boucle for pour pimenter le tout.
# # Dans cet exercice, vous devez boucler à travers la liste et ajouter au dictionnaire 'employes' seulement
# # les elements de la liste qui sont des chaines de caractere.
# # Le but de l'exercice est de trier les donnees et de construire un dictionnaire d'employes.
# # Les cles du dictionnaires doivent etre 'id-xx', xx etant le numere de l'employe.
# # Votre script devra donc retourner le dictionnaire suivant:
# # {'id-01','Pierre','id-02','Marie','id-03','Adrien'}
# #
# employes = {}
# liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
# num = 1
# for element in liste:
#     if (isinstance(element, str)):
#         id = "id" + "-" + "0" + str(num)
#         employes[id] = element
#         num += 1
# print(employes)

"""
        SOLUTION

    employes = {}
     
    liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
     
    i = 1
     
    for element in liste:
        if not str(element).isdigit():
            employes["id-{:02d}".format(i)] = element
            i += 1
     
    print(employes)

    EXPLICATION

Pour cet exercice, nous avons du ruser un peu. Peut-être avez-vous commencé par utiliser la fonction enumerate pour récupérer directement l'indice et l'élément sur lequel on boucle ? Le problème est qu'ici, certains éléments ne sont pas valides et sont donc ignorés. Ainsi, pour garder un id d'employé continue, nous ne pouvons pas utiliser l'indice de l'élément sur lequel on boucle.

C'est la raison d'être de la variable i que nous initialisons à 1 avant de passer dans la boucle et que nous incrémentons chaque fois qu'un employé valide est détecté.

Pour détecter si un élément de la liste ne contient que des nombres, on utilise la fonction isdigit :

    if not str(element).isdigit():

Pour formatter la clé dans le dictionnaire, on utilise la fonction format :

    employes["id-{:02d}".format(i)] = element

La syntaxe :02d permet d'indiquer que nous souhaitons formater le nombre i pour qu'il contienne toujours 2 chiffres : 1 deviendra 01, 2 deviendra 02, 15 restera tel quel etc.

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si une chaîne de caractère ne contient que des nombres, on utilise la fonction isdigit.

    Pour formater un nombre pour qu'il contienne toujours 2 chiffres, on utilise la syntaxe 02d à l'intérieur d'accolades utilisées pour la fonction format.
"""

# print("\n Exercice52")
# # Notions abordees: les dictionnaires.
# # On continue les dictionnaires: dans cet exercice, vous devez creer un dictionnaire qui contient toutes les lettres de l'alphabet.
# # La cle de chaque element du dictionnaire doit contenir la position de la lettre dans l'alphabet, et la valeur doit etre egal à la
# # lettre en question. L'indice de la premiere letrre doit etre 1 et non 0 !
# # votre dicitionnaire doit donc etre comme ci-dessous:
# # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'} etc...
# # Aller plus loin: Essayer de faire tenir votre script en une seule ligne !
# alphabet = {}
# i = 1
# for letter in string.ascii_lowercase:
#     alphabet[i] = letter
#     i += 1
#
# print(alphabet)

"""     
    POINTS IMPORTANTS À RETENIR

    Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip.

    Pour créer un dictionnaire à partir d'une liste de tuple, on peut utiliser la fonction dict.    SOLUTION

    import string
     
    alphabet = string.ascii_lowercase
    indices = range(1, len(alphabet) + 1)
    liste_zip = zip(indices, alphabet)
    resultat = dict(liste_zip)
     
    print(resultat)

    EXPLICATION

Dans cet exercice, nous utilisons la fonction zip, pour construire un dictionnaire comprenant les lettres de l'alphabet et leur position dans l'alphabet.

Pour commencer, nous récupérons toutes les lettres de l'alphabet en minuscule, grâce au module string :

    >>> alphabet = string.ascii_lowercase
    >>> print(alphabet)
    'abcdefghijklmnopqrstuvwxyz'

Ensuite, on créé une liste qui contient les nombres de 1 à la longueur de l'alphabet, grâce à la fonction range et la fonction len :

    >>> indices = range(1, len(alphabet) + 1)
    >>> print(indices)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

On ajoute 1 à la longueur de l'alphabet car notre liste commence à 1 et non 0.

On utilise ensuite la fonction zip, qui permet de créer une liste de tuples à partir de deux listes (la liste de nombres et les lettres de l'alphabet) :

    >>> liste_zip = zip(indices, alphabet)
    >>> print(list(liste_zip))
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'),
     (11, 'k'), (12, 'l'), (13, 'm'), (14, 'n'), (15, 'o'), (16, 'p'), (17, 'q'), (18, 'r'), (19, 's'),
     (20, 't'), (21, 'u'), (22, 'v'), (23, 'w'), (24, 'x'), (25, 'y'), (26, 'z')

Il ne nous reste plus qu'à utiliser la fonction dict pour convertir cette liste de tuple en dictionnaire.
En effet, vous pouvez passer une liste contenant des tuples contenant deux éléments et la fonction dict va utiliser le premier élément comme clé et le deuxième élément comme valeur :

    >>> resultat = dict(liste_zip)
    >>> print(resultat)
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
     13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
     24: 'x', 25: 'y', 26: 'z'}

    POINTS IMPORTANTS À RETENIR

    Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip.

    Pour créer un dictionnaire à partir d'une liste de tuple, on peut utiliser la fonction dict.
"""

# print("\n Exercice 53")
#
#
# # Notons abordees: la boucle for, les fonctions.
# # Un exercice toujours tres interessant à faire en Python est d'essayer de recreer les fonctions de base.
# # Dans cet exercice, nous allons recreer la fonction len() qui permet de compter la longueur d'une variable.
# # Dans cet exemple, nous voulons compter le nombre de lettres dans le mot 'bonjour'/
# # votre script doit donc retourner le nombre 7.
#
#
# def longueur(variable):
#     compteur = 0
#     for i in variable:
#         compteur += 1
#     return compteur
#
#
# print(longueur("bonjour"))

"""
        SOLUTION

    def longueur(variable):
        compte = 0
        for i in variable:
            compte += 1
        return compte
     
    print(longueur("bonjour"))

    EXPLICATION

Dans cette série d'exercices, nous attaquons un sujet intéressant qui consiste à recréer les fonctions de base qui viennent avec Python.

Ici, la fonction len, qui permet de calculer la longueur de différents types de variables : le nombre de caractère dans une chaîne de caractère, le nombre d'éléments dans une liste etc.

Il apparaît donc rapidement que nous allons devoir boucler à travers les différents éléments qui composent la variable qui est passée à notre fonction 'longueur'. Pour ce faire, on utilise donc logiquement une boucle for.

Puis, afin de compter le nombre d'éléments, on utilise tout simplement une variable 'compte' qu'on incrémente à chaque itération de la boucle :

    compte = 0
    for i in variable:
        compte += 1

 Il ne reste plus qu'à retourner le résultat contenu dans la variable :

    return compte

Et voilà, le tour est joué ! Une fonction très importante que l'on utilise quotidiennement en Python et qu'il est assez simple à recréer en fin de compte.

    POINTS IMPORTANTS À RETENIR

    Pour boucler à travers les différents éléments de plusieurs types de variables, on peut utiliser une boucle for.
    Pour incrémenter facilement un nombre entier, on peut utiliser la syntaxe +=
"""

# print("\n Exercice 54")
# # Notions abordees: La fonction print, la fonction range, la boucle for.
# # Dans cet exercice, vous allez devoir afficher une moitie de losange composee du symbole '*' grace à une boucle for
# # et la fonction print
# # votre scipt doit afficher le motif suivant:
# # *
# # **
# # ***
# # ****
# # *****
# # ******
# # *******
# # ********
# # *******
# # ******
# # *****
# # ****
# # ***
# # **
# # *
# n = 8
# symbole = '*'
# for i in range(0, n):
#     resultat = (symbole) * i
#     print(resultat)
#
# for i in range(n, 0, -1):
#     resultat = (symbole) * i
#     print(resultat)

"""
SOLUTION

    n = 8
    symbole = "*"
    nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
    for i in nombres:
        print(symbole*i)

EXPLICATION

Beaucoup de nombres dans tous les sens avec cet exercice mais au final vous allez voir que c'est assez simple.

Le but de cet exercice était d'afficher une moitié de losange :

    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *

Nous avons donc besoin d'afficher le symbole contenu dans la variable 'symbole' 1 fois, puis 2, puis 3 etc, jusqu'à la valeur du nombre contenu dans la variable n. Il va donc falloir dans un premier temps 
incrémenter le nombre de fois que l'on affiche le symbole, puis dans un deuxième temps, décrémenter cette variable pour revenir à 1.

L'objectif est donc de créer une première liste allant de 1 jusqu'au nombre n :

    >>> n = 8
    >>> liste = range(1, n+1)
    >>> print(liste)
    [1, 2, 3, 4, 5, 6, 7, 8]

La deuxième valeur indiquée dans la fonction range est n+1 car la fonction range est exclusive. Il faut donc indiquer 9 (n+1) si l'on veut avoir le nombre 8 dans la liste. La première valeur que nous indiquons à 
la fonction range est 1 puisque nous voulons commencer la liste à partir du nombre 1.

Deuxièmement, il nous faut une liste qui cette fois-ci, commence à 7 (n-1, puisque le nombre 8 est déjà dans la première liste, nous n'en n'avons pas besoin une seconde fois). La liste doit se rendre jusqu'à 1 et 
décrémenter à chaque fois.
Pour cela, nous passons le nombre -1 en troisième paramètre à la fonction range, afin d'avoir une liste décrémenté.
On part donc de 7 (8-1), pour aller jusqu'à 1 (on indique donc 0 en deuxième paramètre à la fonction range car là encore, cette fonction est exclusive).

    >>> n = 8
    >>> liste = range(n-1, 0, -1)
    >>> print(liste)
    [7, 6, 5, 4, 3, 2, 1]

Nous additionnons ensuite ces deux listes ensemble, en prenant le soin de les convertir en liste car nous ne pouvons pas ajouter deux objets range l'un avec l'autre :

    >>> nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
    >>> print(nombres)
    [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]

Nous avons donc maintenant la liste qui va nous permettre d'afficher le bon nombre de symboles à chaque itération. Il ne reste donc plus qu'à boucler dans cet liste et afficher le symbole multiplié par le nombre à chaque itération de la boucle :

    for i in nombres:
        print(symbole*i)

On va donc printer le symbole 1 fois, puis 2, puis 3... jusqu'à 8, et ensuite redescendre à 7, 6, 5... jusqu'à 1.

POINTS IMPORTANTS À RETENIR

    Pour créer une liste avec la fonction range en sens inverse, on peut passer un troisième paramètre : -1
"""

# print("\n Exercice 55")
# # Notions abordees: les boucles, les chaines de caractere.
# # Dans cet exercice, nous aloons, à partir d'une variable 'symbole' et un variable 'taille'
# # creer un pyramdide avec ce symbole, de la hauteur du nombre contenu dans la variable 'taille'.
# # Dans cet exemple-ci, nous allons donc afficher une pyramide de dollar ($) de hauteur 10.
# # votre script devra donc afficher:
# #         $
# #        $ $
# #       $ $ $
# #      $ $ $ $
# #     $ $ $ $ $
# #    $ $ $ $ $ $
# #   $ $ $ $ $ $ $
# #  $ $ $ $ $ $ $ $
# # $ $ $ $ $ $ $ $ $
#
# symbole = "$"
# taille = 10
# for i in range(1, taille + 1):
#     print(" " * (((11) - i) - 1) + (symbole + " ") * i)

"""
    SOLUTION

    symbole = "$"
     
    taille = 10
     
    for i in range(1, taille + 1):
        espaces = " " * (taille - i)
        print(espaces + (symbole + " ") * i)

    EXPLICATION

On continue avec un exercice d'affichage, grâce à la fonction print.

Le but de cet exercice était d'afficher une pyramide de dollars !

Nous commençons donc par définir le symbole utilisé et la taille de la pyramide dans deux variables, respectivement 'symbole' et 'taille'.

Nous entamons ensuite une boucle for qui boucle sur une liste de nombres de la taille de notre variable 'taille' (on commence à 1 parce que notre première ligne contient un symbole. Si on commençait à 0 on aurait une première ligne vide).

Nous déclarons ensuite à l'intérieur de la boucle une variable 'espaces' qui contient un caractère espace, multiplié par la taille de la liste moins la valeur contenue dans l'itération actuelle de la boucle (la variable i).
À la première itération nous aurons donc une variable espaces qui contiendra 9 espaces (10 - 1), puis 8 (10 - 2), puis 7 (10 - 3) etc.

Cela permettra de décaler notre symbole pour que le premier dollars soit au milieu de la pyramide, puis chaque symbole suivant se retrouvera de plus en plus proche de la marge.

Nous faisons donc ensuite un print de cette variable espaces, à laquelle nous ajoutons le symbole plus un espace, multiplié par le nombre de l'itération actuel (la variable i).
Pourquoi ajouter un espace au symbole et multiplier le tout par i ? Parce que si on n'ajoute pas d'espace au symbole, on se retrouve avec une pyramide un peu bizarre :

             $
            $$
           $$$
          $$$$
         $$$$$
        $$$$$$
       $$$$$$$
      $$$$$$$$
     $$$$$$$$$
    $$$$$$$$$$

Pour que chaque symbole soit bien aligné pour constituer une pyramide, il faut qu'il y ait un espace entre chaque symbole $.

    POINTS IMPORTANTS À RETENIR

    Pour afficher plusieurs fois de suite un caractère, on peut tout simplement multiplier une chaîne de caractère par un nombre.
"""

# print("\n Exercice 56")
# # Notions abordees: la fonction format.
# # Dans cet exercice, nous continuons d'aborder le formatage de texte, cette fois-ci avec la fonction format.
# # le but de cet exercice est d'afficher le texte suivant:
# -------------
# |    B      |
# |    o      |
# |    n      |
# |    j      |
# |    o      |
# |    u      |
# |    r      |
# |           |
# |    J      |
# |    u      |
# |    l      |
# |    i      |
# |    e      |
# |    n      |
# -------------

# texte = "Bonjour Julien"
# longueur = len(texte)
# symbole1 = "-"
# symbole2 = "|"
#
# print(symbole1 * longueur)
# for lettre in texte:
#     print(f"{symbole2}{lettre:^{longueur - 2}}{symbole2}")
# print(symbole1 * longueur)
"""
    SOLUTION

    texte = "Bonjour Udemy"
    longueur = len(texte)

    symbole1 = "-"
    symbole2 = "|"

    print(symbole1*longueur)

    for lettre in texte:
        print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))

    print(symbole1*longueur)

    EXPLICATION

Beaucoup de lignes de codes qui ne font pas forcément de sens à prime abord dans cet exercice, nous allons donc pas à pas expliquer la logique derrière cette solution.

Tout d'abord, nous déclarons un certain nombre de variables : le texte à afficher, la longueur du texte (dans la variable 'longueur') et les deux symboles que nous allons utiliser ('symbole1' et 'symbole2').

Nous commençons ensuite par afficher le premier symbole, multiplié par la longueur de la chaîne de caractère :

    >>> print(symbole1*longueur)
    -------------

Nous passons ensuite avec une boucle for à travers chaque lettre du mot :

    for lettre in texte:

Vient ensuite, la partie un peu plus complexe de l'exercice. Nous utilisons toute la puissance que nous permet la méthode format avec la syntaxe suivante :

    print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))

Tout d'abord, nous définissons deux balises au début et à la fin de la chaîne de caractère, représentées par les accolades entourant le 0 : {0}

Cela nous permet d'afficher la symbole 2 au début et à la fin.


Puis, nous utilisons la syntaxe suivante :

    {1:^{2}}

Le 1 signifie que l'on insère à l'intérieur de cette accolade le 2e argument passé à la méthode format (la variable 'lettre', donc chaque lettre de notre variable texte, récupérée grâce à la boucle for).

La deuxième partie, avec les deux points et l'accent circonflexe, signifie que l'on veut ajouter un 'padding' avant et après cette lettre : en gros, python va ajouter autant d'espaces que nécessaire avant et après la variable que l'on insère dans l'accolade, afin que le nombre total de caractère soit égal au nombre passé.
Ce nombre, on lui passe grâce à l'accolade qui contient le 2, signifiant que l'on va passer ce nombre comme 3e argument à la méthode format. On passe comme nombre 'longueur - 2', donc la longueur du texte, minus les 2 symboles que l'on place au début et à la fin de la chaîne de caractère (rappelez-vous, les accolades avec le 0) :

    >>> print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))
    |     B     |

Ainsi, on s'assure que la longueur totale de la ligne, soit égale à la longueur de la première ligne.

Puis on termine notre script par le même print que pour afficher la première ligne, afin de refermer notre boîte :

    print(symbole1*longueur)

    POINTS IMPORTANTS À RETENIR

    Vous pouvez afficher plusieurs fois le même élément dans une chaîne de caractère avec la méthode format, en utilisant plusieurs fois le même indice à l'intérieur des accolades.
    Pour faire en sorte qu'une chaîne de caractère occupe un nombre précis de caractère, vous pouvez la 'padder' avec des espaces, en utilisant l'accent circonflexe à l'intérieur de votre chaîne de caractère et la méthode format.
"""

# print("\n Exercice 57")
# # Notions abordees: la boucle for, les fonctions, les structures conditionnelles.
# # Dans cet exercice, nous voulons formater un nombre pour ajouter une virgule entre chaque millier.
# # Ansi, le nombre contenu dans la variable 'nombre' devra etre comme ci-dessous:
# # 52,039,480,394,023
# # Votre script doit bien entendue fonctionner peu importe le nombre
# nombre = []
# resultat = ''
# while len(nombre) < 4:
#     nombre = ['5', '2', '0', '3', '9', '4', '8', '0', '3', '9', '4', '0', '2', '3']
#
#     if (len(nombre) < 4):
#         print("Votre nombre est < 1000 !\n")
#     else:
#         i = 0
#     nombre.reverse()
#
#     while i < len(nombre):
#         if (int(i) % 3 == 0) and (i != 0):
#             resultat = resultat + ','
#         resultat += nombre[i]
#         i += 1
#
# print(resultat[::-1])
#
#
# # correction
# def ajout_separateur(nombre):
#     nombre = str(nombre)[::-1]
#     resultat = ""
#
#     for i, chiffre in enumerate(nombre, 1):
#         print(i, chiffre)
#         chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre
#         resultat += chiffre_formatte
#
#     return resultat[::-1]
#
#
# nombre = 52039480394023
# print(ajout_separateur(nombre))
#
#
# print("\n Exercice 58")
# # Dans cet exercice, nous allons utiliser le module datetime pour calculer l'annee de naissance de quelqu'un
# # à partir de son age. Dans cet exemple, nous allons prendre un age de 25 ans.
# # Afin de ne pas fausser les resultats, nous allons egalement indiquer le mois de naissance afin de verifier si
# # la date d'anniversaire de la personne est passee ou non.
# # Nous avons donc deux variables:
# # 1 - La variable 'age' qui contient l'age de la personne (ici: 25).
# # 2 - Le mois de naissance, contenu dans la variable 'mois_de_naissance' (ici, le mois d'octobre, soit 10).
# # A partir de ces deux infos, il faut calculer l'annee à laquelle est nee la personne.
# # Dansce cas-ci. l'annee que vous devez afficher est '1994'
# from datetime import date
#
# age = 25
# mois_de_naissance = 10
#
#
# def date_of_birth(age, month):
#     current_year = date.today().year
#     current_month = date.today().month
#     birth_year = current_year - age
#     if month > current_month:
#         birth_year += 1
#     return birth_year
#
#
# print(date_of_birth(25, 10))

# print("Exercice 59")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366036#overview
"""
059 - Calculer la somme des nombres entre deux nombres

Notions abordees: la fonction sum, la fonction range.
Dans cet exercice, nous allons calculer la somme des nombres entre deux nombres.
Dans cet exemple-ci, nous prenons les nombres 2 et 6, le resultat de votre script doit donc etre 20 (2 +3 + 4 + 5 + 6)
Attention: votre script doit fonctiooner peu importe l'ordre dans lequel vous donnez les nombres : somme(2, 6) et
somme(6, 2) doivent retourner le meme resultat !
Astuces: Afin de faire fonctionner le script peu importe l'ordre des variables a et b, pensez à utiliser les fonctions
min et max.
"""

# def somme(a, b):
#     total = 0
#     for i in range(min(a, b), max(a, b) + 1):
#         total += i
#     return (total)
#
#
# print(somme(2, 6))
#
#
# # correction
# def somme(a, b):
#     return sum(range(min(a, b), max(a, b) + 1))
#
#
# print(somme(2, 6))
#
#
# print("Exercice 60")
# from math import floor
# import string
#
# # Separer la liste ci-dessous en 2 par rapport au milieu de l'alphabet.
# employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoe"]
#
# alphabet = string.ascii_lowercase
# milieu = int(len(alphabet) / 2)
# print(milieu)
#
# alphabet_01, alphabet_02 = alphabet[:milieu], alphabet[milieu:]
# employes_a_m = []
# employes_n_z = []
# for employe in employes:
#     premiere_lettre = employe[0].lower()
#     if premiere_lettre in alphabet_01:
#         employes_a_m.append(employe)
#     elif premiere_lettre in alphabet_02:
#         employes_n_z.append(employe)
#
# print("Employes de A à M:", ", ".join(sorted(employes_a_m)))
# print("Employes de N à Z:", ", ".join(sorted(employes_n_z)))
#
# # Optimal solution
# employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoe"]
# alphabet = string.ascii_lowercase
# employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
# employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]
#
# print("Employes de A à M:", ", ".join(sorted(employes_a_m)))
# print("Employes de N à Z:", ", ".join(sorted(employes_n_z)))
#
#

print("Exercice 61")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366038#overview
"""
061 - Créer une fonction pour remonter dans une structure de dossiers
Notions abordees: le module os, la boucle while, les fonctions.
Dans cet exercice, nous abordons le module os !
Le but de cet exercice est de creer une fonction, qui permette de remonter dans une structure de dossier autant de
fois qu'indique.
Par exemple avec le dossier suivant: /Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy
Nous allons indiquer à la fonction 'remonter_dossier' le nombre de dossier que l'on veut remonter, par exemple:
remonter_dossier("/Users/Thibh/Desktop/Dossier_01/Udemy, 3)
Notre fonction va donc remonter dans la structure de dossier 3 fois et nous retourner le chemin suivant:
/Users/Thibh/Desktop
Astuces: Pour recuperer le dossier parent d'un dossier, on utilise la fonction os.path.dirname() du module OS.
"""
# import os
#
# dossier = "/Users/Thibn/Desktop/Dossier_01/Tutoriel/Udemy"
#
#
# def remonter_dossier(dossier, iterations=1):
#     i = 0
#     while i < iterations:
#         dossier = os.path.dirname(dossier)
#         i += 1
#     return dossier
#
#
# print(remonter_dossier(dossier, 3))


# print("Exercice 62")
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11318094#overview
"""
chemin = "/Users/Thibn/Desktop/Dossier_01/../../Dossier02/Udemy"


la fonction os.path.normpath(chemin) permet de transformer le chemin relatif en chemin absolu.
Faire de meme sans utiliser cette fonction
"""

# def normalize_path(chemin):
#     result = []
#     nouveau_chemin = chemin.split("/")
#     for element in nouveau_chemin:
#         if element == '..':
#             del result[-1]
#         else:
#             result.append(element)
#     return os.sep.join(result)
#
#
# print(normalize_path(chemin))
#
#
# # Autre solution possible
# def normalize_path(chemin):
#     chemin_parts = chemin.split("/")
#     while ".." in chemin_parts:
#         index = chemin_parts.index("..")
#         chemin_parts.pop(index)
#         chemin_parts.pop(index - 1)
#
#     return os.sep.join(chemin_parts)
# print(normalize_path(chemin))
#
#
# print("Exercice 63")
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11318608#overview
# dossier = os.path.dirname(__file__)
# dossier = os.path.join(dossier, 'data')
# fichier = os.path.join(dossier, 'Fichier.txt')
#
# try:
#     os.makedirs(dossier, exist_ok=True)
#     print("Directory '%s' created successfully" %dossier)
# except OSError as error:
#     print("Directory '%s' can not be created")
#
# with open(fichier, 'w') as f:
#     f.write("Ceci est mon texte !")
#
#
# print("Exercice 64")
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11318478#overview
# import os
# import distutils
#
# cur_dir = os.path.realpath(os.path.dirname(__file__))
# fichier = os.path.join(cur_dir, "variable.txt")
#
# with open(fichier, "r") as f:
#     variable = f.read()
#
# vraie_variable = bool(distutils.util.strobool(variable))
# if vraie_variable:
#     print("La variable est un boolean True")


print("\n Exercice65")
# """
# Notions abordees: Les boucles, les operateurs mathematiques.
# Dans cet exercice, nous cherchons tous les diviseurs d'un nombre, dans ce cas-ci, le nombre 50.
# Les diviseurs du nombre 50 correspondant à tous les nombres par lesquels on peut diviser 50 sans qu'il n'y ait de reste
# à la division.
# Par exemple, 25 est un diviseur de 50 (car 50 / 25 = 2, et il reste 0.)
# Astuces: Pour trouver le rest d'une division avec Python, on utilise l'operateur modulo(%)
# """
#
# nombre = 1
# diviseur = []
# while 51 - nombre > 0:
#     if 50 % nombre == 0:
#         diviseur.append(nombre)
#     nombre += 1
#
# print(diviseur)


print("\n Exercie66")
# """
# Notions abordees: Les boucles, les operateurs mathemeatiques, les structures conditionnelles
# Le but de cet exercice est de trouver tous les nombres de 0 à 1000 qui sont divisibles par 7 mais ne sont pas des multiples
# de 3. Par exemple, le nombre 14 est divisible par 7 (car 14/7=2, il reste 0), mais n'est pas un multiple de 3 (car 14/3
# ne retourne pas un nombre entier).
# Pour valider l'exercice, vous devez récupérer tous ces nombres dans la liste nombres.
# """
# nombres = []
# for i in range(1, 1001):
#     if (i % 7 == 0) and i % 3 != 0:
#         nombres.append(i)
# print(nombres)


print("\n Exercice67")
# """
# Notions abordées: les boucles.
# Dans cette exercice, nous cherchons la factorielle d'un nombre, dans ce cas-ci le nombre 5.
# La factorielle de 5 est egale à 120 (car 1 x 2 x 3 x 4 x 5 = 120)
# Votre script doit aussi gérer le cas dans lequel le nombre de départ est 0 (la factorielle de 0 est égale à 1).
# Astuces: Pour calculer la factorielle d'un nombre, vous pouvez utiliser une boucle for associée à la fonction range.
# """
#
# nombre_saisie = int(input("entrer un nombre:"))
# print(f"Le nombre saisie est {nombre_saisie}")
# result = 1
# for i in range(1, nombre_saisie+1):
#     result *= i
#
# print(result)

print("\n Exercice68")
# """
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11331692#overview
# """
# dossier = r"C:\Users\MOTTIER LUCIE\Documents\testglob"
# fichier_a_trouver = "fichier_a_trouver.txt"
#
# # fichiers = glob(dossier + "/**", recursive=True)
# # fichiers_trouves = [f for f in fichiers if os.path.split(f)[1] == fichier_a_trouver]
# # print(fichier_a_trouver)
#
# for fichier in glob(dossier + './**/', recursive=True):
#     print(fichier)


print("\n Exercice69")
# """
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11365358#overview
# """
# nbsec = int(input("Entrez un temps de rafraichissement:"))
# dossier_a_chercher = "Python"
# dossier = os.path.join(r"C:\Users\MOTTIER LUCIE\Documents", dossier_a_chercher)
#
#
# while True:
#     if os.path.exists(dossier):
#         print("fichier Trouve!")
#         exit(0)
#     else:
#         print("Dossier introuvable...")
#     time.sleep(nbsec)
#
# # Autre possibilite:
# dossier = r"C:\Users\MOTTIER LUCIE\Documents"
# dossier_a_chercher = "Python"
#
# nbsec = input("Entrez un temps de rafraichissement:")
# while dossier_a_chercher not in os.listdir(dossier):
#     print("Dossier introuvable...")
#     time.sleep(int(nbsec))
# print("Trouve")


print("\n Exercice70")
# """
# ennonce: https://www.udemy.com/course/python-exercices/learn/lecture/11365358#overview
# """
# dossier = r"C:\Users\MOTTIER LUCIE\Documents"
# fichiers = glob(f"{dossier}/**", recursive=True)
#
# print(f"Il y a {len(fichiers)} fichiers et repertoires dans le repertoire {dossier}")

print("\n Exercice71")
# """
# + Notions abordées: Les modules, les boucles.
# Dans cet exercice, nous allons générer un octet aléatoire.
# Un octet est représenté par un suite de 8 chiffires allant de 0 à 1, par exemple: 01101110 qui est égal au nombre 110
# en base décimale.
# + Aller plus loin: Utilisez une comprehension de liste pour réduire le nombre de lignes dans votre code.
# + Astuce: Pour générer des nombres aléatoires en Python, on utilise le module random.
# """
# i = 0
# resultat = ""
# for i in range(0, 8):
#     resultat = resultat + str(random.choice(range(0, 2)))
# print(resultat)
#
# resultat=""
# resultat = [str(random.choice(range(2))) for _ in range(8)]
# print("".join(resultat))

print("\n Exercice72")
"""
+ Notions abordées: le module datetime
Dans cette exercice, nous allons calculer le nombre de jours entre deux dates.
La date de départ que nous allons utiliser est le 2 juillet 2014 et la date de fin le 11 juillet 2018.
Le nombre de jours entre ces deux dates est 1470.
A vous de trouver le code qui permet de calculer automatiquement le nombre de jours entre ces deux dates, grace au 
module datetime.
+ Astuces: Pour créer un objet date, on utilise la classe 'date' du module 'datetime'. 
"""
# date1 = date(2014, 7, 2)
# date2 = date(2018, 7, 11)
# print((date2 - date1).days)

print("\n Exercice73")
"""
+ Notions abordées: le module string, le module random.
Dans cet exercice, nous allons créer un générateur de mot de passe aléatoire.
A l'aide du module string et du module random, vous allez générer un mot de passe aléatoire de la longueur spécifiée
dans la variable 'taille (ici, 8).

Votre mot de passe doit pouvoir contenir des lettres minuscules, n'importe quel chiffre de 0 à 9 et n'importe
quel caractère spécial(!#$%& etc...)
+ Astuces: Le module string vous permet de récupérer des suites de lettres, de nombres de carctères spéciaux.
"""
# resultat, i, taille = "", 0, 8
# while i < taille:
#     resultat += random.choice(string.ascii_letters + string.digits + string.punctuation)
#     i += 1
#
# print(resultat)
#
# # correction
# # La premiere chose à faire est de récupérer toutes les lettres de l'alphabet, les nombres et tous les symboles:
# symboles = string.ascii_letters + string.digits + string.punctuation
# # On utilise ensuite le module random et la fonction choice. Cette fonction va nous permettre de sélectionner une
# # lettre aléatoire parmi la chaine de carctère "symoble" que nous avons déclaré plus haut.
# # Pour répéter l'opération autant de fois que nécessaire, on utilise une boucle et une compréhension de liste:
# mot_de_passe = ''.join(random.choice(symboles) for i in range(taille))
# print(mot_de_passe)

# POINTS IMPORTANTS A RETENIR
# 1 - Pour récupérer toutes les lettres majuscules et minuscules de l'alphabet, on utilise la constante "ascii_letters"
# du module "string".
# 2 - Pour récupérer tous les nombres, on utilise la constante dighits du module string.
# 3 - Pour récupérer tous les symboles du clavier, on utilise la constante "punctuation" du module "string"
# 4 - Pour récupérer une lettre aléatoire dans une chaine de caractère, on utilise la fonction "choice" du
# module "random"

print("\n Exercice74")
# """
# ennoncé: https://www.udemy.com/course/python-exercices/learn/lecture/11372370#overview
# """
# taille = 8
# symboles = string.ascii_letters + string.digits + string.punctuation
# mot_de_passe = ''.join(random.choice(symboles) for i in range(taille))
# print(mot_de_passe)
#
#
# count_numbers = 0
# count_capital = 0
# count_letters = 0
# for letter in mot_de_passe:
#     if letter in string.ascii_letters and letter.isupper():
#         count_capital += 1
#     elif letter in string.digits:
#         count_numbers += 1
#     count_letters += 1
#
# if count_numbers >= 2 and count_capital >= 1 and count_letters >= 8:
#     print("le mot de passe est valide")
# else:
#     print("le mot de passe est invalide")
#     print(f"DEBUG: {count_numbers}, {count_capital}, {count_letters}")
#
# correction (more pythonic code than above)
# def verificateur_mdp(mdp):
#     if len(mdp) >= 8 and any(i.isupper() for i in mdp) and len([n for n in mdp if n.isdigit()]) >= 2:
#         return True
#     return False
#
#
# succes = verificateur_mdp(mot_de_passe)
# print(succes)

print("\n Exercice75")
"""
+ Notions abordées: les chaines de caractères.
Dans cet exercice, nous allons compter le nombre d'occurence du mot 'elit' dans le texte en Lorem Ipsum contenu
dans la variable 'lorem'.
Dans cet extrait de texte, le mot apparait une seule fois, voitre script doit donc retourner 1.
+ Astuces: Afin de compter le nombre de mots, vous devz d'abord vous débarasser des carctères spéciaux gênant comme
les virgules et lses points.
"""
# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et\
#  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea \
#  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\
#   pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est\
#    laborum."
# mot = "elit"
# lorem = lorem.replace(',', '').replace('.', '')
# lorem = lorem.lower()
# lorem_split = lorem.split()
# print(lorem_split.count(mot))

print("\n Exercice76")
# """
# + Notions abordées: les boucles, les chaines de caractères.
# On Continue avec les chaines de carctère dans cet exercice dans lequel vous devez convertir une phrase en un mot au
# format camelCase.
# Le camelCase est un facon de formater une suite de mot pour chaque que mot soit séparé par un majuscule, excepté le
# premier mot.
# Dans ce cas-ci, votre script doit donc convertir la 'Phrase en camel case' en 'praseEnCamelCase'.
# + Astuces: Afin de s'assurer qu'un mot commence par une majuscule, vous pouvez utiliser la fonction capitalize sur une
# chaine de caractère
# """
# phrase = "Phrase en camel case"
# nouvellePrase = phrase.split()
# resultat=""
# resultat += "".join([word.capitalize() for word in nouvellePrase])
# resultat = resultat.replace("P", "p")
# print(resultat)

print("\n Exercice77")
"""
+ Notions abordées: les chaines de caractère, les boucles.
On reprend un exercice que nous avons effectué plus tot dans la formation mais cette fois ci avec une phrase.
Il est question ici d'inverser l'ordre des mots dans la phrase. Votre phrase devra, comme une phrase normalement 
construite, commencer par une majuscule.
Nous avons ici la phrase 'Bonjour tout le monde', votre script devra donc retourner la phrase 'Monde le tout bonjour'.
+ Astuces: Pour inverser une liste, vous pouvez utiliser la vonction reversed.
"""
# phrase = "Bonjour tout le monde"
# print(" ".join(list(reversed(phrase.split()))).capitalize())

print("\n Exercice78")
"""
+ Notions abordées: Les chaines de caractère.
Dans cet exercice, nous allons vérifier si une phrase est un palindrome ou non. Un palindrome est un mot ou une phrase
qui peut se lire de la meme facons dans les deux sens.
Dans cet exemple-ci, nous avons le palindrome 'Un roc cornu'. Votre script devra donc vérifer si cette phrase est
un palindrome, et donc dans ce cas-ci, retourner la valeur 'True'
+ Aller plus loin: Essayez cette fois ci de ne pas utliser la fonction reversed.
"""

# phrase = "Un roc cornu"
# phrase = phrase.replace(" ", "")
# phrase1 = phrase[:5]
# phrase2 = ""
#
# # ma premiere solution
# for i in range(1, 6):
#     phrase2 += phrase[-i]
#
# if phrase1.lower() == phrase2.lower():
#     print(True)
#
# # Autre solution possible
# mot = "Un roc cornu"
# mot_lower = mot.lower().replace(" ", "")
# if mot_lower == mot_lower[::-1]:
#     print(True)
# else:
#     print(False)
#
# chaine = "Pierre, Julien, Anne, Marie, Lucien"
# chaine_en_ordre = chaine.split(", ")
# chaine_en_ordre.sort()
# chaine_en_ordre = ", ".join(chaine_en_ordre)
# print(chaine_en_ordre)

"""
+ EXPLICATIONS
Tout d'abord, il faut séparer les différents prénoms de la chaîne de caractère pour les mettres dans une liste.
En effet, on ne peut pas trier une chaîne de caractère, il va donc fallor passser par une liste.
Pour séparer les différents prénoms, on utilise la fonction split, qui permet de séparer la chaîne de caractère
en plusieurs éléments, en opérant la séparation sur la virgule.
Vous noterez qu'on a ajouté un espace après la virgule pour ne pas récupérer l'espace dans les prénoms de notre liste
A ce stade-ci, nous avons donc la liste suivante:
['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien']
Il faut maintenant ordonner cette liste, ce que nous faisons à la ligne suivante avec la fonction sort.
chaine_en_ordre.sort()
Il ne reste plus qu'à joindre de nouveaux les prénoms de la liste avec le carctère que nous avons utilisé précédemment
pour réaliser la séparation (une virgule suivie d'un espace).
Pour cela, nous utilisons la méthode join.
chaine_en_ordre = ", ".join(chaine_en_ordre)
+ POINTS IMPORTANTS A RETENIR
- On ne peut pas trier une chaîne de caractère.
- Pour séparer une chaîne de cactère en plusieurs éléments, on utilisera la fonction split.
- Pour trier une liste, on utilise la fonction sort
- Pour joindre différents éléments d'une liste par une chaîne de caractère, on utilise la méthode join.

"""

print("\n Exercice79")
"""
+ Notions abordées: les chaines de caractères, les boucles.
Encore un exercice avec un mot que vous n'avez peut-être jamais entendu de votre vie. Un pangramme est une phrase qui 
contient toutes les lettres de l'alphabet au moins une fois.
La phrase que nous utiliserons dans cette exercice est la suivante: "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary
skie dans l'ombre". Vous devez donc vérifier si cette phrase est bien un pangramme, et si c'est le case, afficher la phrase
"La phrase est un Pangramme."
"""
# import string
#
# count = 0
# lettre_deja_utilise = []
# phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l'ombre"
#
# for letter in phrase:
#     if letter in string.ascii_letters and letter not in lettre_deja_utilise:
#         lettre_deja_utilise.append(letter)
#         count += 1
#
# if count == 26:
#     print("La phrase est un Pangramme")
#
#     # Autre solution
#     import string
#
#     phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
#     phrase_lower = phrase.lower()
#
#     alphabet = list(string.ascii_lowercase)
#
#     for l in phrase_lower:
#         if l in alphabet:
#             alphabet.remove(l)
#
#     if alphabet:
#         print("La phrase n'est pas un Pangramme")
#     else:
#         print("La phrase est un Pangramme")
"""
Nous commencons par convertir la phrase en minuscule avec la méthode lower.
Nous récupérons grâce au module string toutes les lettres de l'alphabet que nous mettons dans une liste avec la
fonction list:
alphabet = list(string.ascii_lowercase)
la logique ensuite est de passer à travers chque lettre de notre phrase avec une boucle for...
for l in phrase_lower:
... pour vérifier si la lettre courrante est contenue dans notre liste "alphabet"...
if in alphabet:

...et si c'est le cas, nous enlevons cette lettre de notre liste "alphabet":
alphabet.remove(l)
Il ne nous reste plus à la fin qu'à vérifier si notre liste alphabet est vide ou non. Si la liste est vide, c'est donc
que notre phrase contenait toutes les lettres de l'alphabet. Si il reste au moins une lettre dans la liste, alors la 
phrase n'est pas vide donc n'est pas un pangramme.

Pour vérifier si une liste est vide, pas besoin de s'embêter avec la fonction len: une liste vide est évaluée comme
False, on peut donc vérifier facilement avec une structure conditionelle si la liste est vide ou non:
if alphabet:
  print("La phrase n'est pas un Pangramme")
else:
  print("La phrase est un Pangramme")
  
+ Points importants à retenir
1. pour récupérer toutes les lettres de l'alphabet, on utilise le module string et la constante "asci_lowercase".
2. pour enlever un élément d'une liste, on utilise la methode remove.
3. Une liste vide est évalée comme False.
"""

print("\n Exercice80")
"""
ennoncé: https://www.udemy.com/course/python-exercices/learn/lecture/11372420#overview
"""
# code = "print(any(('py' or 'txt') in ext for ext in ['.py'. '.obj', '.json']))"
# ouvrant = code.count("(")
# fermant = code.count(")")
# if ouvrant == fermant:
#     print("ok")
# elif ouvrant > fermant:
#     print(f"il y a {ouvrant} parenthese ouvrante et {fermant} parenthese fermante")
# else:
#     print(f"il y a {ouvrant} parenthese ouvrante et {fermant} parenthese fermante")
#
# # Autre solution
# print(code.count("(") == code.count(")"))

print("\n Exercice81")
"""
+ Notions abordées: les chaines de caractères.
Dans cet exercice, le but est de compter le nombre de phrase présentes dans le texte contenu dans la variable
'lorem'. Ce texte contient 4 phrases, votre script devra retourner le nombre 4.
"""
# lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# 		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# 		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# 		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
#
# print(lorem.count("."))

print("\n Exercice82")
"""
+ Notions abordées: les boucles, les dictionnaires.
Dans cet exercice, nous chercons à anylyser un texte pour savoir combien de fois on y retrouve chaque lettre de 
l'alphabet.
Nous avons donc un texte classique de Lorem Ipsum et votre script doit retourner un dictionnaire avec chaque lettre
de l'alphabet et le nombre de fois qu'elle apparait dans le texte.
Dans l'exemple ci-dessous, votre script devra retourner le dictionnaire suivant:
{'a': 29, 'b': 3, 'c': 16, 'd': 19, 'e': 38, 'f':3, 'g': 3, 'h': 1, 'i': 42, 'j': 0, 'k': 0, 'l': 22, 'm': 17, 'n': 24,
'o': 29, 'p': 11, 'q': 5, 'r': 22, 's': 18, 't': 32, 'u': 29, 'v': 3, 'w': 0, 'x': 3, 'y': 0, 'z': 0}
+ Astuces: Pour récupérer toutes les lettres de l'alphabet, vous pouvez utiliser la variable ascii_lowercase du module
string.
"""
import string

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

resultat = {}

for letter in string.ascii_lowercase:
    resultat[letter] = 0

for letter in lorem.replace('.', '').replace(',', '').replace(' ', '').replace('\n', '').replace('\t', '').lower():
    resultat[letter] += 1

print(resultat)

# Autre solution

import string

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

alphabet = string.ascii_lowercase
resultat = dict(zip(alphabet, [0] * len(alphabet)))

for lettre in lorem.lower():
    if resultat.get(lettre) is not None:
        resultat[lettre] += 1

print(dict(resultat))

"""
+ Explication
Dans cet exercice, le but était de compter le nombre d'occurence de chaque lettre de l'alphabet dans le texte contenu
dans la variable "lorem" pour obtenir le cictionnairre suivant:
{'a': 29, 'b': 3, 'c': 16, 'd': 19, 'e': 38, 'f':3, 'g': 3, 'h': 1, 'i': 42, 'j': 0, 'k': 0, 'l': 22, 'm': 17, 'n': 24,
'o': 29, 'p': 11, 'q': 5, 'r': 22, 's': 18, 't': 32, 'u': 29, 'v': 3, 'w': 0, 'x': 3, 'y': 0, 'z': 0}

Comme nous l'avons déjà fait, nous récupérons toutes les lettres de l'alphabet grâce au module string et la constante
ascii_lowercase.

Pour commencer, nous créons une liste de la meme longueur que notre variable "alphabet":
0 * len(alphabet)
Ce qui nous donne donc la liste suitvante:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Nous utilisons ensuite la fonction zip et la fonction dict pour créer un dictionnaire qui contient chaque lettre de 
l'alphabet comme clé et le nombre 0 comme valeur:
resultat = dict(zip(alphabet, [0] * len(alphabet)))
Ce qui nous donne le dictionnaire suivant:
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

Nous passons ensuite avec une boucle for sur chaque lettre de notre variable "lorem""
for lettre in lorem.lower():
Nous faisons une petite vérification pour s'assurer que la lettre courante existe dans notre dictionnaire "resultat"
(cela nous permet de filtrer les signes de ponctuations, les espaces etc) grâce à la méthode get.
L'intérêt de cette méthode est que si la clé n'existe pas, la méthode retourne None, ce qui nous permet de tester
l'existence d'une clé dans un dictionnaire dans un structure conditionnelle sans risquer de faire planter notre script.

Il faut également faire attention de ne pas juste mettre if resultat.get(lettre) car la valeur de base que nous insérons
dans le dictionnaire est 0. if 0 est équivalent à if False et la condition ne sera donc pas vérifiée. Il faut donc 
explicitement vérifier si resultat.get(lettre) n'est pas égal à None pour que la structure conditionnelle soit vérifiée
même si le get nous retourne 0: if resultat.get(lettre) is not None:
Enfin, si cette lettre existe dans notre dictionnaire, nous ajoutons 1 à la valeur associée à la clé de la lettre
contenue dans le dictionnaire:
resultat[lettre] += 1
Ainsi, nous allons incrémenter à chaque fois cette valeur et ainsi compter le nombre d'occurence de chaque lettre dans 
notre variable "lorem".

+ Solution alternative
Rappelez-vous qu'il est toujours possible de faire plus simple et plus concis. Pour le plaisir des yeux, voici donc une 
façon de résoudre cet exercice en une seule igne, en utilisant la fonction count:
dict([a, lorem.lower().count(a)) for a in string.ascii.lowercase])

+ Points importants à retenir
1. Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip

2. Pour créer un dictionnaire à partir d'une liste de tuple, on utilise la fonction dict.

3. Pour récupérer la valeur d'une clé dans un dictionnaire sans risquer de faire planter notre script si la clé 
n'existe pas, on utilise la methode get.

"""

print("\n Exercice83")
"""
Recréer la methode isdigit.
+ Notions abordées: Les fonctions, les boucles, les structures conditionnelles.
Dans cet exercice, nous allons créer une méthode appartenant aux chaînes de caractères, la méthode isdigit, qui permet
de vérifier si une chaîne de caractère ne contient que des nombres.
Nous allons transformer cette méthode en fonction.
 
A vous donc de combler la fonction isdigit() afin de vérifier si la chaîne de caractère que l'on passe (ici "1864274") 
contient uniquement des nombres.
Votre script doit dans ce cas-ci retourner True.
Bien entendu, vous ne devez pas utiliser la méthode isgigit !

+ Aller plus loin: Vérifiez également si l'argument passé à la fonction est bien une chaîne de caractère afin
d'éviter les erreurs (si par exemple l'utilisateur envoi une liste ou un boolean).

+ Astuces: Afin de vérifier chaque caractère de la chaîne de caractère, il vous faudra utiliser une boucle for.
"""


def isdigit(nombre):
    for digit in nombre:
        if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False

    return True


print(isdigit("1854274"))

"""
+ Autre solution possible:
def isdigit(variable):
  for i in variable:
    if i not in [str(n) for n in range(10)]
      return False
      
  return True

print(isdigit("1854274")

+ Explication
Dans cet exercice, on continue avec la création de fonctions et méthodes disponibles de base dans Python.
Dans cet exercice, nous créons une fonction isdigit qui imite le comportement de la méthode isdigit, qui permet
de vérifier si une chaîne de caractère est composée uniquement de chiffres.

La première chose à faire était donc logiquement de créer une fonction isdigit qui accepte une variable en argument:
def isdigit(variable):
jusque là rien de bien compilqué.

Ensuite, il faut que nous vérifions chaque caractère de la chaîne de caractère qui nous est passée en argument afin de
savoir si c'est un chiffre ou non.
Généralement pour vérifier si une chaîne de caractère est un nombre, on utilise la méthode isdigit. Ici, interdit de 
l'utiliser, il va donc falloir faire autrement.

Comment vérifier si une chaîne de caractère correspond à un chiffre?
Facile, il suffit de vérifier s'il est égal à 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Si c'est le cas, alors la chaîne de 
caractère est bien un chiffre.

Il nous faut donc créer une liste qui contient tous les chiffres de 0 à 9, ce que nous faisons avec la compréhension de 
liste suivante [str(n) for n in range(10)]

Nous convertissons directement chaque chiffre "n" récupéré dans la boucle en chaîne de caractère avec la fonction str,
car dans notre boucle for, la variable i que nous récupérons est une chaîne de carctère.

La compréhension de liste ci-dessus nous retourne donc une liste de tous les chiffres de 0 à 9 en chaîne de caractère:
["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

Pour vérifier si la chaîne de caractère récupérée dans la variable "i" dans notre boucle for appartient ou non à cette
liste, on utilise une sturcutre conditionnelle et la condition "in":
if i not [str(n) for n in range(10)]:

Ici, nous utilisons "not in" car la variable "i" n'est pas présente dans notre liste, alors cela veut dire que la chaîne
de caractère passée à notre fonction contient un caractère qui n'est pas égal à un chiffre.

Pas besoin d'aller plus loin donc et de passer en revue tous les caractères restants, nous pouvons arrêter la fonction
directement à ce stade et retourner False.

Si nous finissons la boucle for sans jamais avoir vérifié cette condition, cela signifie que nous n'avons rencontré 
aucun cactère dans notre variable qui n'était pas un chiffre: notre variable ne contient donc que des chiffres et nous 
pouvons retourner True.

+ Points importants à retenir
1 - Pour créer rapidement et efficacement des listes, on peut utiliser des compréhensions de liste et la fonction range.
2 - Pour vérifier si une variable est présente ou non dans une liste, on utilise "in" dans une condition: if variable in
liste. La condition retournera True si la varialbe est présente dans la liste et False dans le cas contraire.
"""
print("\n Exercice83")
"""
+ Notions abordées: les fonctions.
On continue avec les fonctions et méthodes de base que l'on essaie de comprendre et de recréer. Cette fois-ci, on
s'intéresse à la méthode join() qui permet de joindre plusieurs éléments d'une liste par une chaîne de caractère.

Nous allons donc recréer cette méthode et la transformer en fonction. Votre fonction devra prendre comme premier 
argument l'élément avec lequel vous voulez séparer les éléments de votre liste.

A la place d'une liste, nous passrons ici directement à la fonction des chaînes de caractère à joindre ensemble.
Votre fonction devra donc être appelée de la façon suivante:
join(":", "Bonjour", "tout", "le", "monde")
Et retournera la chaîne de caractère suivante:
"Bonjour:tout:le:monde"
"""

# def join(*mots):
#     phrase = ""
#
#     for word in range(1, len(mots)):
#         if word == 1:
#             phrase += mots[word]
#         else:
#             phrase += mots[0] + mots[word]
#     return phrase
#
#
# j = join(":", "Bonjour", "tout", "le", "monde")
# print(j)

"""
+ Autre solution possible:
def join(*args):
  resultat = ""

  separateur = args[0]
  elements = args[1:]
  
  for element in elements:
    resultat += element + separateur
    
  return resultat[:-1]
  
j = join(":", "Bonjour", "tout", "le", "monde")
print(j)

+ Explication
Le but de cet exercice était de recrée la méthode join, encore une fois en la transformant en fonction.

La méthode join s'utilise sur une chaîne de caractère et permet de joindre plusieurs éléments d'une liste par la chaîne 
de caractère en question. Par exemple: "-".join(["Bonjour", "tout", "le", "monde"]) pour joindre 4 mots dans la liste
par des tirets.

Nous allons donc recréer cette méthode en la transformant en fonction : en premier argument nous passerons le caractère
de séparation, puis tous les autres arguments correspondront aux mots que l'on veut joindre ensemble.

Notre fonction join pouvant accepter un nombre indéfini de paramètre, il nous faudra donc utiliser les "args":
def join(args)

Notez que ce qui est vraiment important ici c'est l'estérisque. Vous pourriez remplacer "args" par "robert" et votre
code fonctionnerait également. args est une convention et nous allons donc l'utiliser.

Cette syntaxe nous permet de passer un nombre indéfini d'arguments à notre fonction: ces arguments seront récupérables
dans la liste "args" à l'intérieur de notre fonction.

A l'intérieur de notre fonction, nous récupérons donc le premier élément de la liste args, qui correspondra au 
séparateur utilisé pour joindre les arguments suivants:
separateur = arg[0]

Nous récupérons ensuite tous les arguments restants grâce à la syntaxe des slices:
element = args[1:]

Cette syntaxe indique que nous voulons récupérer tous les éléments à partir du 1er indice, jusqu'à la fin de la liste.
Cela nous permet donc de récupérer dans ce cas-ci les mots "Bonjour", "tout", "le", "monde".

Il ne nous reste plus qu'à joindre ensemble tous les éléments récupérés dans la liste "elements" par le séparateur
contenu dans la variable "separateur". Nous avons défini au début de la fonction une variable "resultat" qui contient
une chaîne de caractère vide.

Nous allons passer à travers chaque élément grâce à une boucle for et ajouter un à un les éléments et le séparateur à la
variable "resultat":

for element in elements:
  resultat += element + separateur

A ce stade-ci, la variable "resultat" contient donc:

"Bonjour:tout:le:monde:"

Tout fonctionne à merveille, le seul problème est que nous avons un séparateur en trop à la fin de notre chaîne de
caractère. Nous allons donc retourner notre chaîne de caractère en enlevant le dernier caractère, là encore grâce aux
slices, qui peuvent également être utilisés directement sur une chaîne de caractère (car une chaîne de caractère est
comme une liste de caractère individuels):
return resulat[:-1]

Cette syntaxe indique que nous souhaitons récupérer tous les caractères de la chaîne de caractère sauf le dernier (-1).

+ Points importants à retenir
1. Pour envoyer et récupérer un nombre indéfini d'arguments à une fonction, on utilise *args.

2. Pour récupérer tous les éléments d'une liste sauf le premier, on utilise la syntaxe de slice[1:]

3. Pour récupérer tous les éléments d'une liste ou d'une chaîne de caractère sauf le dernier, on utilise la syntaxe
de slice[:-1]

"""

print("\n exercice 85")
# import os
# import string
#
# dossier = os.path.dirname(__file__)
# alphabet_dir = os.path.join(dossier, "alphabet")
#
# for letter in string.ascii_uppercase:
#     lettre_dir = os.path.join(alphabet_dir, letter)
#     if not os.path.isdir(lettre_dir):
#         os.makedirs(lettre_dir)
#
# """"
# + Autre solution possible (qui ne permet pas de choisir ou l'on creait le repertoire :-(
# import os
# for lettre in string.ascii_uppercase:
#     os.makedirs(f'/ alphabet / {lettre}')
# """

print("\n exercice 86")
# # https://www.udemy.com/course/python-exercices/learn/lecture/11731636#overview
# import os
# dossier = "/Utilisateurs/MOTTIER LUCIE/Documents/Test"
# mot = "Python"
# fichiers_trouves = []
#
# for root, directories, filename in os.walk(f"/Users/MOTTIER LUCIE/Documents/Test"):
#     print(root," - ", directories, " - ", filename)
#     with open(filename, "r") as file:
#         contenu_fichier = file.read()
#         if mot not in contenu_fichier:
#             fichiers_trouves.append(file)
#
# print(fichiers_trouves)


# # """Autre solution possible:"""
# import os
# from glob import glob
#
# dossier = "/Users/Mottier Lucie/Documents/Test"
# mot = "Python"
#
# fichiers = glob(f"{dossier}/**/*.txt", recursive=True)
#
# fichiers_trouves = []
#
# for filename in fichiers:
#     with open(filename, "r") as file:
#         contenu_fichier = file.read()
#         if mot in contenu_fichier:
#             fichiers_trouves.append(filename)
#
# print(fichiers_trouves)
#
#
# print("\n exercice 87")
#
# class SuperStr(str):
#     def __init__(self, chaine):
#         self.chaine = chaine
#
#     def __add__(self, mot):
#         return SuperStr(f"{self.chaine} {mot}")
#
# s = SuperStr("Bonjour")
# print(s + "tout" + "le" + "monde")
# print(s.__add__("tout").__add__("le").__add__("monde"))
# # en fait le + appel automatiquement l'operateur __add__ ce qui permet de simplifier la syntaxe

print("\n exercice 88")
# # ma solution
# liste = liste2 = []
# test = True
# def buble_sort(liste):
#     i = 0
#     # while (test):
#     for element in liste:
#         while element >= liste[i]:
#             i += 1
#             if i == len(liste):
#                 print(element)
#                 liste2.insert(0, element)
#                 liste.remove(element)
#                 buble_sort(liste)
#
#     print(f"resulat : {liste2}")
# l = [40, 16, 100, 2, 90]
# print(buble_sort(l))

# # Solution du prof
# def buble_sort2(liste):
#     for i in range(len(liste) - 1, 0, -1):
#         print(f'debug {i}')
#         for j in range(i):
#             n_courant = liste[j]
#             n_suivant = liste[j + 1]
#             if n_courant > n_suivant:
#                 liste[j] = n_suivant
#                 liste[j+1] = n_courant
#
#     return liste
# l = [40, 16, 100, 2, 90]
# print(buble_sort2(l))

print("\n exercice 89")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366096#overview
"""
089 - Récupérer un élément dans une liste sans causer d'erreur
+ Notions abordées: les listes, les fonctions, les structures conditionnelles.
Dans cet exercice, nous allons créer une fonction pour récupérer un élément dans une liste, sans causer d'erreur si 
l'indice est en dehors de la liste, comme c'est le cas par défaut avec Python.
Il faut donc insérer du code dans la fonction recuperer_item pour que l'on puisse récupérer grâce à cette fonction les
éléments avec l'indice 0, 5 et -13.
Dans le premier cas, la fonction nous retournera l'élément "Julien", et dans les deux autres cas, les phrases:
    Index 5 hors de la liste
    Index -13 hors de la liste
La fonction aura comme premier paramètre la liste dont on veut récupérer un élément et comme deuxième prameètre l'indice
désiré.
"""
# def recuperer_item(liste, indice):
#     if indice < 0 and abs(indice) <= len(liste):
#         return liste[indice]
#     elif indice > 0 and indice < len(liste):
#         return liste[indice]
#     elif indice ==0 and liste:
#         return liste[0]
#
#     return "Index {} hors de la liste".format(indice)
#
# liste = ["Julien", "Marie", "Pierre"]
#
# print(recuperer_item(liste, 0))
# print(recuperer_item(liste, 5))
# print(recuperer_item(liste, -13))
#
print("\n exercice 90")
# https://www.udemy.com/course/python-exercices/learn/lecture/11774828#overview

# def replace(phrase, mot_a_remplacer, nouveau_mot):
#     while mot_a_remplacer in phrase:
#         debut = phrase.index(mot_a_remplacer)
#         fin = debut + len(mot_a_remplacer)
#
#         phrase = list(phrase)
#         phrase[debut:fin] = list(nouveau_mot)
#         phrase = "".join(phrase)
#     return phrase
#
#
# phrase = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
# print(phrase)

print("\n exercice 91")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366098#overview
"""
091 - Créer une classe personnalisée pour une chaîne de caractère
+ Nontions abordées: les classes, les methodes
Dans cet exercice, on continue avec les classes et les méthodes.
L'ojbectif est de créer une classe qui va nous permettre d'utiliser des noms de méthodes francisés à la place des 
méthodes de base de Python qui sont en anglais.

Les trois méthodes que nous allons recréer sont: upper, lower et capitalize qui ont comme effet respectivement, de 
mettre le texte en majuscule, en minuscule, et en format 'titre' (première lettre en majuscule, le reste en minuscule).

Le but de l'exercice n'est pas de recrée l'algorithme des fonctions anglaises mais juste d'appeler les fonctions upper,
lower et capitalize dans des methodes francisés. Si vous souhaitez cependant compexifier l'exercice, vous pouvez vous
amuser à recréer l'algorithme de ces fonctions en plus.

Nous allons appeler ces fonction respectivement majuscule, minuscule et titre.
"""
# class SuperChaine(object):
#     def __init__(self, chaine):
#         self.chaine = chaine
#
#     def majuscule(self):
#         return self.chaine.upper()
#
#     def minuscule(self):
#         return self.chaine.lower()
#
#     def titre(self):
#         return self.chaine.capitalize()
#
#
# chaine = SuperChaine("UdeMy")
# print(chaine.majuscule())
# print(chaine.minuscule())
# print(chaine.titre())
# # print(chaine.titre())


print("\n exercice 92")
# https://www.udemy.com/course/python-exercices/learn/lecture/11775216#overview

# def get_value(dico, *args):
#     args = list(args)
#     default = args.pop(-1)
#
#     for arg in args:
#         dico = dico.get(arg)
#         if not dico:
#             return default
#     return dico
#
#
# dictionnaire = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# a = get_value(dictionnaire, "01", "identite", "prenom", "valeur inconnue")
# print(dictionnaire.get("02", {}).get("identite", {}).get("prenom", "valeur inconnue"))
#
# print(a)


print("\n exercice 93")
# https://www.udemy.com/course/python-exercices/learn/lecture/11796502#overview

# class CustomListe():
#     def __init__(self, *args):
#         self.valeurs = list(args)
#
#     def append(self, value):
#         if isinstance(value, int):
#             print("Vous ne pouvez pas ajouter de nombre à la liste")
#             return False
#         if isinstance(value, list):
#             self.valeurs.extend(value)
#         elif isinstance(value, str):
#             if value not in self.valeurs:
#                 self.valeurs.append(value)
#
#
# ma_liste = CustomListe('Julien', 'Marie', 'Pierre')
# ma_liste.append(5)
# ma_liste.append('Pierre')
# print(ma_liste.valeurs)

print("\n exercice 94")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366102#overview
"""
094 - Recréer lam méthode split

+ Notions abordees: Les fonctions, les boucles, les structures conditionnelles.
Dans cet exercice, nous allons re-creer la methode split, qui permet de separer une chaine de caracteres en plusieurs
elements, en specifiant un caracter ou une chaine de caracteres avec lequel separer la phrase.
Nous allons separer la phrase "bonjour-tout-le-monde" sur le (-) pour ainsi recuperer la liste suivante:
["bonjour", "tout", "le", "monde"]
Bien sure, la encore, pas le droit d'utiliser la methode split native dans Python.
Nous utiliserons la fonction separateur en indiquant en premier parametre la phrase à separer et en deuxieme parametre
la chaine de caracteres sur laquelle faire la separation.
"""
#
#
# def sepearateur(phrase, separateur):
#     mot_courant = ""
#     liste = []
#
#     for letter in phrase:
#         if letter != "-":
#             mot_courant += letter
#         else:
#             liste.append(mot_courant)
#             mot_courant = ""
#
#     liste.append(mot_courant)
#     return liste
#
#
# phrase = "bonjour-tout-le-monde"
# print(sepearateur(phrase, "-"))
"""
+ EXPLICATION
Dans cet exercice, il fallati recreer la method split, qui permet de separer une chaine de caractère en plusieurs 
éléments.

Une méthode un peu plus complexe à recréer que celle que nous avons eu à refaire dans des exercices précédent.

Notre fonction "separateur" acceptera deux pramètres: la chaîne de caractère à séparer et l'élément sur lequel on sépare
cette chaîne  de caractère:
    def separateur(mot, sep):

Nous initialisons ensuite deux variables vides:
    liste = []
    mot_courant = ""
    
Il nous faut enusite passer à travers chaque caractère de la chaîne de carctère contenue dans la variable "mot" pour 
vérifier si on est en présence duc caractère séparateur ou non.

Nous avons donc une structure conditionnelle à l'intérieur de la boucle for, qui vérifie si la lettre courante est égale
ou non au séparateur. Si c'est le cas, nous ajoutons la lettre à la variable "mot courrant":
    for lettre in mot:
        if lettre != sep:
            mot_courrant += lettre
            
Dans le cas de la phrase "bonjour-tout-le-monde", nous allons donc ainsi ajouter les 7 premières lettres à notre 
variable mot_courant.

Puis, dans le cas où nous sommes en présence du séparateur, nous allons dans la deuxième partie de la structure 
conditionnelle, le "else", dans lequel nous ajoutons le mot_courant à notre variable "liste" et nous reinitialisons la
variable mot_courant à une chaîne de caractère vide:
    else:
        liste.append(mot_courant)
        mot_courant = ""

Une fois que nous sortons de la boucle for, il ne faut pas oublier d'ajouter le contenu de la variable "mot_courant" 
dans notre list.

En effet, on ajoute la chaîne de cartère "mot_courrant" à notre liste uniquement quand on rencontre un séparateur. A
moins donc que notre chaîne de caractère ne finisse par un séparateur, si nous n'ajoutons pas une dernière fois la 
variable "mot_courant" à notre liste, nous manquerons le dernier mot de notre phrase.

+ POINTS IMPORTANTS A RETENIR
1. Pour vérifier si une variable est différente d'une autre, on utilise la syntaxe !=
2. Pour vérifier si une variable est égale à une autre, on utilise la syntaxe == 
"""

print("\n exercice 95")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366104#overview
""" 
095 - Créer une classe pour gérer des voitures

+ Notions abordees: les classes, les instances.
Dans cet exercice sur les classes, on commence doucement avec un exercice dans lequel le but est de creer une classe 
Voiture qui va contenir trois attributs:
La marque de la voiture, son prix, et sa couleur.
A vous donc de completer le code de la classe Voiture afin que les trois print à la fin du script retournent 
respectivement la marque, le prix et la couleur de la voirture ('Lamborghini', '150000' et 'rouge').
"""

# class Voiture:
#     def __init__(self, marque, prix, couleur):
#         self.marque = marque
#         self.prix = prix
#         self.couleur = couleur
#
#
# super_voiture = Voiture("Lamborghini", 150000, "rouge")
# print(super_voiture.marque)
# print(super_voiture.prix)
# print(super_voiture.couleur)
"""
EXPLICATION
On passe avec ces exercices dans des sujets un peu plus complexes de Python avec les classes. Cet exercice etait 
cependant encore tres simple pour qui maitrise l'oriente objet.

Le but de cet exercice etait de creer une classe qui contient trois attributs: la marque, le prix et la couleur de la 
voiture.

Il suffisait donc de creer la methode __init__, qui contient trois paraametres(sans compter "self"):
    class Voiture:
        def __init__(self, marque, prix, couleur)
        
Nous creons ensuite 3 variables (marque, prix et couleur), appartenant à la classe, à partir des arguments passes à la 
fonction __init__ lors de li'instanciation de la classe:
    class Voiture:
        def __init__(self, marque, prix, couleur):
            self.marque = marque
            self.prix = prix
            self.couleur = couleur
            
Nous pouvons donc ensuite creer une instance de notre classe en passant respectivement la marque, le prix et la couleur
de la voiture à la classe:
    super_voiture = Voiture("Lamborghini", 150000, "rouge")
    
+ POINTS IMPORTANTS A RETENIR
1. La methode "magique" appelee lors de l'instanciation d'une classe est la methode __init__
"""

print("\n exercice 96")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366110#overview
"""
096 - Modifier la représentation d'une classe

+ Notions abordees: les classes, les methodes.
Dans cet exercice, nous continuons avec notre classe Voiture.
Le but de cet exercice est de changer la representation de notre class afin de pouvoir faire un print d'une instance de
notre classe et avoir des informations precises sur notre instance.
Notre script doit donc retourner la phrase suivante lorsqu'on print une instance de notre classe:
>> super_voiture = Voiture("lamborghini", 150000, "rouge")
>> print(super_voiture)
Votre voiture est un Lamborghini rouge et coute 150000$
"""
# class Voiture:
#     def __init__(self, marque, prix, couleur):
#         self.marque = marque
#         self.prix = prix
#         self.couleur = couleur
#
#     def __repr__(self):
#         return f'Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}$'
#
#
# super_voiture = Voiture("Lamborghini", 150000, "rouge")
# print(super_voiture)
"""
EXPLICATION
Encore une fois une exercice assez simple pour qui maitrise l'oriente objet, mais qui aborde tout de meme des notions
moins connus du "grand public".

Ici, il fallait modifier la representation de la classe Voiture, c'est à dire ce qui nous est retourne lorsque l'on
print une instance cree à partir de la classe Voiture.

Il fallait pour ce faire re-implementer la methode special__repr__:
    def __repr__(self)
        return 'f'Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}$'
        
Nous utilisons la method format ainsi que les attributs marque, couleur et prix de la classe pour afficher les 
informations de l'instance de notre Voiture.

+ POINTS IMPORTANTS A RETENIR
    1 - Pour modifier la representation d'une classe, on utilise la methode speciale __repr__.
"""

print("\n exercice 97")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366112#overview
"""
097 - Créer des classes de base avec les classmethod

+ Notions abordées: les classes, les méthodes.
On continue encore et encore avec notre classe Voiture, pour laquelle nous allons manintenant créer des 'classmethod'.
Cela nous permettra donc de définir une marque, un prix et une couleur par defaut pour 2 types de voitures de luxe: une
lamborghini et une proshe.

Nous allons donc à partir de ces deux classmethod créer deux instances de voitures:
    lamborhini = Voiture.lamborghini()
    print(lamborghini.prix)
    150000
    porsche = Voiture.porsche()
    print(porsche.prix)
    200000
    
La lamborghini devra avoir comme marque "Lamborhini", comme prix 150 000$ et comme couleur "rouge".
La porsche quand à elle devra avoir comme marque "Porshce", comme prix 200 000$ et comme couleur "noire"/
"""

# class Voiture(object):
#     def __init__(self, marque, prix, couleur):
#         self.marque = marque
#         self.prix = prix
#         self.couleur = couleur
#
#     @classmethod
#     def lamborghini(cls):
#         return cls("lamborghini", str(150000) + "$", "rouge")
#
#     @classmethod
#     def porsche(cls):
#         return cls("porsche", str(200000) + "$", "noire")
#
#
# lamborghini = Voiture.lamborghini()
# print(lamborghini.prix)
# porsche = Voiture.porsche()
# print(porsche.prix)

"""
EXPLICATION
Dans cet exercice, on continue dans les fonctions avancées de l'orienté objet avec les classmethod.

Pour spécifier qu'une méthode est une "classmethod", on utilise le decorateur @classmethod.

Cela nous permet de déclarer deux méthodes, "lamborghini" et "porsche", qui vont nous permettre de créer des instances
à partir de notre classe Voiture plus facilement.

Une "classmethod" a comme premier paramètre, la classe elle-même, qui par convention est appelé "cls":
    @classmethod
    def lamborghini(cls):
        pass
        
A l'intérieur de cette méthode "lamborghini", nous pouvons donc utilier "cls" pour référer à la class Voiture:
    return cls("Lambroghini", 150000, "rouge")
    
Dans le cas de la méthode "lamborghini", nous retournons donc une instance céé à partir de la classe "Voiture", dont la 
marque est "Lamborghini", le prix 150 000 et la couleur "rouge".

On fait de même pour la porsche avec des valeurs différentes pour chaque attribut:
    classmethod
    def porsche(cls):
        return cls("Porsche", 200000, "noire")
        
Vela nous permet donc de créer facilement des modèles pour chaque type de voiture, afin de pouvoir facilement créer des
voitures de marques célèbres:
    lamborghini = Voiture.lamborghini()
    porsche = Voiture.porsche()
    
+ POINTS IMPORTANTS A RETENIR
1. Pour définir une méthode comme "classmethod" on utilise le décorateur @classmethod.
2. Par convention, le premier pramètre d'une classmethod, représentant la classe, est appelé "cls".
"""

print("\n exercice 98")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366116#overview
"""
098 - Ajouter une propriété à la classe Voiture

+ Notions abordées: les classes, les propriétés.
On continue avec notre classe Voiture qui commence à devenir assez intéressante à utiliser.

Néanmoins, depuis le début, nous fonctionnons avec des prix en dollars ($). Pour un concessionnaire automobile qui
aurait des sccursales dans plusieurs pays, il va devenir important d'avoir un moyen d'acceder facilement au prix d'une
voiture dans un autre devise.

Nous allons donc dans cet exercice, ajouter un méthode qui repose sur le principe des propriétés et qui nous permettra
d'accéder au prix en euros de la facon suivante:
    lamborghini = Voiture.lamborghini()
    print(lamborghini.prix)
    150000
    print(lamborghini.prix_euros)
    225000
"""

# class Voiture:
#     def __init__(self, marque, prix, couleur):
#         self.marque = marque
#         self.prix = prix
#         self.couleur = couleur
#
#     @classmethod
#     def lamborghini(cls):
#         return cls("Lamborghini", 150000, "rouge")
#
#     @property
#     def prix_euros(self):
#         prix_euros = self.prix * 1.5
#         return round(prix_euros)
#
#
# lamborghini = Voiture.lamborghini()
# print(lamborghini.prix)
# print(lamborghini.prix_euros)


print("\n exercice 99")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366120#overview
"""
099 - Erreur d'heritage entre deux classes

+ Notions abordées: les classes, l'hériage.
Le but de cet exercice est de trouver l'erreur d'héritage qui s'est glissée dans le script de départ.
Le print de chien.race va dans l'état actuel des choses nouts retourner une erreur (AttributeError: 'Chihuahua' object 
has no attribute 'race').
A vous de trouver pourquoi cette erreur apparaît et modifiez la classe Chihuahua afin que le print affiche la race du
chien:
    >>> print(chien.race)
    "Chihuahua
"""

# class Chien:
#     def __init__(self, race):
#         self.race = race
#
#     @property
#     def taille(self):
#         return 100
#
#
# class Chihuahua(Chien):
#     def __init__(self, nom):
#         super().__init__("Chihuahua")
#         self.nom = nom
#
#
# chien = Chihuahua("Lily")
# print(chien.race)
"""
EXPLICATION
Cet exercice touche à l'héritage et contenait une erreur que vous deviez identifier et résoudre.
Le problème du script de départ était que la classe Chihuahua n'appelait jamais le constructeur __init__ de la fonction
dont elle héritait.

Nous essayion d'afficher la race du chien alors qu'ell n'est pas définie dans la classe Chihuahua, et la classe "Chien"
dont Chihuahua hérite et qui contient l'attribut race dans sa méthode __init__ n'est jamais appelée.

Pour remédier à cela, nous utilisons la fonction "super" qui nous permet d'appeler la méthode __init__ de la classe 
parent de Chihuahua:
    super().__init__("Chihuahua")

Vous remarquerez que nous profitons de l'appel à la méthode __init__ pour passer en argument la race du chien 
("Chihuahua"), ce qui permettra donc d'afficher la bonne valeur lors du print de la race du chien à la dernière ligne du
script.

A la place de la fonction super, on peut explicitement utiliser le nom de la classe parente:
    Chien.__init__(self, "Chihuahua")
L'avantage d'utiliser la fonction super est que nous n'avons pas besoin de référer directement au nom de la classe 
parent.
Ainsi, si nous décidons plus tard de renommer la classe "Chien" en "Chat", notre classe "Chihuahua" fonctionera toujours
si on utilise super, mais nous retournera une erreur si on utilise explicitement le nom de la classe "Chien".

+ POINTS IMPORTANTS A RETENIR
1. Pour appeler une fonction d'une classe parente, on peut utliser la fonction super.
"""

print("\n exercice 100")
# https://www.udemy.com/course/python-exercices/learn/quiz/5366126#overview
"""
100 - Créer une classe qui hérite d'une autre
+ Notions abordées: les classes, l'héritage.
Dans cet exercice, on retrouve notre chère classe Voiture, avec cette fois-ci un exercice sur l'héritage.
Plutôt que de passer par les classmethod comme nous l'avions fait précédemment, nous allons cette fois-ci créer une 
classe Lamborghini qui va hériter de la classe Voiture.
Voici ce que doit retourner votre script final:
>>> ma_voiture = Lamborghini()
>>> print(ma_voiture.vitess_max)
300
>>> print(ma_voiture.couleur)
noire
>>> print(ma_voiture)
Je suis une voiture de luxe

Vous voyez donc que la vitesse maximale a été augmentée et passe à 300km/h au lieu de 200, que la représentation de la
classe change aussi pour afficher que c'est une voiture de luxe. Seule la couleur n'a pas changé et affiche toujour la
couleur "noire" par défaut de la classe Voiture.
"""

# class Voiture(object):
#     def __init__(self):
#         self.couleur = "noire"
#         self.vitesse_max = 200
#         self.prix = 25000
#
#     def __repr__(self):
#         return "Je suis une voiture normale"
#
#     @property
#     def prix_reduit(self):
#         return self.prix * 0.75
#
#
# class Lamborghini(Voiture):
#     def __init__(self):
#         super().__init__()
#         self.vitesse_max = 300
#         self.prix = 100000
#
#     def __repr__(self):
#         return "Je suis une voiture de luxe"
#
#
# ma_voiture = Lamborghini()
# print(ma_voiture.couleur)
# print(ma_voiture.vitesse_max)
# print(ma_voiture)

"""
EXPLICATION
Le but de cet exercice était de créer une classe "Lamborghini" qui hérite de la class Voiture et de tous ses attributs.

Pour commencer, il fallait donc créer une classe Lambroghini qui hérite de la classe Voiture:
    class Lamborghini(Voiture):
Pour hériter d'une classe rien de plus simple que d'indiquer le nom de la classe dont on veut hériter dans les 
parenthèse après la définition de la classe.

Pour pouvoir hériter de tous les attributs définis dans la méthode __init__ de la classe Voiture, il nous faut appeler
cett méthode grâce à la fonction super:
    super().__init__()
Nous avons donc ainsi accès dans notre classe Lamborghini aux attributs "couleur", "vitesse_max" et "prix" définie dans
la classe Voiture.

Nous modifions ensuite les valeurs par défaut des attributs "vitesse_max" et "prix" (parce qu'une Lamborghini, ça va
vite et ça coûte chère)
    self.vitesse_max = 300
    self.prix = 100000
    
Pour finir, nous ré-implémentons la méthode spéciale __repr__ pour signifier que la voiture n'est pas une voiture 
normale mais une voiture de luxe:
    def __repr__(self):
        return "Je suis une voiture de luxe"
        
POINTS IMPORTANTS A RETENIR
1. Pour hériter d'une classe, on indiique le nom de la classe dont on veut hériter entre les parenthèses lors de la 
création de notre classe enfant.

2. Pour appeler une méthode de la classe parent, on utilise la fonction super.
"""

print("\n exercice 101")
# https://www.udemy.com/course/python-exercices/learn/quiz/4459372#overview
"""
101 - Créer une classe pour manipuler les chemins
+ Notions abordées: les classes, les méthodes, les propriétés.

Dans cet exercice, on continue avec les classes: l'objectif va être de créer une classe 'Path' qui va simplifier la 
manipulation de chemins vers des dossiers ou fichiers sur notre disque dur.

Pour les besoins de cet exercice nous allons créer 3 méthodes et propriétés:
1. Une propriété 'ext' pour récupérer l'extension du fichier.
2. Une propriété 'name' pour récupérer le nom du fichier uniquement(donc sans le dossier parent et sans l'extension.)
3. Une méthode 'dirname' qui va récupérer le dossier parent du chemin actuel. Cette méthode devra retourner un objet
Path pour que l'on puisse appliquer de nouveau la méthode 'dirname' sur le résultat précédent.

Notre script devra donc exécuter et retourner les lignes de code suivante:
    >>> s = Path("/Users/thibh/Documents/test.txt")
    >>> print(s.dirname().dirname())
    /Users/thibh
    >>> print(s.name)
    test
    >>> print(s.ext)
    .txt
    
Astuces: Pour déclarer une méthode comme une propriété, vous pouvez utiliser le décorateur @property
"""


class Path(str):

    @property
    def ext(self):
        extension = os.path.splitext(self.chemin)[1]
        extension = extension.strip(".")
        return extension

    def dirname(self):
        return Path(os.path.dirname(self))

    @property
    def name(self):
        basename = os.path.basename(self)
        name = os.path.splitext(basename)[0]
        return name


s = Path("/Users/thibh/Documents/test.txt")
print(s.dirname().dirname())
print(s.name)
print(s.ext)

"""
EXPLICATION
Dans cet exercice, on met en pratique beaucoup d'élément que l'on a vu dans les exercices précédents, avec les classes,
les méthodes et les propriétés.

Le but de cet exercice était de créer une classe "Path" pour nous aider à manipuler des chimins de dossier.

Avec le module os, si on veut remonter dans une structure de dossier, on peut utliser la fonction dirname, mais le code
ne sera pas très élégant:
    os.path.dirname(os.path.dirname(mon_dossier))
Vous conviendrez qu'il serait plus pratique de pouvoir faire:
    mon_dossier.dirname().dirname()
Ce mécanisme est possible en créant notre propre classe.

Pour commencer, nous allons créer une classe Path qui hérite de la classe "str":
    class Path(str):
Cela nous permet d'heriter de toutes les fonctionnalités des chaînes de caractère.

Nous allons créer une première propriété pour facilement accéder à l'extension de notre fichier:
    @property
    def ext(self):
        return os.path.splitext(self)[-1]
        
On utilise la fonction os.path.splitext pour séparer le nom du fichier de l'extension, puis nous récupérons uniquement
l'extension avec [-1].

Vous remarquerez que l'on utilise la fonction splitext directement sur "self".
En effet, vu que l'on hérite de la classe "str", self correspons à la chaîne de carctère que nous passons à notre classe
"Path" lors de la création d'une instance.

Nous créons ensuite une deuxième propriété pour récupérer le nom du fichier uniquement:
    @property
    def name(self):
        basename = os.path.basename(self)
        name = os.path.splitext(basename)[0]
        return name
        
Là encore, rien de bien compliqué.

Pour finir, nous créons une méthode "dirname" qui va nous permettre de récupérer le dossier parent de notre chemin.
Nous utilisons logiquement la fonction dirname du module os.path:
    def dirname(self):
        return Path(os.path.dirname(self))
Cependant, vous remarquez que je ne fais pas simplement que retourner le résultat de la fonction dirname: je retourne
un objet "Path". Cela va nous permettre si nécessaire, de répéter l'opération autant de fois que nécessaire. Si je
retourne uniquement le résultat de la fonction dirname, je me retrouve avec une chaîne de caractère  de base, qui n'aura
donc pas accès à la méthode dirname. En retournant un objet Path, j'aurai accès à cette méthdode dirname et je pourrai
donc refaire l'opération si nécessaire.

Si l'on print le type de la vrariable retournée par la fonction dirname, on voit bien qu'on est en présence d'une 
instance de notre classe "Path":
    >>> dossier_parent = dossier.dirname()
    >>> print(type(dossier_parent))
    <class '__main__.Path'>
    
Dans les deux propriétés précédente, je n'ai pas retourné d'object Path car on retournait pas un chemin mais juste une
chaîne de caractère (le nom du fichier et l'extension). Il ne servait donc à rien de retourner un objet Path dans ce 
cas-ci.

POINTS IMPORTANTS A RETENIR
1. Vous pouvez retourner une instance de votre classe afin de pouvoir répéter la même méthode encore et encore sur une
instance de votre classe.
"""
