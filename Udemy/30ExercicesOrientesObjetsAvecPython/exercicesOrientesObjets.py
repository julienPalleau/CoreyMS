# Exercice 1
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842284#overview
"""
01 - Créer une classe
Dans cet exercice, vous devez créer une classe livre.
La classe doit juste être déclarée (vous pouvez mettre une instruction pass à l'intérieur).
Vous devez ensuite créer une instance harry_potter à partir de cette classe Livre.
"""

# class Livre:
#     pass
#
#
# harry_potter = Livre()

"""
EXPLICATIONS
Pour définir une classe, on utilise l'instruction class suivi du nom de la classe:
    class Livre:
        pass
        
Il ne faut pas oublier de terminer la ligne par le symbole deux-points.

Pour que Python ne nous retourne pas d'erreur on est obligé de mettre au moins une ligne de code à l'intérieur de la
classe, dans ce cas-ci l'instruction pass qui ne fait rien.
"""

# Exercice 2
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842286#overview
"""
002 - Initialiser une instance

Dans cet exercice, vous devez initialiser l'instance harry_potter et créer un attribut d'instance pour que l'instance
ait un prix différent de celui par défaut.
L'instance harry_potter devra donc avoir un prix de 19.99 euros.
L'attribut de classe prix de la classe Livre lui ne doit pas changer et doit rester à 9.99 euros.
Vous devez créer une méthode pour initialiser l'instance.
Vous ne pouvez pas simplement modifier l'attribut prix de l'instance pour lui donner la valeur de 19.99.
Si vous faitez ceci, l'exercice ne sera pas validé.
"""

# class Livre:
#     prix = 9.99
#
#     def __init__(self, prix):
#         self.prix = prix
#
#
# harry_potter = Livre(19.99)
# print(harry_potter.prix)
#
# james_bond = Livre(10.55)
# print(james_bond.prix)

"""
EXPLICATIONS
Pour initialiser une instance, on utilise la méthode __init__ qui est appelée automatiquement lorsque l'on crée une 
instance.

A l'intérieur de cette méthode, il ne faut pas oublier de mettre en premier paramètre self, qui correspond à notre 
instance, et va nous permettre à l'intérieur de cette méthode de créer un attribut propre à notre instance.

Cet attribut prix est le deuxième paramètre que nous donnons à la méthode __init__.

Ainsi, nous pouvons définir un prix personalisé pour notre instance au moment de sa création:
    harry_potter = Livre(19.99)
    
Et le récupérer pour l'assigner à notre instance (self) dans la méthode __init__:
    def __init__(self, prix):
        self.prix = prix
        
Ainsi, on definit un attribut prix uniquement sur notre instance (self) et l'attribut de classe prix reste inchange à
9.99 euros.

POINTS IMPORTANTS A RETENIR
1. Pour initialiser une instance, on utilise la méthode __init__.
2. Pour référer à notre instance à l'intérieur d'une méthode, on utilise le pramètre self.
3. Pour créer un attribut d'instance, on utilise la syntaxe self.attribut = valeur
"""

# Exercice 3
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842288#overview
"""
003 - Créer un employé

Dans cet exercice, vous devez créer une classe Employe qui permettra de créer des employés qui auront 4 attributs:
1. prenom
2. nom
3. position
4. salaire

On doit donc pouvoir avec votre script créer une instance de la sorte:
john = Employe("Jhon", "Smith", "Developpeur Python", 4500)
"""

# class Employe:
#     def __init__(self, prenom, nom, position, salaire):
#         self.prenom = prenom
#         self.nom = nom
#         self.position = position
#         self.salaire = salaire
#
#
# john = Employe("John", "Smith", "Developpeur Python", 45000)

"""
EXPLICATION
Pour créer une classe, on utilise l'instruction class.

Afin de pouvoir initialiser directement les instances créées avec des attributs, on utilise la méthode __init__ qui
contient 4 paramètres (en plus du self):
1. prenom
2. nom
3. position
4. salaire

Afin de créer des attributs sur notre instance, il faut assigner les valeurs passées lors de la création de l'instance,
à notre instance à l'intérieur de la méthode __init__ (qui est récupérée par le paramètre self):
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire
        
Notez que dans ce cas-ci, le nom des paramètres de la méthode __init__ et le nom des attributs est le même, mais ce 
n'est pas une obligation! On pourrait très bien faire comme ceci:
    class Employe:
        def __init__(self, a, b, c, d):
            self.prenom = a
            self.nom = b
            self.position = c
            self.salaire = d
            
    John = Emplye("John", "Smith", "Dev Python", 4500)
Mais ça serait beaucoup moins clair, il vaut donc mieux utiliser des noms de parmètres explicites.

POINTS IMPORTANTS A RETENIR
1. Pour initialiser une instance, on utilise la méthode __init__.
2. Pour créer un attribut d'instance à l'intérieur de la méthode __init__, on utlise la syntaxe self.attribut = valeur
"""

# Exercice 4
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842290#overview
"""
004 - Créer un attribut de classe
"""

# class Livre:
#     prix = 9.99

"""
EXPLICATIONS
Pour créer un attribut de classe, c'est très simple, il suffit de déclarer une variable directement à l'intérieur du boc
d'instruction appartenant à la classe.

Pas besoin de self ou quoi que ce soit d'autre vu que l'attribut appartient directement à la classe.

On peut par la suite accéder à l'attribut comme suit:
    >>> Livre.prix
    9.99
    
POINTS IMPORTANTS A RETENIR
1. Pour créer un attribut de classe, on le définit directement à l'intérieur de la classe, sans avoir besoin d'utiliser
self.
"""

# Exercice 5
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842292#overview
"""
005 - Changer l'affichage d'une instance

Dans cet exercice, vous devez ajouter une méthode 'spéciale' à la classe Employe pour changer l'affichage des instances
de cette classe. En effet, avec le code de départ, si on affiche les instances contenues dans l'attribut 
Entreprise.employes, on obtient le résultat suivant, qui n'est pas très exiplicite:
    [<__main__.Employe object at 0x102356860>,
     <__main__.Employe object at 0x102356898,
     <__main__.Employe object at 0x1023568d0>]
A la place, on aimerait afficher le prénom et le nom des employés, comme ceci:
    [Pierre Smith,
     Julie Martin,
     Eric Dupont]
Vous devez donc utliser cette méthode 'magique' pour changer la représentation des instances.
"""

# class Entreprise:
#     nom = "Docstring"
#     employes = []
#
#
# class Employe:
#     def __init__(self, prenom, nom, position, salaire):
#         self.prenom = prenom
#         self.nom = nom
#         self.position = position
#         self.salaire = salaire
#
#     def __repr__(self):
#         return f'{self.prenom} {self.nom}'
#
#
# employes = [
#     ("Pierre", "Smith", "Responsable RH", 35000),
#     ("Julie", "Martin", "Développeur Python", 42000),
#     ("Éric", "Dupont", "Chef de projet", 50000),
# ]
#
# for employe_data in employes:
#     employe = Employe(*employe_data)
#     Entreprise.employes.append(employe)
#
# print(Entreprise.employes)

"""
EXPLICATIONS
Pour réussir cet exercice, il fallait ajouter à la classe Employe la méthode spéciale __repr__ qui permet de changger la
représentation des instances de la classe:
    def __repr__(self):
        return f"{self.prenom} {self.nom}"
        
A l'intérieur de cette méthode, on retourne tout simplement le prénom de notre instance (respectivement self.prenom et
self.nom) que l'on formate à l'intérieur d'une chaîne de caractères grâce aux f-string.

POINTS IMPORTANTS A RETENIR
1. Pour changer la représentation d'une instance, on implémente la méthode 'spéciale' __repr__ dans laquelle on peut 
retourner une chaîne de caractères qui sera affichée.
"""

# Exercice 6
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842294#overview
"""
006 - Hériter de la classe list

Dans cet exercice, vous devez faire hériter la classe ListeCustom de la classe list de Python.
On doit ainsi pouvoir utiliser la méthode append sur notre instance liste.
Vous devez ajouter le nombre 5 à l'instance liste.
"""


class ListeCutsom(list):
    pass


liste = ListeCutsom()
liste.append(5)

"""
EXPLICATIONS
Pour créer une notion d'héritage entre une classe et une autre (avec une relation 'parent' / 'enfant'), il faut indiquer
la classe dont on veut hériter dans les parenthèses lors de la définition de la classe:
    class ListeCustom(list):
On peut hériter des classes de base de Python comme str, list etc.

En héritant d'une classe, on accède automatiquement à toutes ses méthodes.

Cela nous permet donct d'utiliser la méthode append sur l'instance créée à partir de notre classe ListeCustom:
    liste.append(5)
    
POINTS IMPORTANTS A RETENIR
1. Pour hériter d'une classe, il faut indiquer cette classe dans les parenthèses lors de la définition de la classe.
"""

