import os
from PyQt5 import QtWidgets
from ui.fenetrePrincipale import Ui_FenetrePrincipale
import notesManager as nm
import utils as utl


class CreateurDeNote(QtWidgets.QWidget, Ui_FenetrePrincipale):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.recupererNotes()
        self.setupConnections()
        self.show()

    def setupConnections(self):
        self.btn_creerNote.clicked.connect(self.creerNotes)
        self.lw_listeDeNotes.itemClicked.connect(self.afficherLaNote)
        self.btn_mettreAjourNote.clicked.connect(self.mettreAJourLaNote)
        self.btn_supprimerNote.clicked.connect(self.supprimerNote)

    def afficherLaNote(self):
        nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
        contenuDeLaNote = nm.recupererContenuNote(nomDeLaNote)
        self.te_contenuDeLaNote.setText(contenuDeLaNote)

    def creerNotes(self):
        nomDeLaNote, ok = QtWidgets.QInputDialog.getText(self, 'Creer une note', 'Entrez le nom de la note: ')
        if not ok:
            return

        nm.creerNote(nomDeLaNote)
        self.recupererNotes()
        print(nm.recupererLesNotes()[-1])

    def mettreAJourLaNote(self):
        if self.recupererNoteSelectionnee():
            nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
            contenuDeLaNote = self.te_contenuDeLaNote.toPlainText()
            nm.creerNote(nomDeLaNote, contenuDeLaNote)
        else:
            #print("La fonction ne retourne rien")
            QtWidgets.QMessageBox.warning(self, "Erreur de Saisie", "Veuillez selectionner la note à updater")

    def recupererNotes(self):
        self.lw_listeDeNotes.clear()
        notes = nm.recupererLesNotes()
        self.lw_listeDeNotes.addItems(notes)

    def recupererNoteSelectionnee(self):
        notesSelectionnees = self.lw_listeDeNotes.selectedItems()
        if not notesSelectionnees:
            #return "", ""
            # return
            nomDeLaNote = nm.recupererLesNotes()[-1]
            cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')
            return nomDeLaNote, cheminDeLaNote
        nomDeLaNote = notesSelectionnees[-1].text()
        cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')
        return nomDeLaNote, cheminDeLaNote

    def supprimerNote(self):
        nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
        nm.supprimerNote(nomDeLaNote)
        self.recupererNotes()
        self.te_contenuDeLaNote.setText('')


app = QtWidgets.QApplication([])
nc = CreateurDeNote()
app.exec_()
