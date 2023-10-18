from PySide2 import QtWidgets, QtCore
import sys
import time

"""
PySide documentation: http://pyside.github.io/docs/pyside/
"""


####################
# QUELQUES WIDGETS #
####################

## CREATION D'UNE FENETRE VIDE
# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Ma Premiere Applicaiton")
#
# app = QtWidgets.QApplication([])
# fenetre = FenetrePrincipale()
# fenetre.show()
# app.exec_()

## QLABEL
# app = QtWidgets.QApplication([])
# label = QtWidgets.QLabel('Bonjour tout le monde')
# print(label.text())
# label.setText('Au revoir tout le monde')
# print(label.text())
# label.show()
# app.exec_()

## QPUSHBUTTON
# app = QtWidgets.QApplication([])
# bouton = QtWidgets.QPushButton('Clique sur le bouton')
#
# # modification du texte sur le bouton
# bouton.setText('Cliquez sur le bouton')
#
# # Recuperation du texte du bouton que l'on affiche dans la console
# print(bouton.text())
#
# bouton.show()
# app.exec_()

## QLINEDIT
# app = QtWidgets.QApplication([])
# lineEdit = QtWidgets.QLineEdit()
#
# # Affichage d'un texte gris pale qui va disparaitre quand on va cliquer dans la boite
# lineEdit.setPlaceholderText('Entrez votre nom')
# lineEdit.show()
# lineEdit.clearFocus()  # Si on on clear pas le focus on ne voie pas Entrez votre nom
# lineEdit.setText('Julien')
# print(lineEdit.text())  # Imprime dans la console ce qui est ecrie dans le linedit
# app.exec_()

###############
# LES LAYOUTS #
###############

## COORDONNEES ABSOLUES
# class MonApplication(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         btn_bonjour = QtWidgets.QPushButton('Bonjour', self)
#         btn_bonjour.move(10, 10)  # coordonnees en absolues (par rapport au point 0,0 situe en haut à gauche)
#
#         btn_auRevoir = QtWidgets.QPushButton('Au revoir', self)
#         btn_auRevoir.move(50, 50)  # coordonnees en absolues (par rapport au point 0,0 situe en haut à gauche)


## Le QGridLayout
# class MonApplication(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QtWidgets.QGridLayout(self)
#
#         # # Exemple 1
#         # btn_1 = QtWidgets.QPushButton('0.0')
#         # btn_2 = QtWidgets.QPushButton('0.1')
#         # btn_3 = QtWidgets.QPushButton('0.2')
#         # btn_4 = QtWidgets.QPushButton('1.0')
#         # btn_5 = QtWidgets.QPushButton('1.1')
#         # btn_6 = QtWidgets.QPushButton('1.2')
#         # btn_7 = QtWidgets.QPushButton('2.0')
#         # btn_8 = QtWidgets.QPushButton('2.1')
#         # btn_9 = QtWidgets.QPushButton('2.2')
#         #
#         # layout.addWidget(btn_1, 0, 0)
#         # layout.addWidget(btn_2, 0, 1)
#         # layout.addWidget(btn_3, 0, 2)
#         # layout.addWidget(btn_4, 1, 0)
#         # layout.addWidget(btn_5, 1, 1)
#         # layout.addWidget(btn_6, 1, 2)
#         # layout.addWidget(btn_7, 2, 0)
#         # layout.addWidget(btn_8, 2, 1)
#         # layout.addWidget(btn_9, 2, 2)
#
#         # Exemple 2
#         btn_1 = QtWidgets.QPushButton('0.0-1x3')
#         btn_2 = QtWidgets.QPushButton('1.0-1x1')
#         btn_3 = QtWidgets.QPushButton('1.1-1x1')
#         btn_4 = QtWidgets.QPushButton('1.2-1x1')
#
#         layout.addWidget(btn_1, 0, 0, 1, 3)
#         layout.addWidget(btn_2, 1, 0, 1, 1)
#         layout.addWidget(btn_3, 1, 1, 1, 1)
#         layout.addWidget(btn_4, 1, 2, 1, 1)


## Le QHBoxLayout et le QVBoxLayout
# class MonApplication(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # layout = QtWidgets.QVBoxLayout(self)
#         layout = QtWidgets.QHBoxLayout(self)
#
#         btn_1 = QtWidgets.QPushButton('Bouton n1', self)
#         btn_2 = QtWidgets.QPushButton('Bouton n2', self)
#         btn_3 = QtWidgets.QPushButton('Bouton n3', self)
#
#         layout.addWidget(btn_1)
#         layout.addWidget(btn_2)
#         layout.addWidget(btn_3)