# Exercice 7
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842296#overview
"""
07 - Créer des instances employés

Dans ce exercice, vous disposez d'une classe Entreprise qui contient un attribut de la classe employes:
    class Entreprise:
        employtes = []
        
Cet attribut est un liste qui doit contenir les employés de l'entreprise.
Le but de cet exercice, est de créer des instances d'employés à partir de la liste de tuples employes:
    employes = [
                    ("Pierre", "Smith", "Responsable RH", 35000),
                    ("Julie", "Martin", "Développeur Python", 42000),
                    ("Eric", "Dupont", "Chef de projet", 50000),
                ]
Chaque instance d'employé créé à partir de la classe Employe doit être ajouté à l'attribut de classe employes de la
classe Entreprise.
L'attribut employes de la classe Entreprise, doit donc à la fin de l'exercice contenir trois instances de la classe 
Employe:
    >>> print(Entreprise.employes)
    [<__main__.Employe object at 0x102356860>,
     <__main__.Employe object at 0x102356898>,
     <__main__.Employe object at 0x1023568d0>]
"""

# class Entreprise:
#     employes = []
#
#
# class Employe:
#     def __init__(self, prenom, nom, position, salaire):
#         self.prenom = prenom
#         self.nom = nom
#         self.position = position
#         self.salaire = salaire
#
#
# employes = [
#     ("Pierre", "Smith", "Responsable RH", 35000),
#     ("Julie", "Martin", "Développeur Python", 42000),
#     ("Éric", "Dupont", "Chef de projet", 50000),
# ]
#
# for employe in employes:
#     Entreprise.employes.append(Employe(*employe))
#     print(Entreprise.employes)

"""
EXPLICATIONS

La première chose à faire pour pouvoir ajouter les employés contenus dans la liste employes est de boucler dessus pour
avoir accès à chaque tuple de cette liste.

Pour ce faire, on utilise une boucle for:
    for employ_data in employes:
    
A l'intérieur de la boucle, on crée ensuite une instance à partir de la classe Employe:
    employe = Employe(*employe_data)
    
Vous remarquerez que j'utilise l'astérisque, qui permet d'unpacker automatiquement le tuple dans les pramètres de la 
méthode __init__.

En effet, on aurait pu spécifier chaque argument séparément en récupérant les éléments dans le tuple mais c'est plus
long à ecrire:
    employe = Employe(employe_data[0], employe_data[1], employe_data[2], employe_data[3])

Ou encore en spécifiant le nom des paramètres, pour un code plus clair (mais définitivement plus long à écrire!):
    employe = Employe(prenom=employe_data[0],
                      nom=employe_data[1],
                      position=employe_data[2]
                      salaire=employe_data[3]
                      
Vu que les éléments dans le tuple sont dans le même ordre que les paramètres de la méthode __init__, on peut donc 
utiliser l'asterisque pour 'unpacker' ces éléments:
    employe = Employe(*employe_data)
Il ne reste plus qu'à ajouter l'instance récupérée dans la variable employe à l'attribut employes de la classe Entrepise 
    Entreprise.employes.append(employe)
    
POINTS IMPORTANTS A RETENIR
    1. Pour unpacker des éléments d'un tuple, on peut utiliser l'astérisque.
    2. Pour ajouter un élément à une liste, on utilise la méthode append.
    3. Pour boucler sur une liste, on utilise une boucle for.
"""

# Exercice 8
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842298#overview
"""
008 - Trouver les erreurs

Dans cet exercice, vous devez modifier le code de base pour qu'il ne retourne plus d'erreur et qu'il affiche les
coordonnées x, y et z de l'instance sphere avec des valeurs respectivement de 9, 2 et 5 (pour x, y et z)
Votre script doit donc afficher:
9
2
5

class Geometry:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


sphere = Geometry(9, 2, 5)
print(sphere.x)
print(sphere.y)
print(sphere.z)
"""

# class Geometry:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# sphere = Geometry(9, 2, 5)
# print(sphere.x)
# print(sphere.y)
# print(sphere.z)

"""
EXPLICATIONS
Premièrement, il faut corriger la méthode init à laquelle il manquait les deux tirets de bas avant et après le mot init.

Sans ces tirets du bas, la méthode n'est pas appelée automatiquement lors de l'instanciation de la classe et les 
attributs ne sont donc pas définis.
    class Geometry:
        def __init__(self, x=0, y=0):

Ensuite, il fallait modifier la variable pos_x qui n'existe pas et qui vous retournait une erreur de type NameError. A 
la place, il fallait donc mettre x, qui est le nom du paramètre défini dans la méthode __init__:
def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.z = z
    
Il fallait églement ajouter un pramètre à la méthode __init__ pour pouvoir récupérer la valeur 5 qui est envoyée au
paramètre z lors de la création de l'instance sphere.

On ajoute donc un paramètre z avec une valeur par défaut de 0 comme pour les autres coordonées et on assigne la valeur 
de z à l'attribut self.z:
    def __init__(self, x=0, y=0, z=0)
        self.x = x
        self.y = y
        self.z = z
        
Pour finir, il fallait rajouter les parenthèses lors de la céation de l'instance sphere et donner les valeurs 9, 2 et 5
respectivement aux paramètres x, y et z"
    sphere = Geometry(x=9, y=2, z=5)
    
POINTS IMPORTANT A RETENIR
1. La méthode spéciale qui est appelée lors de l'instanciation d'une classe, est la méthode __init__ et non pas init.
"""

# Exercice 9
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842300#overview
"""
009 - Créer un héritage entre deux classes

Dans cet exercice, vous devez faire hériter la classe Cube de la classe Shape.

Vous devez en pous vous assurer que la classe Cube hérite des attributs d'instance définis dans la classe Shape (les
attributs x et y del method __init__)

Comme un cube est en trois dimensions, vous devez en plus ajouter un attribut z qui n'existera que sur les instances de
la classe Cube et non pas sur la classe Shape.

Les trois attributs x, y et z doivent être définis à 0.
"""

# class Shape:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#
#
# class Cube(Shape):
#     def __init__(self):
#         super().__init__()
#         self.z = 0
#
#
# cube = Cube()
# print(cube.x)
# print(cube.y)
# print(cube.z)

"""
EXPLICATIONS
La première chose à faire était de rajouter le nom de la classe Shape à l'intérieur des parenthèses de la classe Cube
pour que Cube hérite de Shape.
    class Cube(Shape):
Pour que les attributs x e y soient accessibles sur les instances de Cube, il faut appeler la méthode __init__ de la 
classe parente (la classe Shape) dans laquelle ces attributs sont définis:
    class Cube(Shape)
        def __init__(self):
            super().__init__()
            
Depuis Python3, vous pouvez utiliser la fonction super en l'appelant directement sans lui passer aucun argument:
    super()

Pour finir, il fallait créer un attribut z uniquement sur les instances de la classe Cube.

Pour cela, on crée un attribut z à l'intérieur de la méthode __init__ de la classe Cube:
    def __init__(self):
        super().__init__()
        self.z = 0
        
Il ne fallait pas ajouter l'attribut à la suite des atttributs x et y de la classe Shape, car on ne voulait ajouter cet
attribut que pour les instances de la classe Cube.

POINTS IMPORTANTS A RETENIR
1. Pour appeler une méthode de la classe parent, on peut utiliser la fonction super.
"""

# exercice 10
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842302#overview
"""
010- Modifier un attribut

Dans cet exercice, vous devez créer une méthode changer_prix qui permette de modifier le prix de l'instance 
harry_potter:
    harry_potter.changer_prix(prix=14.99)

Le prix de l'instance harry_potter doit être de 14.99 à la fin du script.
Le prix la classe Livre doit lui rester à 9.99.
"""

# class Livre:
#     prix = 9.99
#
#     def __init__(self, prix):
#         self.prix = prix
#
#     def changer_prix(self, prix):
#         self.prix = prix
#
#
# print(Livre.prix)
#
# harry_potter = Livre(19.99)
# print(harry_potter.prix)
#
# harry_potter.changer_prix(prix=14.99)
# print(harry_potter.prix)

