from PyQt5 import QtWidgets, QtGui
#  from PySide2 import QtWidgets, QtGui # both are working


class FenetrePrincipale(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mon Application')

        layout = QtWidgets.QHBoxLayout(self)

        self.lw_demo = QtWidgets.QListWidget(self)
        self.lw_demo.addItems(['Premier', 'Deuxieme', 'Troisieme'])

        QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Delete'), self, self.lw_demo.clear)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)

        QtGui.QKeySequence(QtGui.QKeySequence.Print)
        QtGui.QKeySequence("Ctrl+P")

        layout.addWidget(self.lw_demo)


app = QtWidgets.QApplication([])
fenetre = FenetrePrincipale()
fenetre.show()
app.exec_()