## Combiner les layouts
# class MonApplication(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layoutPrincipal = QtWidgets.QHBoxLayout(self)
#
#         layoutGauche = QtWidgets.QVBoxLayout()
#         layoutDroite = QtWidgets.QVBoxLayout()
#         layoutPrincipal.addLayout(layoutGauche)
#         layoutPrincipal.addLayout(layoutDroite)
#
#         btn_1 = QtWidgets.QPushButton('Bouton n1', self)
#         btn_2 = QtWidgets.QPushButton('Bouton n2', self)
#         btn_3 = QtWidgets.QPushButton('Bouton n3', self)
#
#         layoutGauche.addWidget(btn_1)
#         layoutGauche.addWidget(btn_2)
#         layoutGauche.addWidget(btn_3)
#
#         btn_4 = QtWidgets.QPushButton('Bouton n4', self)
#         btn_5 = QtWidgets.QPushButton('Bouton n5', self)
#         btn_6 = QtWidgets.QPushButton('Bouton n6', self)
#
#         layoutDroite.addWidget(btn_4)
#         layoutDroite.addWidget(btn_5)
#         layoutDroite.addWidget(btn_6)
#
#         self.resize(500, 500)

## Le QListWidget

# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QtWidgets.QHBoxLayout(self)
#
#         lw_demo = QtWidgets.QListWidget(self)
#         lw_demo.addItem('Premier Item')
#         lw_demo.addItem('Deuxieme Item')
#         lw_demo.addItems(['Troisieme Item', 'Quatrieme Item', 'Cinquieme Item'])
#         lw_demo.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
#
#         layout.addWidget(lw_demo)

## Le QCheckBox

# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Mon Application')
#
#         layout = QtWidgets.QHBoxLayout(self)
#
#         chk_demo = QtWidgets.QCheckBox('Ceci est une checkbox')
#         chk_demo.setCheckState(QtCore.Qt.Checked)
#         print(chk_demo.checkState())
#
#         layout.addWidget(chk_demo)

## Le QComboBox
# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Mon Application')
#
#         layout = QtWidgets.QHBoxLayout(self)
#         cbb_demo = QtWidgets.QComboBox()
#         cbb_demo.addItem('Premier Item')
#         cbb_demo.addItems(['Deuxieme Item', 'Troisieme Item'])
#         # cbb_demo.setCurrentIndex(2)
#         cbb_demo.setCurrentIndex(cbb_demo.count() - 1)  # selection du dernier item si on ne connait pas le nombre
#         # d'item
#         cbb_demo.setItemText(0, 'First')
#         cbb_demo.setItemText(cbb_demo.count() - 1, 'Last Item')
#
#         layout.addWidget(cbb_demo)

## Le QProgressBar
# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Mon Application')
#
#         layout = QtWidgets.QHBoxLayout(self)
#         prg_demo = QtWidgets.QProgressBar()
#         prg_demo.setRange(0, 10)
#         prg_demo.setValue(6)
#         prg_demo.setTextVisible(False)  # Desactive le text ex: 60%
#
#         layout.addWidget(prg_demo)

###############
# Les signaux #
###############

## Connexions simples
# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Les Signaux')
#         layout = QtWidgets.QHBoxLayout(self)
#         btn = QtWidgets.QPushButton('Clique')
#         btn.clicked.connect(self.cliquerSurLeBouton)
#
#         layout.addWidget(btn)
#
#     def cliquerSurLeBouton(self):
#         print('Bouton Clique')

## Connexions avec arguments
from functools import partial

class FenetrePrincipale(QtWidgets.QWidget):


    ("Ici on a deux boutons bouton1 et bouton2 qui appellent la meme fonction (boutonClicked). On va donc passer\n"
     "un argument à la fonction boutonClicked, pour cela il faut importer partial (from functools import partial)\n"
     "et lorsque l'on connect le bouton on passe l'argument")
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Les Signaux')

        layout = QtWidgets.QHBoxLayout(self)

        btn_01 = QtWidgets.QPushButton('Premier Bouton')
        btn_01.clicked.connect(partial(self.boutonClicked, 'Premier Bouton Clique'))

        btn_02 = QtWidgets.QPushButton('Deuxieme Bouton')
        btn_02.clicked.connect(partial(self.boutonClicked, 'Deuxieme Bouton Clique'))

        layout.addWidget(btn_01)
        layout.addWidget(btn_02)

    def boutonClicked(self, texte):
        print(texte)

app = QtWidgets.QApplication([])
# fenetre = MonApplication()
fenetre = FenetrePrincipale()
fenetre.show()
app.exec_()