"""
EXPLICATIONS
Pour créer une méthode, il faut utliser la même syntaxe que pour une fonction. La seule chose à ne pas oublier est de
mettre self en premier paramètre.

self correspond à l'instance que nous manipulons, dans ce cas-ci harry_potter.

Quand nous appelons la méthode changer_prix sur l'instance harry_potter, Python passe en fait par la classe.

Les deux lignes de codes suivantes sont les mêmes et la deuxième façon de faire vous montre bien que l'instance est
envoyé en argument au paramètre self de la méthode changer_prix:
    harry_potter.changer_prix(prix=14.99)
    En arrière-plan, Python opère comme ceci, d'où la nécéssité de mettre self en premier paramètre pour récupérer
    l'instance.

La méthode changer_prix doit également accepter un deuxième paramètre qui va récupérer le nouveau prix que l'on souhaite
attribuer à l'attribut prix de l'instance:

On assigne ensuite la valeur récupérée par ce paramètre prix à l'attribut d'instance self.prix:
    def changer_prix(self, prix):
        self.prix = prix
        
On a donc à la fin du script l'attribut Livre.prix qui reste inchangé à 9.99.

La valeur de harry_potter.prix elle a cependant été modifiée par l'appel de la méthode changer_prix:
    harry_potter.changer_prix(prix=14.99)
    
POINTS IMPORTANTS A RETENIR
1. Pour créer une méthode, on utilise la même syntaxe que pour créer une fonction, avec l'instruction def.
2. il ne faut pas oublier de mettre le paramètre self en premier paramètre de la méthode pour récupérer l'instance.
"""

# exercice 11
#

"""
011 - Trouver les erreurs

Dans cet exercice, vous devez corriger le script pour que la méthode set_position fonctionne correctement et modifie les
attributs x, y et z de l'instance cube.
Votre script doit donc redéfinir les valeurs de ces trois attributs qui devront être égaux à 1 pour x, 2 pour y et 3
pour z.
"""

# class Cube:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def set_position(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# cube = Cube()
# cube.set_position(1, 2, 3)

"""
EXPLICATIONS
Le premier élément qu'il fallait corriger était la définition de la méthode set_position.

Dans le script de départ, cette méthode ne contenait pas le paramètre self en première position, ce qui n'est pas 
possible pour une fonction définie à l'intérieur d'une classe (à moins d'utiliser le décorateur staticmethod):
    def set_position(self, x, y, z):
Ensuite, il fallait assigner les valeurs de x, y et z à l'instance, et donc à self à l'intérieur de la méthode:
    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        
POINTS IMPORTANTS A RETENIR
1. Une fonction contenue à l'intérieur d'une classe doit obligatoirement contenir un paramètre pour récupérer 
l'instance. Par convention, on utilise le nom self pour ce premier paramètre.

2. Pour récupérer ou modifier l'attribut d'une instance, il faut donc accéder à cet attribut via le paramètre self. Donc
pour assigner une valeur à l'attribut x de l'instance à l'intérieur d'une méthode, il faut le faire self.x = valeur.     
"""

# exercice 12
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842306#overview
"""
012 - Ajouter les self

Dans cet exercices, vous devez corriger le code pour qu'il fonctionne.
La seule chose que vous devez rajouter, c'est le fameux self, qui pose beaucoup de problèmes au débutants en 
programmation orientée objet. C'est le seul mot que vous devez ajouter.
Le script final doit contenir self à 6 endroits différents.
x, y et z doivent appartenir à l'instance mon_cube.
A la fin du script, la valeur de l'attribut x de l'instance mon_cube doit être égale à 6 (pour valider l'exercice, la
méthode move_x doit donc fonctionner et vous ne devez pas enlever la dernière ligne du script).
"""

# class Cube:
#     def __init__(self, x=5, y=2, z=7):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def move_x(self):
#         self.x += 1
#         return self.x
#
#
# mon_cube = Cube()
# print(mon_cube.move_x())

"""
EXPLICATIONS
La première chose à laquelle il faut penser quand on crée des méthodes, c'est de toujours ajouter self comme premier 
paramètre.
Il fallait donc ajouter self à la méthode __init__ et à la méthode move_x:
    class Cube:
        def __init__(self, x=5, y=2, z=7):
            x = x
            y = y
            z = z
            
        def move_x(self):
            x += 1
            
    mon_cube = Cube()
    mon_cube.move_x()
    
Enfin, il fallait associer préfixer chaque variable par self. self représent l'instance (donc mon_cube dans ce cas-ci).

On peut ainsi accéder à self.x à l'intérieur de la méthode move_x et incrémenter sa valeur de 1:

    class Cube:
        def __init__(self, x=5, y=2, z=7):
            self.x = x
            self.y = y
            self.z = z
        
        def move_x(self):
            self.x += 1
            
POINTS IMPORTANTS A RETENIR
1. self représente l'instance, dans ce cas-ci l'instance mon_cube, créée à partir de la classe Cube.
2. Les méthodes d'une classe doivent posséder au moins un paramètre, self, pour récupérer l'instance.
"""

# exercice 13
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842310#overview
"""
0-13 Changer un attribut avec une méthode 

Dans cet exercice, vous devez créer une méthode changer_prix qui permet de changer le prix de la voiture. Vous
devez également créer la méthode __init__ afin de créer les attributs d'instance maque et prix.
La méthode changer_prix ne doit fonctionner qu'avec un nombre entier.
L'utilisateur ne doit donc pas être en mesure de changer le prix pour autre chose qu'un nombre entier.
Le code voiture.changer_prix(prix="bonjour") ou voiture.changer_prix(prix=25000.5) ne doivent donc pas modifier la 
valeur de l'attribut voiture.prix.
Pour valider l'exercice, l'attribut prix doit être mis à jour et être égal à 35,000 à la fin du script.
"""

# class Voiture:
#     def __init__(self, marque, prix):
#         self.marque = marque
#         self.prix = prix
#
#     def changer_prix(self, prix):
#         self.nouveau_prix = prix
#         if not isinstance(self.nouveau_prix, int):
#             print("vous devez fournir un entier !")
#         else:
#             self.prix = prix
#         return self.prix
#
#
# voiture = Voiture(marque="Mazda", prix=30000)
# print(voiture.changer_prix(35000))

"""
EXPLICATIONS
La première chose à faire était de créer la méthode __init__ afind de pouvoir initialiser les attributs marque et prix
sur l'instance:
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
            
Vous devriez ensuite créer une méthode changer_prix qui permette de modifier le prix:
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
            
        def changer_prix(self, prix):
            self.prix = prix
            
Jusque-là rien de bien compliqué.

La dernière chose à faire était de modifier l'attribut prix, seulement si celui-ci était un nombre entier.

Pour cela, on utlise la fonction isinstance qui permet de vérifier si une variable est d'un certyin type (on pourrait
également utiliser la fonction type, mais isinstance a l'avantage de gérer l'héritage. Je préfère donc l'utiliser que
la fonction type):
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
            
        def changer_prix(self, prix):
            if isinstance(prix, int):
                self.prix = prix
                
Avec if isinstance(prix, int): on vérifie que la valeur passée en argument au parameètre prix est bien de type int 
(nombre entier).
Si c'est le cas, on met à jour l'attribut prix de l'instance:
    self.prix = prix
    
POINTS IMPORTANTS A RETENIR
1. Pour vérifier si une variable est d'un certain type, on peut utiliser la fonction isinstance.
2. Pour modifier un attribut d'instance on fait une assignation comme si on modifiait une variable: self.nom_attribut = 
   valeur
"""

# exercice 14
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842312#overview
"""
0-14 Eviter la répétition avec l'héritage

Dans cet exercice, vous devez simplifier le code grâce l'héritage.
En effet, dans l'état actuel du script, on répète plusieurs fois les informations de nom et prenom de nos personnages.
Ca fonctionne, mais ce n'est pas très efficace.
Vous devez donc créer une classe Personnage dont vont hériter les classes Magicien, Gobelin et Chevalier.
Cette classe Personnage devra définir les attributs nom et prenom qui sont communs aux trois classes.
Vous ne devez pas toucher à l'attribut puissance des classes Magicien, Gobelin et Chevalier. Ces trois classes devront
donc avoir un attribut puissance égal respectivement à 80, 20, 70.
"""

