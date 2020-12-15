'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

import time
import tkinter as tk

x_max = 6
y_max = 6
nb_tirs = 0

class alien:

    def __init__(self, identifiant, x, y):
        self.identifiant = identifiant
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.identifiant)

    def mouvement(self):
        # fait bouger le vaisseau alien en zig-zag jusqu'en bas de l'écran
        self.print_coord()
        while self.y < y_max:
            while self.x < x_max:
                # l'alien bouge de gauche à droite jusqu'à atteindre le bord droit de l'écran
                time.sleep(.5)
                self.x += 1
                self.print_coord()
            time.sleep(.5)
            self.y += 1
            # l'alien descend d'une case
            self.print_coord()
            while self.x > 0:
                # l'alien bouge de droite à gauche jusqu'à atteindre le bord gauche de l'écran
                time.sleep(.5)
                self.x -= 1
                self.print_coord()
            time.sleep(.5)
            self.y += 1
            # l'alien descend d'une case
            self.print_coord()
            
    def print_coord(self):
        # affiche les coordonnées du vaisseau alien
        print('x=' + str(self.x), 'y=' + str(self.y))



class vaisseau:
    
    def __init__(self):
        self.x = 3
        
    def recup_touche(self):
        fenetre = tk.Tk()
        fenetre.bind("<Key>", self.action)
        fenetre.mainloop()

    def action(self, touche):
        caractere = touche.char
        if caractere == 'q':
            print('a gauche')
            self.print_coord()
            self.mouvement('gauche')
        elif caractere == 'd':
            print('a droite')
            self.print_coord()
            self.mouvement('droite')
        elif caractere == ' ':
            print('tir')
            self.tir()

    def mouvement(self,cote):
        if cote == 'gauche' and self.x > 0:
            self.x -= 1
        if cote == 'droite' and self.x < x_max:
            self.x += 1

    def tir(self):
        global nb_tirs
        nb_tirs += 1
        numero_tir = nb_tirs
        nom_tir = 'tir' + str(numero_tir)
        nom_tir = tir(nom_tir, self.x)
        nom_tir.lancement()
        print(nom_tir)

    def print_coord(self):
        # affiche les coordonnées du vaisseau du joueur
        print('x=' + str(self.x))

class tir:

    def __init__(self, nom_tir, x):
        self.x = x
        self.y = y_max
        self.nom = nom_tir

    def __str__(self):
        return str(self.nom)

    def lancement(self):
        while self.y > 0:
            self.print_coord()
            time.sleep(.5)
            self.y -= 1

    def print_coord(self):
        # affiche les coordonnées du tir
        print('x=' + str(self.x), 'y=' + str(self.y))



joueur = vaisseau()
joueur.recup_touche()



'''
blob = alien('blob',0,0)
print(blob)
blob.mouvement()
'''