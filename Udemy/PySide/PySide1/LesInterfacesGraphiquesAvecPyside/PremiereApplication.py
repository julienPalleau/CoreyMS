from PySide2 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    fenetre = QtWidgets.QWidget()
    fenetre.setWindowTitle("Mon Application")
    w = h = 500
    fenetre.resize(w, h)
    fenetre.move(1920/2 - w/2, 1080/2 - h/2)


    fenetre.show()
    app.exec_()
