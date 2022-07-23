# -*- coding: iso8859-15 -*-

from tkinter import *
from random import choice
from base64 import decodestring
import sys


class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("::.Trouver le mot.::-By Kouakou021988")
        self.master.resizable(width=False, height=False)
        self.grid()
        Label(self, text="Reponse/Question('?'):", fg='royal blue',
              font='arial 9 bold').grid(row=0, column=0)
        self.ent = Entry(self, width=20, bg='grey40',
                         font='arial 9 bold', fg='white')
        self.ent.grid(row=0, column=1)
        self.but = Button(self, text='Envoyer>>', font='arial 9 bold',
                          fg='royal blue', command=self.reponse).grid(row=0, column=2)
        self.msg = tkinter.scrolledtext(self)
        self.msg.grid(row=1, column=0, columnspan=3)
        self.msg.insert('end', 'Akwaba vous souhaite la bienvenue\nPour comprendre ce jeu, lisez le fichier "c://Akwaba_jeu/Lisezmoi.txt\nPour tout renseignement russian_akwaba@yahoo.fr\nBonne Chance\n----------------------------------------------------------\n')
        self.liste = []
        self.qst = []
        self.f = open("traduit.txt", 'r').readlines()
        self.start()
        self.master.protocol("WM_DELETE_WINDOW", self.quitter)
        self.master.bind('<Escape>', self.quitter)

    def reponse(self):
        if not self.ent.get() or self.ent.get().isspace():
            tkMessageBox.showerror("::.Trouver le mot.::", "Champ vide")
        else:
            txt = self.ent.get().strip()
            if len(txt) == 2 and txt[1] == '?':
                txt = txt[0].upper()
                if len(self.qst) == 3:
                    tkMessageBox.showerror(
                        "::.Trouver le mot.::", "Vous devez repondre maintenant!!")
                else:
                    r = self.question(txt)
                    self.qst.append(r)
                    if r:
                        msg = "Le mot contient (%s) lettre(s) %s\n" % (r, txt)
                        self.msg.insert('end', msg)
                    else:
                        msg = "Le mot ne contient pas de lettre %s\n" % txt
                        self.msg.insert('end', msg)
            else:
                if self.ent.get().upper().strip() == self.rep:
                    msg = "Bravo vous venez de trouvez le mot: %s\n" % self.rep
                    self.msg.insert('end', msg)
                else:
                    msg = "Desoler mais la bonne réponse etait %s\n" % self.rep
                    self.msg.insert('end', msg)
                self.msg.insert(
                    'end', "----------------------AKWABA----------------------------\n")
                self.start()

    def start(self):
        nbre = len(self.f)
        q, h = self.choix(nbre)
        self.qst = []
        if len(self.liste) > nbre/2:
            self.liste = []
        self.rep = str(decodestring(self.f[q][:-1]).upper())
        if h == 0:
            c = self.rep[h]
            msg = "Le mot recherché commence par %s et est composé de %s caractère(s)\n" % (
                c, len(self.rep))
            self.msg.insert('end', msg)
        else:
            c = self.rep[len(self.rep)-1]
            msg = "Le mot recherché se termine par %s et est composé de %s caractère(s)\n" % (
                c, len(self.rep))
            self.msg.insert('end', msg)

    def choix(self, x):
        while 1:
            s = choice(range(x))
            if s in self.liste:
                pass
            else:
                self.liste.append(s)
                break
        return s, choice(range(2))

    def question(self, r):
        if r in self.rep:
            return self.rep.count(r)
        else:
            return 0

    def quitter(self, event=None):
        self.master.destroy()
        sys.exit()


###-----------------------------------------------------------------------###
if __name__ == '__main__':
    app = Game()
    app.mainloop()
