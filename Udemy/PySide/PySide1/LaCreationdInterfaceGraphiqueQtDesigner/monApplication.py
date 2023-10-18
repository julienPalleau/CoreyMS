from PyQt5 import QtWidgets, QtCore
from LaCreationdInterfaceGraphiqueQtDesigner import monInterface


class FenetrePrincipale(QtWidgets.QWidget, monInterface.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()


app = QtWidgets.QApplication([])
fenetre = FenetrePrincipale()
app.exec_()