# class Personnage:
#     def __init__(self, prenom, nom):
#         self.prenom = prenom
#         self.nom = nom
#
#
# class Magicien(Personnage):
#     def __init__(self, prenom, nom):
#         super().__init__(prenom, nom)
#         self.puissance = 80
#
#
# class Gobelin(Personnage):
#     def __init__(self, prenom, nom):
#         super().__init__(prenom, nom)
#         self.puissance = 20
#
#
# class Chevalier(Personnage):
#     def __init__(self, prenom, nom):
#         super().__init__(prenom, nom)
#         self.puissance = 70
#
#
# gandalf = Personnage("Gandalf", "LeGris")
# print(f"prenom: {gandalf.prenom}, nom: {gandalf.nom}")
#
# isidor = Magicien(prenom="Isidor", nom="LeVert")
# print(f"prenom: {isidor.prenom}, nom: {isidor.nom}, puissance: {isidor.puissance}")
#
# mexus = Gobelin(prenom="Mexus", nom="LeMechant")
# print(f"prenom: {mexus.prenom}, nom: {mexus.nom}, puissance: {mexus.puissance}")

"""
EXPLICATIONS
Cet exercice comportait beaucoup de tests à réussir mais il était finalement assez simple à réaliser si vous maîtriser
le concept d'héritage.

Pour éviter la répétition des attributs prenom et nom dans les trois classes, il fallait créer une classe Personnage qui
définissait ces deux attributs:
    class Personnage:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            
Cela nous permet de créer un personnage de la sorte:
    perso = Personnage(prenom='Gandalf', nom='LeGris')

Dans notre cas, on ne veut pas créer directement une personnage, mais utiliser cette classe comme classe 'parente' de 
nos trois classes Magicien, Gobelin et Chevalier. Il suffisait donc d'indiquer cette classe dans la définition de nos 
trois classes:
    class Personnage:
        def __init__(self, prenom, nom)
            self.prenom = prenom
            self.nom = nom
            
    class Magicien(Personnage):
        def __init__(self, prenom, nom)
            self.prenom = prenom
            self.nom = nom
            self.puissance = puissance
            
    class Gobelin(Personnage):
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            self.puissance = 20
            
    class Chevalier(Personnage)"
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            self.puissance = 70
            
C'est mieux, mais on répète encore trois fois la déclaration des attributs prenom et nom dans chacune des classes.

Pour remédier à cette répétition, il faut appeler la méthode __init__ de la classe dont on hérite.

Pour cela, le plus simple est d'utiliser la fonction super et de passer les valeurs de nom et prenom à la méthode 
__init__:
    class Magicien(Personnage):
        def __init__(self, prenom, nom)
            super().__init__(prenom=prenom, nom=nom)
            self.puissance = 80
            
On peut ainsi créer un magicien comme ceci:
    gandalf = Magicien(prenom='Gandalf', nom='LeGris')
    
La fonction super va appeler la méthode __init__ de la classe Personnage et passer en argument "Gandalf" et "LeGris" aux
paramètres prenom et nom définit dans la méthode __init__ del la classe Personnage.

On répète la même opération pour les autres classes et cela permet d'évitter la répétition.

L'attribut puissance quand à lui est différent pour chaque instance, on peut donc le laisser dans chaque classe.

On aurait pu également le définir dans la classe Personnage et passer la valeur désirée lors de l'appel de la méthode 
__init__ comme ceci:
    class Personnage:
        def __init__(self, prenom, nom, puissance)
            self.prenom = prenom
            self.nom = nom
            self.puissance = puissance
            
    class Magicien(Personnage):
        def __init__(self, prenom, nom)
            super().__init__(prenom=prenom, nom=nom, puissance=80)
            
    class Gobelin(Personnage):
        def __init__(self, prenom, nom)
            super().__init__(prenom=prenom, nom=nom, puissance=20)
    
    class Chevalier(Personnage):
        def __init__(self, prenom, nom)
            super().__init__(prenom=prenom, nom=nom, puissance=70)
            
POINTS IMPORTANTS A RETENIR
1. Pour hériter d'une classe, on indique le nom de la classe à l'intérieur des parenthèses lors de la définition de la 
classe.

2. Pour appeler un méthode de la classe dont on hérite, on peut utliser la fonction super.
"""

# exercice 15
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842314#overview
"""
015 - Rendre une méthode privée

La classe MachineACafe permet de faire du café et dispose pour ce faire de trois méthodes:
1. chauffe_eau
2. moud_cafe
3. fait_du_cafe

Dans le code de départ, ces trois méthodes sont accessibles directement par l'instance.
Cependant, on aimerait restreindre l'accès aux méthodes chauffe_eau et mou_cafe qui n'ont pas vocation à être utilisée 
directement par l'utlisisateur mais uniquement par la méthode fait_du_cafe.
Vous devez donc rendre ces méthodes privées et adapter le code de la méthode fait_du_cafe pour utiliser ces méthodes 
privées.
"""

# class MachineACafe:
#     def __init__(self):
#         self.temperature_eau = 0
#
#     def __chauffe_eau(self):
#         self.temperature_eau = 100
#         print("L'eau est chaude.")
#
#     def __moud_cafe(self):
#         print("Café moulu avec succès.")
#
#     def fait_du_cafe(self):
#         self.__moud_cafe()
#         self.__chauffe_eau()
#         print("Le café est prêt")
#
#
# machine = MachineACafe()
# machine.fait_du_cafe()

"""
EXPLICATIONS
Rien de compliqué dans cet exercice si vous connaissiez les méthodes privées. 
Pour valider le code, il suffisait de trnaformer les méthodes chauffe_eau et moud_cafe en méthodes privées.

Pour ce faire, il suffit d'ajouter deux tirets du bas avant le nom des méthodes.

Il ne fallait pas oublier de modifier l'appel à ces méthodes dans la méthode fait_du_cafe pour appeler les méthodes
privées:
    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le café est prêt")
        
En rendant ces méthodes privées, on ne peut plus les appeler directement depuis l'instance machine:
    >>> machine.__moud_cafe()
    AtrributeError: 'MachineCafe' ojbect has no attribute '__moud_cafe'
    
POINTS IMPORTANTS A RETENIR
1. Pour rendre une méthode privée, il suffit de la précéder de deux tirets du bas.
"""

# exercice 16
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842316#overview
"""
016 - Trouver les erreurs

Le code de départ de cet exercice comporte plusieurs erreurs.
A vous de les identif et les corriger pour que le script fonctionne.
def Voiture:
    class _init_(self):
        marque = "Mazda"
        couleur = "Rouge"

    def recuperer_couleur():
        return couleur


mazda_rouge = Voiture
couleur = mazda_rouge.recuperer_couleur()
"""

# class Voiture:
#     def __init__(self):
#         self.marque = "Mazda"
#         self.couleur = "Rouge"
#
#     def recuperer_couleur(self):
#         couleur = self.couleur
#         return couleur
#
#
# mazda_rouge = Voiture()
# couleur = mazda_rouge.recuperer_couleur()
# print(couleur)

"""
EXPLICATIONS
Beaucoup d'erreurs disséminées dans ce script! Bravo si vous les avez toutes trouvées.

Premièrement, il fallait remplacer def Voiture par Class Voiture.

L'instruction def sert à déclarer des fonctions. Pour créer une classe, on utilise l'instruction class.
    class Voiture:

A l'inverse, à la deuxième ligne, il fallait utiliser def au lieu de class pour défirnir la méthode __init__:

Il manquait également un tiret du bas avant et après lee nom de la méthode init. En effet, il faut deux tirets du bas 
avant et après le nom de la méthode init. On avait donc deux erreurs sur la même ligne!
    def __init__(self):
Ensuite, il fallait ajouter self devant le nom des attributs marque et couleur:
    self.marque = "Mazda"
    self.couleur = "Rouge"
    
Sans le self ces deux noms n'étaient que des variables définies à l'intérieur de la méthode __init__.

Dans notre cas, on voulait créer des attributs d'instance, il fallait donc ajouter le self.

Il manquait également un self dans la méthode recuperer_couleur:
    def recuperer_couleur(self):

il ne faut jamais oublier de mettre self en premier paramètre pour pouvoir récupé l'instance.
La seule façon de faire qui permette d'omettre le self est d'utiliser le décorateur @staticmethod pour rendre la méthode
statique.

A l'intérieur de la méthode recuperer_couleur, il fallait là encore ajouter un self pour retourner l'attribut couleur de
la voiture:
    def recuperer_couleur():
        return self.couleur
        
Pour finir, il manquait les parenthèse lors de la création de l'instance mazda_rouge.
    mazda_rouge = Voiture()
    
Sans ce paramètres, on fait juste associer le nom mazda_rouge à la classe Voiture.

Cela n'a pas grand intérêt , à part d'utiliser ce nom pour créer une instance, par exemple cela permettrait de faire:
    voiture = mazda_rouge()
    
Mais nous ce que l'on veut dans ce cas-ci c'est bien créer une instance de Voiture que l'on retourne dans le nom
mazda_rouge. Il fallait donc ajouter les parenthèses après Voiture.

POINTS IMPORTANTS A RETENIR
1. Pour créer une classe, on utilise l'instruction class.
2. Pour définir une méthode, on utilise def.
3. Pour initialiser une instance, on utilise la méthode 'magique' __init__.
4. Pour définir un attribut d'instance, on doit le préfixer du mot self.
5. Pour définir une méthode, on doit obligatoirement mettre en premier paramètre self (à moins d'utiliser le décorateur
   @staticmethod pour créer une méthode statique).
6. Pour créer une instance à partir d'une classe, on utilise le nom de la classe suivie de parenthèses.
"""

