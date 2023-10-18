import os
from glob import glob
import utils as utl


def creerNote(nomDeLaNote, contenu=''):
    # cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')

    with open(recupereLeCheminDeLaNote(nomDeLaNote), 'w') as f:
        f.write(contenu)

    if os.path.isfile(recupereLeCheminDeLaNote(nomDeLaNote)):
        print('La note "{}" a bien ete creee'.format(nomDeLaNote))


def recupererContenuNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')
    with open(cheminDeLaNote, 'r') as f:
        contenuDeLaNote = f.read()

    return contenuDeLaNote


def recupereLeCheminDeLaNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')
    return cheminDeLaNote


def recupererLesNotes():
    notes = glob(utl.DATA_FOLDER + '/*.txt')
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]
    return notes


def supprimerNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')

    if os.path.isfile(recupereLeCheminDeLaNote(nomDeLaNote)):
        os.remove(recupereLeCheminDeLaNote(nomDeLaNote))
        print('La note "{}" a bien ete supprimee'.format(nomDeLaNote))
    else:
        print('La note "{}" n existe pas'.format(nomDeLaNote))
