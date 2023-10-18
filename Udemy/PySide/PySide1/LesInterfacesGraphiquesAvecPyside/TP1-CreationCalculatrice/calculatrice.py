from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial
from custom_ui.fenetrePrincipale import Ui_form_calculatrice


class Calculatrice(Ui_form_calculatrice, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Init Window
        self.setupUi(self)
        self.modificationSetupUi()
        self.setupConnections()
        self.setupRaccourcisClavier()
        self.show()

    def modificationSetupUi(self):
        self.btns_nombre = []

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setStyleSheet('QPushButton:hover {color: rgb(100, 200, 130);}')
            if isinstance(widget, QtWidgets.QPushButton) and widget.text().isdigit():
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

    def setupRaccourcisClavier(self):
        for btn in range(10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNombrePressed, str(btn)))

        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self, partial(self.btnOperationPressed, str(self.btn_plus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self, partial(self.btnOperationPressed, str(self.btn_moins.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_mult.text())), self, partial(self.btnOperationPressed, str(self.btn_mult.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_div.text())), self, partial(self.btnOperationPressed, str(self.btn_div.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
        QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat)
        QtWidgets.QShortcut(QtGui.QKeySequence('Escape'), self, self.close)

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
        # operationText = str(self.le_operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_resultat.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute à la fin le signe de l'operation qu'on a choisie
        #self.le_operation.setText(operationText + resultat + operation)
        self.le_operation.setText(resultat + operation)
        # On reset le texte du LineEdit resultat
        self.le_resultat.setText('0')

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""
        self.le_resultat.setText("0")
        self.le_operation.setText("")

    def calculOperation(self):
        """On calcule le resultat de l'operation en cours (quand l'utilisateur appuie sur egual)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_resultat.text())

        # On ajoute le nombre actuel dans le LineEdit resulat
        # au LineEdit operation
        self.le_operation.setText(self.le_operation.text() + resultat)

        # On evalue le resultat de l'operation
        resultatOperation = int(eval(str(self.le_operation.text())))

        # On met le resultat final dans le LineEdit resultat
        self.le_resultat.setText(str(resultatOperation))



app = QtWidgets.QApplication([])
fenetre = Calculatrice()
fenetre.show()
app.exec_()