# exercice 17
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842318#overview
"""
017 - Créer une métode statique

Le but de cet exercice est de transformer la méthode chante_pour afin de la rendre statique.
La méthode doit permettre de chanter Joyeux Anniversaire pour une personne définie par l'argument envoyé au paramètre 
prenom. 

Dans ce cas-c, le script doit donc afficher Joyeux Anniversaire pour Paul(la méthode chante_pour ne doit pas afficher le
text de la chanson mais juste le retourner).

Vous devez donc rendre la méthode statique et la modifier pour qu'elle affiche le texte contenu dans l'attribut paroles
de la classe Chanson, adapté pour le prénom Paul.
"""

# class Chanson:
#     paroles = '''Joyeux anniversaire,
#     Joyeux anniversaire,
#     Joyeux anniversaire {prenom},
#     Joyeux anniversaire.'''
#
#     @staticmethod
#     def chante_pour(prenom):
#         return Chanson.paroles.format(prenom=prenom)
#
#
# print(Chanson.chante_pour(prenom="Paul"))

"""
EXPLICATIONS
Pour rendre une méthode statique et ainsi pouvoir l'utiliser directement depuis la classe, sans avoir besoin de créer 
d'instance, il faut utiliser le décorateur @staticmethod:
    @staticmethod
    def chante_pour():

Cela nous permet d'appeler directement la méthode chante_pour depuis la classe Chanson:
    Chanson.chante_pour()
    
Il suffisait ensuite de permettre l'envoi d'un argument prenom et d'afficher les paroles de la chanson contenues dans
l'attribut paroles de la classe Chanson:
    @staticmethod
    def chante_pour(prenom)
        return Chanson.paroles.format(prenom=prenom)
        
Dans ce cas-ci, vu qu'on a une méthodes statiques, pas besoin de mettre le paramè self, vu qu'on n'a pas besoin 
d'instance.

C'est l'avabtage des méthodes statiques, de pouvoir travailler directement à partir de la classe. Il suffisait donc 
d'ajouter un paramètre prenom.

On retournait ensuite la chanson adaptée pour le prénom passé en argument grâce la méthode format:
    Chanson.paroles.format(prenom=prenom)
    
POINTS IMPORTANTS A RETENIR
1. Pour définir une méthode statique, on utilise le décorateur @staticmethod.
2. Pour insérer la valeur d'une variable à l'intérieur d'une chaîne de caractères on peut l'utiliser la méthode format.
"""

# exercice 18
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842320#overview
"""
018 - Supprimer une instance

Dans cet exercice, nous voulons récupérer dans une liste etudiants_partis les étudiants qui ne sont plus présents dans
notre établissement scolaire.
Pour cela, nous souhaitons permettre la suppression d'une instance de la classe Etudiant.
Lors de la suppression de l'instance, le prénom et le nom de l'étudiant en question doivent être ajoutés à la liste
etudiants_partis. Dans ce cas-ci, la liste etudiants_partis doit donc à la fin du script être égale à ["Marc Tremblay"].
"""
# etudiants_partis = []
#
#
# class Etudiant:
#     def __init__(self, prenom, nom):
#         self.prenom = prenom
#         self.nom = nom
#
#     def __del__(self):
#         etudiants_partis.append(f'{self.prenom} {self.nom}')
#         del self
#
#
# john = Etudiant("John", "Smith")
# julie = Etudiant("Julien", "Martin")
# marc = Etudiant("Marc", "Tremblay")
#
# del marc
# print(john.nom)
# print(julie.nom)
# # print(marc.nom)
# print(etudiants_partis)

"""
EXPLICATIONS
Pour éxecuter du code lors de la suppression d'une instance avec l'instruction del, il faut utiliser la méthode __del__.
A l'intérieur de cette méthode, nous ajoutons tout simplement le prénom et le nom de l'étudiant qui a été suprrimé, avec
les f-string:
    def __del__(self):
        etudiants_partis.append(f'{self.prenom} {self.nom}')
        
A chaque fois qu'on supprime une instance de la classe Etudiant, on ajoute ainsi le prénom et le nom de l'étudiant 
supprimé à la liste tudiants_partis.

POINTS IMPORTANTS A RETENIR
1. Pour exécuter une action quand on supprime une instance, il faut impémenter la méthode __del__.
"""

# exercice 19
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842322#overview
"""
019 - Créer un gestionnaire de compte

Cet exercice n'est pas extrêmement compliqué si ce n'est que vous partez cette fois-ci de 0 !
Dans cet exercice vous devez créer une classe compte qui permette de déposer de l'argent de votre compte bancaire.
Les instances créées grâce à la classe compte doivent posséder trois attributs:
1. nom
2. numero
3. balance
Cela permet ainsi de créer un compte pour John, avec un numéro de compte de 12345 et un dépot initial de 20,000 euros.
    compte_john = Compte(nom="John", numero="12345", balance=20000)
Nous déposons ensuite 3,000 euros supplémentaires grâce é la méthode deposer.
"""

# class Compte:
#     montant = 0
#
#     def __init__(self, nom, numero, balance):
#         self.nom = nom
#         self.numero = numero
#         self.balance = balance
#
#     def deposer(self, montant):
#         self.balance += montant
#         return self.balance
#
#     def retirer(self, montant):
#         self.balance -= montant
#         return self.balance
#
#
# compte_john = Compte(nom="John", numero="12345", balance=20000)
# print(
#     f'compte au nom de: {compte_john.nom}, numéro de compte: {compte_john.numero}, balance: {compte_john.balance} euros')
# print(f'deposer: {compte_john.deposer(3000)}')
# print(f'retirer: {compte_john.retirer(montant=200)}')

"""
EXPLICATIONS
La première chose à faire était de créer la classe Compte ainsi que sa méthode __init__ afin de pouvoir créer une 
insance avec les bons attributs:
    class Compte:
        def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        
Cela nous permet ainsi de créer l'instance compte_john:
    compte_john = Compte(nom="John", numero"12345", balance=20000)

Il fallait ensuite créer deux méthodes deposer et retirer qui nous permette de modifier l'attribut balance:
    def deposer(self, montant):
        self.balance += montant
    
    def retirer(self, montant):
        self.balance -= montant
        
On utilise ici le raccourci += et -= pour rapidement incrémenter et décrémenter la valeur de l'attribut balance du 
montant passé en argument au paramètre montant.

POINTS IMPORTANTS A RETENIR
1. Pour créer une classe on utilise l'instruction class.
2. Pour initialiser une instance, on utilise la méthode __init__.
3. Pour rapidement incrémenter ou décrémenter une variable, on peut utiliser += ou -=     
"""

# exercice 20
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842324#overview
"""
020 - Surcharger une méthode

Dans cet exercice, vous devez implémenter la méthode pour les classes Animal, Chien et Chat.
Dans le cas de la classe Animal, la méthode parle doit lever une erreur de type NotImplementedError avec le message
d'erreur "Je ne sais pas quoi dire...".
Dans le cas de la classe Chien, vous devez surcharger la méthode parle pour qu'elle retourne la chaîne de caractères 
"Woof!". Pour la classe chat, la méthode parle doit retourner la chaîne de caractère "Miaou!".
"""

# class Animal:
#     def __init__(self, nom):
#         self.nom = nom
#
#     def parle(self):
#         raise NotImplementedError("Je ne sais pas quoi dire...")
#
#
# class Chien(Animal):
#     def parle(self):
#         return f"le chien {self.nom} fait Woof!"
#
#
# class Chat(Animal):
#     def parle(self):
#         return f"le chat {self.nom} fait Miaou!"
#
#
# a = Animal("Patrick")
# chat = Chat("Titi")
# chien = Chien("Max")
# #
# # print(a.parle())
# print(chat.parle())
# print(chien.parle())

