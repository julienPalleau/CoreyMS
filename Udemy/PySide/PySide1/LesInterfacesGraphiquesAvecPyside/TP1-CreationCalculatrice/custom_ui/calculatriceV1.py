from PyQt5 import QtCore, QtWidgets
from functools import partial


class Calculatrice(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Init Window
        self.setWindowTitle('Ma Super Calculatrice')

        self.setupUi()
        self.setupConnections()

    def setupUi(self):

        self.le_operation = QtWidgets.QLineEdit()
        self.le_resultat = QtWidgets.QLineEdit('0')

        self.gridLayout = QtWidgets.QGridLayout(self)

        self.btn_0 = QtWidgets.QPushButton('0')
        self.btn_1 = QtWidgets.QPushButton('1')
        self.btn_2 = QtWidgets.QPushButton('2')
        self.btn_3 = QtWidgets.QPushButton('3')
        self.btn_4 = QtWidgets.QPushButton('4')
        self.btn_5 = QtWidgets.QPushButton('5')
        self.btn_6 = QtWidgets.QPushButton('6')
        self.btn_7 = QtWidgets.QPushButton('7')
        self.btn_8 = QtWidgets.QPushButton('8')
        self.btn_9 = QtWidgets.QPushButton('9')

        self.btn_point = QtWidgets.QPushButton('.')
        self.btn_plus = QtWidgets.QPushButton('+')
        self.btn_moins = QtWidgets.QPushButton('-')
        self.btn_mult = QtWidgets.QPushButton('*')
        self.btn_div = QtWidgets.QPushButton('/')
        self.btn_egal = QtWidgets.QPushButton('=')
        self.btn_c = QtWidgets.QPushButton('c')

        self.gridLayout.addWidget(self.le_operation, 0, 0, 1, 4)
        self.gridLayout.addWidget(self.le_resultat, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.btn_c, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_mult, 3, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_moins, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_point, 6, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_egal, 6, 3, 1, 1)

        self.btns_nombre = []

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64, 64)
                if widget.text().isdigit():
                    self.btns_nombre.append(widget)

    def setupConnections(self):
        for btn in self.btns_nombre:
            btn.clicked.connect(partial(self.btnNombrePressed, str(btn.text())))

        self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
        self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
        self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
        self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))

        self.btn_egal.clicked.connect(self.calculOperation)
        self.btn_c.clicked.connect(self.supprimerResultat)

    def btnNombrePressed(self, bouton):
        """Fonction activee quand l'utilisateur appuie sur un numero (0-9)"""

        # On recupere le texte dans le lineEdit resultat
        resultat = str(self.le_resultat.text())

        if resultat == '0':
            # Si le resultat est egal à 0 on met le nombre du bouton
            # que l'utilisateur a presse dans le LineEdit resultat
            self.le_resultat.setText(bouton)
        else:
            # Si le resultat contient autre chose que zero,
            # On ajoute le texe du bouton a celui dans le LineEdit resultat
            self.le_resultat.setText(resultat + bouton)

    def btnOperationPressed(self, operation):
        """
        Fonction activee quand l'utilisateur appuie sur une touched d'operation (+, -, /, *)
        :param operation:
        :return:
        """

        # On recupere le texte dans le LineEdit operation
        operationText = str(self.le_operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_resultat.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute à la fin le signe de l'operation qu'on a choisie
        self.le_operation.setText(operationText + resultat + operation)
        # On reset le texte du LineEdit resultat
        self.le_resultat.setText('0')

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""
        self.le_resultat.setText("0")
        self.le_operation.setText("")

    def calculOperation(self):
        """On calcule le resultat de l'operation en cours (quand l'utilisateur appuie sur egal)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_resultat.text())

        # On ajoute le nombre actuel dans le LineEdit resulat
        # au LineEdit operation
        self.le_operation.setText(self.le_operation.text() + resultat)

        # On evalue le resultat de l'operation
        resultatOperation = eval(str(self.le_operation.text()))

        # On met le resultat final dans le LineEdit resultat
        self.le_resultat.setText(str(resultatOperation))


app = QtWidgets.QApplication([])
fenetre = Calculatrice()
fenetre.show()
app.exec_()
