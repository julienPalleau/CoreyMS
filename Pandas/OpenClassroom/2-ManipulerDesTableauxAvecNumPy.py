# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/exercises/4575
"""
Compétences évaluées

    Manipuler des tableaux avec Numpy

    Question 1

    Quelles sont les caractéristiques principales de NumPy ?
    Attention, plusieurs réponses sont possibles.

        NumPy est l’unique librairie utilisée en analyse de données

    x    L’un des objets principaux de NumPy est l’array

    x    NumPy est une librairie permettant d’effectuer des calculs scientifiques

        NumPy propose uniquement une amélioration de la liste Python

    NumPy est une librairie complète, proposant via l’objet array une amélioration de la liste Python, mais également de nombreuses fonctions scientifiques et mathématiques. Ce n’est donc pas qu’une amélioration de la liste Python. De plus, c’est une des librairies principales utilisées en data, mais ce n’est pas LA principale !
    Question 2

    L’array NumPy :

        est un des nombreux objets natifs de Python

        peut contenir en même temps des entiers et des décimaux

    x    est plus rapide d'exécution qu’une liste

        doit forcément être créé à partir d’une liste

    L’array est un objet NumPy : ce n’est donc pas un objet natif de Python. Il est forcément monotype. Il peut être créé à partir d’une liste, ou à partir d’une fonction NumPy prévue à cet effet. De plus, l’array permet d’effectuer de nombreux calculs scientifiques et mathématiques jusqu’à 30 fois plus rapidement qu’avec une liste classique.
    Question 3

    Je souhaite créer un array contenant la séquence linéaire suivante :

    0, 1, 2, 3, 4, 5, 6, 7

    Quelle fonction puis-je utiliser ?

    x    arange

        zeros

        linear

        ones

    La fonction  np.arange(i, j, p)  permet de créer un array rempli avec une séquence linéaire, qui ira de  i  à  j, par pas de  p. En définissant i = 0, j = 8 et p = 1, on obtient bien le résultat escompté.
    Question 4

    Quel serait l’affichage correspondant aux lignes de code suivantes ?

a = np.linspace(5, 10, 11)

print(a[-3:-1])

    [5.5, 6. ]

  x  [9. , 9.5]

    [6.5, 7. , 7.5, 8. , 8.5, 9. , 9.5]

    [5.5, 6. , 6.5, 7. , 7.5, 8. , 8.5]

-3 à -1 correspond à l’avant-avant-dernier élément, jusqu’à l’avant-dernier élément.

Ici,  a   contient l’array suivant :  array([ 5. ,  5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5, 10. ])

Donc  a[-3:-1]  affichera :  [9. , 9.5]
Question 5

En reprenant l’array précédent et en sachant que l’opérateur  %   donne le reste de la division euclidienne, qu’affiche la ligne de code suivante ?

a[a % 2 == 0]

 x   L’ensemble des chiffres de l’array qui sont pairs

    L’ensemble des éléments de l’array divisé par 2

    Les éléments qui sont compris entre 0 et 2

    L’ensemble des chiffres de l’array qui sont impairs

Le signe  %   en Python correspond au reste de la division entière. Ainsi, la condition est : l’ensemble des chiffres dont le reste de la division entière par 2 est zéro. Donc on sélectionne selon cette condition, c'est-à-dire l’ensemble des chiffres de l’array qui sont divisibles par 2, donc pairs.
Question 6

Considérons la ligne de code suivante :

b = np.array([[[1, 2],[4, 5]],

        [[6, 7],[8, 9]],

        [[10, 11],[12, 13]]])

Que permet-elle de créer ?

x    Un tableau de 3x2x2

    Un tableau de 3x1x2

    Un tableau de 2x3x2

    Un tableau de 2x2x3

Les dimensions de l’array sont bien 3x2x2 ! Vous pouvez vérifier cela en exécutant le code suivant :

b = np.array([[[1, 2],[4, 5]],

        [[6, 7],[8, 9]],

        [[10, 11],[12, 13]]])

b.shape

Question 7

Quelle ligne de code permettrait de passer l’array b dans une dimension 4x1x3 ?

    np.vstack(b)

    b.flatten(4, 1, 3)

x    b.reshape([4, 1, 3])

La méthode reshape peut prendre en paramètre soit les valeurs séparées (donc  b.reshape(4, 1, 3)  ), soit une liste/tuple comme c’est le cas ici.
Question 8

Souvenez-vous de l’array  b   présenté précédemment :

b = np.array([[[1, 2],[4, 5]],

        [[6, 7],[8, 9]],

        [[10, 11],[12, 13]]])

 Quels indices et/ou conditions permettent d’obtenir l’affichage suivant ?

array([[10, 11],

       [12, 13]])

x    b[2, :, :]

    b[2, 2, :]

    b[b > 10]

    b[2, :, 2]

Nous avons ici un tableau composé de 3 tableaux de 2 lignes et 2 colonnes (le premier contenant 1, 2, 4 et 5, le second 6-9 et le dernier 10-13), donc un array de dimensions 3x2x2. Ici on souhaite accéder uniquement au 3e et dernier tableau (qui a pour indice 2), et on souhaite avoir l’ensemble des lignes et colonnes de ce dernier. L’écriture correcte est donc bien  b[2, :, :]  .

L’écriture  b[b > 10]  aurait pu être valide, mais elle ne l’est pas à cause du signe "strictement supérieur". Ainsi, elle ne sélectionne que 11, 12 et 13.
"""
