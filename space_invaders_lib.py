'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

import time
from random import uniform
import threading
import logging
import tkinter as tk

########## paramètres du jeu ##########

x_max = 5 # largeur de la zone de jeu 
y_max = 5 # hauteur de la zone de jeu
delai_mvt_alien = 1 # délai entre chaque mouvement d'alien
delai_tir_alien = .02 # délai moyen entre les tirs d'un même alien
delai_mvt_tir = .02 # délai entre chaque mouvement de tir
nombre_vies = 3 # nombre de vies du joueur
nombre_aliens = 3 # nombre d'aliens apparaissant dans le jeu

########## initialisation ##########

nb_tirs_joueur = 0
nb_tirs_aliens = 0
tirs_en_cours = []
aliens_vivants = []
logging.basicConfig(level=logging.DEBUG,format='%(threadName)s')



class alien:
    # classe des vaisseaux ennemis
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y
        # la ligne qui suit lance un thread qui exécute les tirs de l'alien, cela permet de faire bouger plusieurs tirs à la fois indépendamment
        threading.Thread(name=str(self.nom) + '_tir_' + str(nb_tirs_aliens), target=self.tir).start()

    def __str__(self):
        return str(self.nom)

    def mouvement(self):
        # fait bouger le vaisseau alien en zig-zag jusqu'en bas de l'écran
        global delai_mvt_alien
        logging.debug(self.print_coord())
        while self.y < y_max:
            while self.x < x_max:
                # l'alien bouge de gauche à droite jusqu'à atteindre le bord droit de l'écran
                time.sleep(delai_mvt_alien)
                self.x += 1
                logging.debug(self.print_coord())
            time.sleep(delai_mvt_alien)
            self.y += 1
            # l'alien descend d'une case
            logging.debug(self.print_coord())
            while self.x > 0:
                # l'alien bouge de droite à gauche jusqu'à atteindre le bord gauche de l'écran
                time.sleep(delai_mvt_alien)
                self.x -= 1
                logging.debug(self.print_coord())
            time.sleep(delai_mvt_alien)
            self.y += 1
            # l'alien descend d'une case
            logging.debug(self.print_coord())
            
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
            nom_tir = str(self.nom) + '_tir_' + str(numero_tir)
            nom_tir = tir_alien(nom_tir, self.x, self.y)
            nom_tir.lancement()



class vaisseau:
    # classe du vaisseau du joueur
    def __init__(self):
        self.x = 3
        
    def __str__(self):
        return str('joueur')

    def recup_touche(self):
        fenetre = tk.Tk()
        fenetre.bind("<Key>", self.action)
        fenetre.mainloop()

    def action(self, touche):
        caractere = touche.char
        if caractere == 'q':
            print('a gauche')
            self.mouvement('gauche')
            logging.debug(self.print_coord())
        elif caractere == 'd':
            print('a droite')
            self.mouvement('droite')
            logging.debug(self.print_coord())
        elif caractere == ' ':
            # la ligne qui suit lance un thread qui exécute le tir du joueur, cela permet de gérer plusieurs tirs indépendamment
            threading.Thread(target=self.tir).start()

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
            logging.debug(self.print_coord())
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
            logging.debug(self.print_coord())
            time.sleep(delai_mvt_tir)
            self.y += 1
            if joueur.x == self.x and self.y == y_max:
                print('joueur touché !')
                nombre_vies -= 1
        tirs_en_cours.remove(self)
        del self



def nouveau_jeu(nb_aliens):
    for i in range(nb_aliens):
        one_alien = alien('alien_' + str(i + 1), 0, 0)
        aliens_vivants.append(one_alien)
        # la ligne qui suit lance un thread qui exécute les mouvements de l'alien, cela permet de faire bouger plusieurs aliens à la fois indépendamment
        threading.Thread(name='thread_alien_' + str(i + 1), target=one_alien.mouvement).start()
    joueur.recup_touche()

joueur = vaisseau()
nouveau_jeu(nombre_aliens)

'''

alien_test_1 = alien('alien_test_1',1,0)
alien_test_2 = alien('alien_test_2',2,0)
alien_test_3 = alien('alien_test_3',3,0)

joueur.recup_touche()
blob = alien('blob',0,0)

print('aliens vivants : ' + str(aliens_vivants))


print(blob)
blob.mouvement()
'''




