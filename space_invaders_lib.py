'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

import time
import tkinter as tk

class alien:

    def __init__(self, identifiant, x, y):
        self.identifiant = identifiant
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.identifiant)

    def mouvement(self, x_max, y_max):
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
        fenetre.bind("<Key>", joueur.mouvement)
        fenetre.mainloop()

    def mouvement(self, touche):
        caractere = touche.char
        if caractere == 'q':
            commande = 'gauche'
        elif caractere == 'd':
            commande = 'droite'
        elif caractere == ' ':
            commande = 'tir'
        return commande
        print(commande)


joueur = vaisseau()
joueur.recup_touche()





'''
blob = alien('blob',0,0)
print(blob)
blob.mouvement(6,6)
'''