"""
EXPLICATIONS
Pour réussir cet exercice, il fallait implémenter la méthode parle pour les classes Animal, Chien et Chat.

Pour la première classe, on devait lever une erreur, Pour ce faire, on utilise l'instruction raise suivie du nom de 
l'erreur que l'on souhaite lever ainsi que le message à afficher:
    class Animal:
        def __init__(self, nom)
            self.nom = nom
            
        def parle(self):
            raise NotImplementedError("Je ne sais pas quoi dire...")
            
Il suffisait ensuite d'implémenter cette même méthode sur les deux autres classes, en retournant la bonne chaîne de 
caractère selon l'animal:

    class Chien(Animal)
        def parle(self):
            return "Woof!"
            
    class Chat(Animal)
        def parle(self):
            return "Miaou!"
            
POINTS IMPORTANTS A RETENIR
1. Pour lever une erreur, on utilise l'instruction raise.
2. Pour surcharger une méthode, il suffit de la ré-implémenter dans la classe fille.
"""

# exercice 21
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842326#overview
"""
021 - Incrémenter un attribut

Dans cet exercice, vous devez assigner un indentifiant unique à chaque instance d'étudiant et ajouter les instances dans
l'attribut de classe repertoire.
Chaque instance créée à partir de la classe Etudiant doit posséder un attribut uid correspondant à son numéro 
d'étudiant.
John devra donc avoir comme identifiant unique 1, julie devra avoir l'identifiant 2 et marc l'identifiant 3.
Cet attribut doit être généré automatiquement. Si on crée un autre étudiant, celui-ci doit avoir un identifiant unique 
égale à 4.
L'attribut repertoire de la classe Etudiant doit contenir toutes les instances d'étudiants créées.
"""

# class Etudiant:
#     repertoire = []
#     uid = 1
#
#     def __init__(self, prenom, nom):
#         self.nom = prenom
#         self.prenom = nom
#         self.uid = Etudiant.uid
#         Etudiant.uid += 1
#         Etudiant.repertoire.append(self)
#
#
# john = Etudiant("John", "Smith")
# Elise = Etudiant("Julie", "Martin")
# Marc = Etudiant("Marc", "Tremblay")
# print(f"nombre d'instance de l'objet créé {Etudiant.uid}")
# print(Etudiant.repertoire)
# # julie = Etudiant("Julie", "Martin")
# # marc = Etudiant("Marc", "Tremblay")
# # print(Etudiant.repertoire)
# print(Marc.uid)

"""
EXPLICATIONS
Cet exercice n'était pas très compliqué mais il fallait tout de même réfléchir un peu pour trouver un moyen de générer
automatiquement un identifiant unique.

Pour cela, on se set de l'attribut repertoire de la classe Etudiant auquel on ajoute chaque instance créée.

En utilisant la fonction len, on peut récupérer la longueut de la liste et s'en servir pour générer l'identifiant 
unique:
    self.uid = len(Etudiant.repertoire) + 1

On ajoute 1 à la longueur de la liste car on ajoute l'étudiant à la ligne d'après.

On pourrait également inverser les deux lignes (ajouter d'abord l'instance) et ainsi éviter d'avoir à ajouter 1. Cela
revient au même.

Une fois l'identifiant unique généré, on ajoute l'instance (donc self) dans la liste avec la méthode append, tout 
simplement:
    Etudiant.repertoire.append(self)
    
POINT IMPORTANTA A RETENIR
1. Pour accéder à un attribut de classe, on utilise directement la classe (MaClasse.mon_attribut).
2. Pour récupérer la longueur d'une liste, on utilise la fonction len.

"""

# exercice 22
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842328#overview
"""
022 - Générer un attribut aléatoire

Dans cet exercice, vous devez implémenter une méthode virement qui permette d'ajouter ou enlever de l'argent à la 
balance du compte. On désire générer un numéro unique pour chaque virement evvectué et le sauvegarder dans le 
dictionnaire virements de l'instance. Le numéro unique généré doit contenir 15 caractères et peut être composé de 
lettres (minuscules ou majuscules) et de chiffres de 0 à 9. Dans le cas de cet exercice, john effectue un virement de 
5,000 euros.
Le dictionnaire john.virements devra donc ressembler à:
    >>> john.virements
    {'vQLONfx81hrIsDS' : 5000}
    
Bien sûr, la clé du virement étant aléatoire, votre scipt retournera un résultat pour le numéro unique du virement.
La balance du compte de John devra être égale à 25,000 euros(20, 000 euros de départ plus des 5, 000 euros du virement).
"""
# import string
# import random
#
# length_of_strings = 15
#
#
# class Compte:
#
#     def __init__(self, nom, numero, balance):
#         self.nom = nom
#         self.numero = numero
#         self.balance = balance
#         self.virements = {}
#
#     def virement(self, montant):
#         self.balance += montant
#         uuid = "".join(random.choice(string.ascii_letters + string.digits) for _ in
#                        range(length_of_strings))
#         self.virements[uuid] = montant
#         return uuid, self.balance
#
#
# john = Compte(nom="John Smith", numero="123456", balance=20000)
# print(john.virement(5000))
# # john.virement(montant=5000)

"""
EXPLICATIONS
Premièrement, on devait créer une méthode virement qui permette de virer un certain montant d'argent dans le compte.

On devait donc pouvoir récupérer ce montant dans un paramètre que l'on appelle tout bonnement montant. On utilise la 
valeur envoyée à ce paramètre pour modifier la balance du compte:
    def virement(self, montant)
        self.balance += montant
        
On devait ensuite générer un identifiant unique aléatoire composé de 15 lettres et chiffres.

Pour cela, on fait appelle à deux modules: le module random et le module string

Le module string contient plusieurs constantes bien pratiques pour ce genre de cas.

Das le cadre de cet exercice, on utilise la constante string.ascii_letters qui contient toutes les lettres de l'alphabet
en majuscule et minuscule:
    >>> import string
    >>>> string.ascii_letters
    
De la même façon, la constante string.digits nous retourne tous les chiffres de 0 à 9:
    >>> import string
    >>> string.digits
    
Chacune de ces constantes nous retournes une chaîne de caractères qui contient tous les caractères demandés.

On peut donc additionner ces deux chaînes de caractères avec le symbole d'addition:
    >>> string.digits + string.ascii_letters
    
On a donc ainsi tous les caractères dans lesquels nous souhaitons 'piocher' pour générer notre identifiant aléatoire.

Pour sélectionner un nombre aléatoire de caractères dans une chaîne de caractère, on utilise la fonction sample du 
module random:
    >>> random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 15)
    
Cette fois-ci, on se retourve avec un liste. Il nous faut donc joindre les éléments de cette liste en chaîne de 
caractères.

Pour ce faire on utilise la méthode join sur un chaîne de caractères vide, ce qui donne la ligne de code suivante qui 
nous permet de générer un identifiant unique complet de 15 caractères:
    uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))

Il ne nous reste plus qu'à ajouter ce virement dans notre dictionnaire
    self.virements[uuid] = montant
    
POINTS IMPORATANTS A RETENIR
1. Pour récupérer toutes les lettres de l'alphabet et tous les chiffres on utilise le module string.

2. Pour récupére aléatoirement des caractères dans une chaîne de caractères, on utilise la fonction sample du module
random.
"""

"""
Résumé de la section

1. Méthode privée
Cette methode (ci-dessous) ne sera pas accessible depuis mon instance:
    class Livre:
        def __changer_prix(self):
            print("Changer Prix")
            
        def __inflation(self):  <-- ici ca marche on peut l'appeler a l'interieur de la classe ou elle est definie
            self.__changer_prix()
            
harry_potter = Livre()
harry_potter.__changer_prix()
>> AttributeError: 'Livre' object has no attribute '__changer_prix'
    
    
2. Methode statique
    class Maths:
    
        @staticmethod
        def addition(a, b):
            return a + b
            
Maths.addition(5, 10)

On utilise les méthodes statique pour faire du rangement, par exemple ici dans Maths on peut ranger: addition, 
soustraction, multiplication et division. De plus avec la methode statique pas besoin de creer une instance on peut donc
appeler la class.methode donc dans le cas ci-dessus Math.addition(5, 10)
"""

# exercice 23
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842330#overview
"""
0-23 Enpêcher la modification d'un attribut

Le but de cet exercice est d'empêcher la modification de l'attribut numero de l'instance john.
Je ne vous en dis pas plus, à vous de trouver un moyen d'empêcher le numéro modifié.
Si on essaie de modifier l'attribut, le script doit retourner une erreur de type AttributeError.
"""

# class Compte:
#     def __init__(self, nom, numero, balance):
#         self.nom = nom
#         self._numero = numero
#         self.balance = balance
#
#     @property
#     def numero(self):
#         return self._numero
#
#     @numero.setter
#     def numero(self, value):
#         raise AttributeError("Vous ne pouvez pas modifier le numéro du compte.")
#
#
# john = Compte(nom="John Smith", numero="123456", balance=20000)
# print(john.numero)
# john.numero = "64321"

