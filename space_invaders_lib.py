'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

import time
import tkinter as tk

# paramètres du jeu
x_max = 6
y_max = 6
delai_mvt_alien = .001
delai_mvt_tir = .01

# initialisation des variables
nb_tirs = 0
tirs_en_cours = []
aliens_vivants = []

class alien:

    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y
        aliens_vivants.append(self)
        
    def __str__(self):
        return str(self.nom)

    def mouvement(self):
        # fait bouger le vaisseau alien en zig-zag jusqu'en bas de l'écran
        global delai_mvt_alien
        self.print_coord()
        while self.y < y_max:
            while self.x < x_max:
                # l'alien bouge de gauche à droite jusqu'à atteindre le bord droit de l'écran
                time.sleep(delai_mvt_alien)
                self.x += 1
                self.print_coord()
            time.sleep(delai_mvt_alien)
            self.y += 1
            # l'alien descend d'une case
            self.print_coord()
            while self.x > 0:
                # l'alien bouge de droite à gauche jusqu'à atteindre le bord gauche de l'écran
                time.sleep(delai_mvt_alien)
                self.x -= 1
                self.print_coord()
            time.sleep(delai_mvt_alien)
            self.y += 1
            # l'alien descend d'une case
            self.print_coord()
            
    def print_coord(self):
        # affiche les coordonnées du vaisseau alien
        print(self.nom + ' : {' + 'x=' + str(self.x) + ' ; y=' + str(self.y) + '}')



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
            self.mouvement('gauche')
            self.print_coord()
        elif caractere == 'd':
            print('a droite')
            self.mouvement('droite')
            self.print_coord()
        elif caractere == ' ':
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

    def print_coord(self):
        # affiche les coordonnées du vaisseau du joueur
        print('x=' + str(self.x))

class tir:

    def __init__(self, nom_tir, x):
        self.x = x
        self.y = y_max
        self.nom = nom_tir
        tirs_en_cours.append(self)

    def __str__(self):
        return str(self.nom)

    def lancement(self):
        global delai_mvt_tir
        alien_touche = 0
        while alien_touche == 0 and self.y > 0:
            self.print_coord()
            time.sleep(delai_mvt_tir)
            self.y -= 1
            for alien in aliens_vivants:
                if alien.x == self.x and alien.y == self.y:
                    print(alien.nom + ' touché !')
                    aliens_vivants.remove(alien)
                    del alien
                    alien_touche = 1
        tirs_en_cours.remove(self)
        del self

    def print_coord(self):
        # affiche les coordonnées du tir
        print(self.nom + ' : {' + 'x=' + str(self.x) + ' ; y=' + str(self.y) + '}')



def nouveau_jeu(nb_aliens):
    for i in range(nb_aliens):
        nom_alien = 'alien_' + str(i + 1)
        nom_alien = alien(nom_alien, 0, 0)
        nom_alien.mouvement()
    joueur = vaisseau()
    joueur.recup_touche()


alien_test = alien('alien_test',3,3)
print('aliens vivants : ' + str(aliens_vivants))
nouveau_jeu(3)
'''
blob = alien('blob',0,0)
print(blob)
blob.mouvement()


joueur = vaisseau()
joueur.recup_touche()
'''

