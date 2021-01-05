'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

import time
from random import uniform
import threading
import tkinter as tk

########## paramètres du jeu ##########

x_max = 6 # largeur de la zone de jeu 
y_max = 6 # hauteur de la zone de jeu
delai_mvt_alien = .001 # délai entre chaque mouvement d'alien
delai_tir_alien = 2 # délai moyen entre les tirs d'un même alien
delai_mvt_tir = .01 # délai entre chaque mouvement de tir
nombre_vies = 3 # nombre de vies du joueur

########## initialisation ##########

nb_tirs_joueur = 0
nb_tirs_aliens = 0
tirs_en_cours = []
aliens_vivants = []



class alien:
    # classe des vaisseaux ennemis
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y
        aliens_vivants.append(self)
        alien.tir(self)
        
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

    def tir(self):
        # génère aléatoirement des objets "tir" qui vont de l'alien au bas de l'écran
        global delai_tir_alien
        global nb_tirs_aliens
        while nombre_vies > 0:
            attente = uniform(0.1, 1.9) * delai_tir_alien
            time.sleep(attente)
            nb_tirs_aliens += 1
            numero_tir = nb_tirs_aliens
            nom_tir = 'tir_alien_' + str(numero_tir)
            nom_tir = tir_alien(nom_tir, self.x, self.y)
            nom_tir.lancement()


class vaisseau:
    # classe du vaisseau du joueur
    def __init__(self):
        self.x = 3
        
    def __str__(self):
        return str(joueur)

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
        global nb_tirs_joueur
        nb_tirs_joueur += 1
        numero_tir = nb_tirs_joueur
        nom_tir = 'tir_joueur_' + str(numero_tir)
        nom_tir = tir_joueur(nom_tir, self.x)
        nom_tir.lancement()

    def print_coord(self):
        # affiche les coordonnées du vaisseau du joueur
        print('x=' + str(self.x))

class tir:
    # classe des tirs du joueur
    def __init__(self, nom_tir, x):
        self.x = x
        self.y = y_max
        self.nom = nom_tir
        tirs_en_cours.append(self)

    def __str__(self):
        return str(self.nom)

    def print_coord(self):
        # affiche les coordonnées du tir
        print(self.nom + ' : {' + 'x=' + str(self.x) + ' ; y=' + str(self.y) + '}')



class tir_joueur(tir):
    # sous-classe de la classe tir pour les tirs venant du joueur
    def __init__(self, nom_tir, x):
        super().__init__(nom_tir, x)
    
    def lancement(self):
        # lance le tir depuis la position du joueur et le fait monter jusqu'à toucher un alien ou sortir de l'écran
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



class tir_alien(tir):
    # sous-classe de la classe tir pour les tirs venant des aliens
    def __init__(self, nom_tir, x, y):
        super().__init__(nom_tir, x)
        self.y = y

    def lancement(self):
        # lance le tir depuis la position de l'alien et le fait descendre jusqu'à toucher le joueur ou sortir de l'écran
        global delai_mvt_tir
        global nombre_vies
        joueur_touche = 0
        while joueur_touche == 0 and self.y < y_max:
            self.print_coord()
            time.sleep(delai_mvt_tir)
            self.y += 1
            if joueur.x == self.x and self.y == y_max:
                print('joueur touché !')
                nombre_vies -= 1
        tirs_en_cours.remove(self)
        del self




def nouveau_jeu(nb_aliens):
    for i in range(nb_aliens):
        nom_alien = 'alien_' + str(i + 1)
        nom_alien = alien(nom_alien, 0, 0)
        nom_alien.mouvement()
    joueur = vaisseau()
    joueur.recup_touche()


joueur = vaisseau()
alien_test = alien('alien_test',2,0)
joueur.recup_touche()
'''
print('aliens vivants : ' + str(aliens_vivants))
nouveau_jeu(3)

blob = alien('blob',0,0)
print(blob)
blob.mouvement()
'''