# exercice 24
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842332#overview
"""
0-24 Calclue l'air d'un rectangle avec un ContextManager

Dans cet exercice, vous allez devoir implémenter ce qu'on appelle un contexmanager.
On doit en effet pouvoir utiliser notre classe Rectangle avec l'instruction with afin de permettre le calcul de l'aire
d'un rectangle:
    with Rectangle(6, 12) as r:
        r.calcul_aire()

Le code suivant devra retourner les deux phrases suivantes:
    L'aire d'un rectangle de 6m par 12m est de:
    72m2
    
Vous devez donc implémenter le contexmanager ainsi que la méthode calcul_aire qui permette de calculer l'aire du
rectangle (petit rappel: pour calculer l'aire d'un rectangle, il suffit de multiplier sa largeur par sa longueur).
"""

# class Rectangle:
#     def __init__(self, longueur, largeur):
#         self.longueur = longueur
#         self.largeur = largeur
#
#     def __enter__(self):
#         print("L'aire d'un rectangle de {}m par {}m est de:".format(self.longueur, self.largeur))
#         return self
#
#     def __exit__(self, exception_type, exception_value, callback):
#         print("{}m2".format(self.calcul_aire()))
#
#     def calcul_aire(self):
#         return self.longueur * self.largeur
#
#
# with Rectangle(6, 12) as r:
#     print(r.calcul_aire())

"""
EXPLICATIONS
La première chose à faire était dimplémenter la méthode calcul_aire:
    def calcul_aire(self):
        self.aire = self.longueur * self.largeur
        
Cette méthode est très simple et retourn l'aire du rectangle dans un attribut aire.

Maintanant, pour pouvoir utiliser l'instruction with, il fallait implémenter un contextmanager.

Pour ce faire, on utilise les deux méthodes spéciales __enter__ et __exit__.

La méthode __enter__ est appelée au début du contexte et la méthode __exit__ à sa sortie.

Pour la méthode __enter__, on voulait juste annoncer le fait qu'on s'apprêter à calculer l'aire du rectangle. Un simple 
print suffisait donc:
    def __enter__(self):
        print("Laire d'un rectangle de {}m par {}m est de".format{self.longueur, self largeur))
        return self
        
Il ne faut cependant pas oublier de retourner self puisque c'est la valeur que l'on retourne dans la méthode __enter__
qui sera récupérée dans notre cas par la variable r lors de l'instruction with:
    with Rectangle(6, 12) as r:
        r.calcul_aire()
        
A l'intérieur du bloc d'instruction, on appelle la méthode calcul_aire afin de récupérer le résultat du calcul dans
l'attribut aire.

On peut ensuite afficher ce résultat à la sortie du contetmanager, dans la méthode __exit__:
    def __exit__(self, exception_type, exception_value, callback)
        print("{}m2".format(self.aire))
        
La méthode __exit__ doit obligatorirement posséder trois paramètres pour recueillir les informations pertinente en cas
d'erreur.
 
Le nom des paramètres n'a pas d'importance, ce qui compte c'est bien d'en avoir trois, mais vous pourriez les appeler
autrement et ça fonctionnerait également.
 
POINTS IMPORTANTS A RETENIR
1. Pour implémenter un contextmanager, on utlise les méthodes __enter__ et __exit__.
2. Le contextmanager d'une classe est appelé automatiquement quand on utilise l'instruction with.
"""

# exercice 25
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842334#overview

"""
025 - Créer une classe e-mail
Dans cet exercice, vous devez compléter la classe e-mail.

Créer, un attribut number_of_mails_sent
1. Vous devez créer un attribut de classe nommé number_of_mails_sent sur la classe Email.
2. Cet attribut devra être incrémenté de 1 à chaque fois qu'un e-mail est envoyé (donc à chaque fois que la méthode 
   send_to est appelée).
3. L'e-mail ne doit être envoyé que si l'attribut is_sent est False.
4. Si cet attribut est False, vous devez le modifier pour le passer à True pour signifier que l'e-mail a bien été envoyé
   et enpêcher ainsi l'utilisateur de l'envoyer une seconde fois.
"""

# class Email:
#     number_of_mails_sent = 0
#
#     def __init__(self, content):
#         self.content = content
#         self.is_sent = False
#
#     def send_to(self, email):
#         if not self.is_sent:
#             self.is_sent = True
#             Email.number_of_mails_sent += 1
#             return f"E-mail envoyé"
#         email2 = email
#         return f"L'e-mail a déjà été envoyé"
#
#
# email = Email(content="La nouvelle formation est disponible !")
# response_01 = email.send_to(email="JohnSmith@gmail.com")
# response_02 = email.send_to(email="JongSmith@gmail.com")
# print(response_01)
# print(response_02)

# exercice 26
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842336#overview
"""
026 - Gérer une classe d'élèves

Dans cet exercice vous devez créer une classe Classe qui permette de gérer les élèves avec la classe Eleve.
La classe Classe doit posséder une méthode statique ajouter_eleve qui permette d'ajouter un élève avec un prénom et un nom.
Les instances délèves créées avec cette méthode statique doivent être ajoutèes à une liste eleves appartenant à Classe.
Vous devez également modifier la représentation des instances créées à partir d'Eleve pour qu'elles affichent le prenom
des élèves. 
Dans le cas de ce script, l'attribut eleves devra donc être une liste qui contient une instance d'un élève qui s'appelle
"John Smith" et cet attribut devra afficher la liste suivante:
    >>> Classe.eleves
    ["John Smith"]
"""

# class Eleve:
#     def __init__(self, prenom, nom):
#         self.prenom = prenom
#         self.nom = nom
#         self.nom_complet = prenom + " " + nom
#
#     def __repr__(self):
#         return f"{self.nom_complet}"
#
#
# class Classe:
#     eleves = []
#
#     @staticmethod
#     def ajouter_eleve(prenom, nom):
#         Classe.eleves.append(Eleve(prenom, nom))
#
#
# Classe.ajouter_eleve("John", "Smith")
# print(Classe.eleves)

"""
EXPLICATIONS
Pour commencer, nous allons modifier la représentation des instances de la classe élève, grâce à la méthode __repr__ et
la méthode format:
    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)

Ainsi, quand on affiche une instance d'élève, on affichera son prénom et son nom au lieu de l'adresse en mémoire de 
l'instance.

Nous devions ensuite créer une méthode statique ajouter_eleve qui permette d'ajouter un élève avec un prénom et un nom.

On donne deux paramètres à la méthode, prenom et nom:
    @staticmethod
    def ajouter_eleve(prenom, nom)

Pour finir, il suffisait de créer une instance d'élève à partir des valeurs passées aux paramètres prenom et nom de la 
méthode ajouter_eleve. On crée également un attribut de classe eleves (une liste vide) pour stocker les instances 
d'élèves créées:
    class Classe:
        eleves = []
        
        @staticmethod
        def ajouter_eleve(prenom, nom):
        eleve = Eleve(prenom=prenom, nom=nom)
        Classe.eleves.append(eleve)
        
POINTS IMPORTANT A RETENIR
1. Pour créer une méthode statique, on utlise le décorateur @staticmethod
2. Pour créer un attribut de classe
"""

# exercice 27
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842338#overview
"""
027 - Créer des pizzas

Quelle meilleur façon de faire de la programmation qu'en créant des pizzas?
Dans cet exercice, vous devez utiliser les méthodes de classe pour créer une pizza napolitaine et une pizza au fromage 
avec la syntaxe suivante: 
    napo = Pizza.napolitaine()
    fromage = Pizza.fromage()
La pizza napolitaine devra avoir comme nom "Napolitaine", comme infrédients la liste ["Tomates", "Anchois"] et comme
prix 12.99 euros.
La pizza au fromage elle devra avoir comme nom "4 Fromages", comme ingrédients ["Mozzarella", "Compté", "Cheddar", 
"Gorgonzola"] et comme prix 14.99 euros.
"""

# class Pizza:
#     def __init__(self, nom, ingredients, prix=9.99):
#         self.nom = nom
#         self.ingredients = ingredients
#         self.prix = prix
#
#     @classmethod
#     def napolitaine(cls):
#         return f"nom='Napolitaine', ingredients=['Tomates', 'Anchois'], prix=12.99"
#
#     @classmethod
#     def fromage(cls):
#         return f"nom='4 Fromages',ingredients=['Mozzarella', 'Comté', 'Cheddar', 'Gorgonzola'], prix=14.99)"
#
#
# print(Pizza("Napolitaine", ["Tomates", "Anchois"], prix=12.99).napolitaine())
# print(Pizza("4 fromages", ["Mozzarella", "Compté", "Cheddar", "Gorgonzola"], prix=14.99).fromage())

"""
EXPLICATIONS
Pour créer des méthodes de classe, on utilise le décorateur @classmethod.
Cela permet de créer  une méthode qui possède en premier paramètre la classe elle-même, dans un paramètre que l'on 
appelle par convention cls (moais on pourrait l'appeler autrement, ce n'est pas une obligation).
Cela nous permet de retourner une instance de la classe directement dans la méthode, ce que nous faisons pour créer une
instance de pizza 4 fromages avec la méthode fromage et une pizza napolitaine avec la méthode napolitaine:
    @classmethod
    def napolitaine(cls):
        retrun cls(nom="Napolitaine",
                    ingredients=["Tomates", "Anchois"], prix=12.99)
                    
    @classmethod
    def fromage(cls):
        return cls(nom="4 Fromages", 
                    ingredients=["Mozzarella", "Comte", "Cheddar", "Gorgonzola"], prix=14.99) 
                    
Il suffisait d'entrer les bonnes valeurs pour le nom, les ingrédients et le prix pour valider l'exercice.

POINTS IMPORTANTA A RETENIR
1. Pour créer des méthodes de classe, on utlise le décorateur @classmethod
2. Le nom du premier paramètre pour les méthodes de classe s'appelle par convention cls.
"""

# Exercice 28
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842340#overview
"""
028 Créer un générateur de mots de passe

Dans cet exercice, rien de très compliqué, mais là encore vous partez de 0,
Vous devez créer une classe PasswordGenerator qui permet de générer grâce à une méthode generate un mot de passe 
aléatoire composé de lettres minuscules ou majuscules et de chiffres de 0 à 9 d'une longueur indiquée par un argument
envoyé à la méthode generate:
    >>> mot_de_passe = PasswordGenerator.generate(15)
    "MPCk5L1q2JEulId"
Pour utiliser la méthode generate directement sur la classe PasswordGenerator, pensez aux méthodes de classe.
"""

# import random, string
#
#
# class PasswordGenerator:
#
#     @staticmethod
#     def generate(longueur):
#         result = random.sample(string.ascii_letters + string.digits, longueur)
#         return result
#
#
# print(PasswordGenerator.generate(15))

"""
EXPICATIONS
Un exercice assez court à mettre en place mais qui faisait appel à plusieurs notions.
Premièrement, nous devions créer une méthode qui soit utilisable directement par la classe.
Pour cela, on utlise le décorateur @staticmethod qui permet de créer une méthode statique.
On créait donc une méthode generate qui acceptait une paramètre que l'on appelé ici length et qui permettait de définir
la longueur du mot de passe:
    @staticmethod
    def generate(length):
Enusuite, nous utilisons le module string pour récupérer toutes les lettres de l'alphabet en majuscules et minuscules et
tous les chiffres de 0 à 9:
    string.digits + string.ascii_letters
Il ne nous restait plus qu'à retourner un échantillon aléatoire de la longueur indiqué par le paramètre longueur à la
fonction sample du module random.

La fonction sample nous retournant une liste, il ne fallait pas oublier de joindre les éléments de la liste avec la 
méthode join, sur une chaîne de caractère vide:
    return "".join(random.sample(string.digits + string.ascii_letters, length))
    
POINTS IMPORTANTS A RETENIR
1. Pour créer une méthode que l'on peut utiliser directement sur une classe, on utilise les méthodes statiques et le
décorateur @staticmethod.
2. Pour générer un échantillon aléatoire d'une certaine longueur, on utilise la methode sample du module random.
"""

# exercice 29
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842342#questions
"""
029 Implementer l'addition entre instances

Dans cet exercice, vous partez là encore de zéro.
Premièrement, vous devez créer une classe Note qui contient un seul attribut, valeur, qui correspond à la valeur de la
note.
Vous devez modifier la représentation des instances de cette classe pour qu'elles affichent la valeur de la note sur 20,
comme ceci: 
    >>> note = Note(valeur=12)
    >>> note
    '12 / 20'
Vous devez ensuite créer une classe Notes qui hérite de la classe list et qui permet de récupérer une liste d'instances 
de notes. On doit pouvoir ajouter une note à cette classe avec la méthode ajouter_note.
On créera ensuite deux méthodes.
La première, notes_parfaites, qui retournera le nombre de notes égales à 20 / 20.
La deuxème, moyenne, qui retourner la moyenne des notes.
"""


# class Note:
#     def __init__(self, valeur):
#         self.valeur = valeur
#
#     def __repr__(self):
#         return "{} / 20".format(str(self.valeur))
#
#
# class Notes(list):
#     def ajouter_note(self, note):
#         self.append(note)
#
#     def notes_parfaites(self):
#         nombre = 0
#         for note in self:
#             if note.valeur == 20:
#                 nombre += 1
#
#         return nombre
#
#     def moyenne(self):
#         return round(sum([note.valeur for note in self]) / len(self), 1)
#
#
# valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
# note = Note('12')
# notes = Notes()
# print(note)
#
# for valeur_note in valeur_notes:
#     notes.ajouter_note(note=Note(valeur=valeur_note))
#
# print(notes.notes_parfaites())
# print(notes.moyenne())

"""
EXPLICATIONS
La première chose à faire était de créer  une classe Note qui permette de représenter la note d'un étudiant.

Cette classe devait posséder comme attribut la valeur de la note.

On récupère donc cette valeur au moment de l'instanciation de la classe, dans la méthode __init__:
    class Note:
        def __init__(self, valeur):
            self.valeur = valeur
            
On devait également modifier la représentation de la classe pour qu'elle affiche la valeur de la note sur 20.

Pour cela, on implémente la méthode __repr__:
    def __repr__(self):
        return "{} / 20".format(str(self.valeur))
        
On devait ensuite créer une classe Notes qui permette d'ajouter et récupére des informations sur toutes les notes de
notre liste.

On devait faire hériter notre classe de la classe list afin de pouvoir ajouter des notes directement dans les instances
de cette classe avec la méthode ajouter_note:
    class Notes(list):
        def ajouter_note(self, note):
            self.append(note)
            
Comme vous pouvez le voir dans le code ci-dessus, le fait d'hériter de la classe list nous permet d'ajouter les notes
directement avec self.append, car les instances créées à partir de la classe Notes seront des listes (on peut donc 
ajouter des éléments à l'intérieur avec la méthode append).

Pour finir, il suffisait d'implémenter deux méthodes pour récupérer toutes les notes égales à 20 
(la méthode notes_parfaites) et la moyenne des notes (la méthode moyenne):
    def notes_parfaites(self):
        nombre = 0
        for note in self:
            if note.valeur == 20:
                nombre += 1
                
        return nombre
        
    def moyenne(self):
        return round(sum([note.valeur for note in self]) / len(self), 1)
        
Rien de bien compliqué à l'intérieur de ces deux méthodes, il s'agit juste de vérifier les notes égales à 20 et de faire
la moyenne des instances de la classe Note contenues dans notre liste avec la fonction sum.

Vous remarquerez que comme notre instance est une liste, on peut boucler sur les éléments de l'instance tout simplement
en bouclant sur self avec for note in self.

POINTS IMPORTANT A RETENIR
1. Pour hériter d'une classe, on met le nom de la classe edans les parenthèses lors de la définition de notre classe.
2. Pour changer la représentations d'une classe, on utilise la méthode __repr__.
3. Quand on hérite d'une classe, on hérite de toutes ses méthodes. En héritant de la class list, on peut donc utiliser 
   la méthode append.
"""

# exercice 30
# https://www.udemy.com/course/30-exercices-orientes-objets-avec-python/learn/quiz/4842344#questions

"""
030 - Implémenter l'addition entre instances

Dans cet exercice, on veut permettre d'additionner plusieurs chaînes de caractères ensemble pour récupérer un chemin de
dossier. La variable composite, qui additionne l'instance c avec des chaînes de caractères doit donc retourner le 
chemin:
    >>> composite = c + "dossier" + "test" + "script"
    /Users/john/dossier/test/script
Le symbole d'addition doit donc concaténer les différentes chaînes de caractères ensemble en ajoutant un slash entre 
chaque chaîne de caractères afin de créer un chemin au format unix valide. 
"""


class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin

    def __add__(self, content):
        return Chemin(self.chemin + "/" + content)


c = Chemin("/Users/John")
composite = c + "dossier" + "test" + "script"
print(composite)
