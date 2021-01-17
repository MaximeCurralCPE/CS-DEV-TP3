'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020

To Do:
- Modifier les défenses pour qu'elles se détruisent au fur et à mesure des dégats
- Rajouter une ligne d'aliens
- Différents niveaux (boss?)
- cheat codes
- réquilibrer les vitesses
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry, StringVar
from random import randint, uniform
from time import time

gamestatus = False
gamelost = True
nombre_vies = 3

# Zone de jeu
zj_width = 800
zj_height = 600

'''
Paramètres de vaisseau joueur
'''
nombre_vies = 3

# Taille hitbox vaisseau
shipwidth = 32
shipheight = 32

# Position initial vaisseau
position_X = zj_width/2
position_Y = zj_height-shipheight-5

# Vitesse de déplacement
speed = 10

'''
Paramètres des aliens
'''
# Taille hitbox alien
alienwidth = 30      
alienheight = 21

# Paramètres de positionnement des aliens
aliengap = 15
position_ligne1 = 50
nb_ennemis = 15
nb_ligne = 2

# Paramètres de déplacement des aliens
pas = 10
alienspeed = 0.3
acceleration = 0.05

'''
Paramètres des défenses
'''
# Blocs de défenses
nbshield = 4
posY_shield = position_Y - 75
shieldwidth = 2 * shipwidth
shieldheight = 20
shield_hp = 7

'''
Paramètres des tirs alliés et ennemies
'''
# vitesse balles
bulletvelocity = 2

bullets = []
bulletdelayalien = 1000

playershoot_time = 0
alienbullets = []
shootdelay = .8

'''
Score et points
'''
score = 0
valeur = 25


class player:
    def __init__(self):
        # Définit les positions et création de l'apparance avec la hitbox
        self.x = position_X
        self.y = position_Y
        self.body = zone_jeu.create_image(self.x, self.y, anchor = 'center', image = joueurimg)

    def movement(self,val):
        # Déplacement du joueur avec les conditions limites pour ne pas sortir de la zone de jeu
        # Déplacement à Gauche
        if self.x >= (shipwidth/2) + 10 and val == -1:
            self.x += speed * val

        # Déplacement à droite
        elif self.x <= zj_width - ((shipwidth/2) + 10) and val == 1:
            self.x += speed * val
        
        # Met à jour l'affichage de la position du joueur
        self.maj_position()
        
    def maj_position(self):
        # Déplace l'affichage du joueur à la nouvelle position (x,y)
        zone_jeu.coords(self.body, self.x, self.y)
          
    def gettinghit(self):
        # Changement d'état visuel du joueur lorsqu'il est touché par l'invader
        zone_jeu.itemconfig(self.body, image = joueurimg_hit)
        print('[CONSOLE LOG] Player got hit')
        fenetre.after(500, self.is_Ok)
        
    def is_Ok(self):
        # Changement d'état visuel du joueur lorsqu'il revient à la normale
        zone_jeu.itemconfig(self.body, image = joueurimg)


class shoot:
    cpt = 0
    def __init__(self):
        # Création de la balle au niveau du joueur
        self.x = vaisseau.x
        self.y = vaisseau.y
        self.body = zone_jeu.create_line(self.x, self.y-4 , self.x, self.y, fill = 'white', width=5)
        self.bulletstatus = True
        shoot.cpt += 1
    
    def maj_position(self):
        # Déplace l'affichage de la balle à la nouvelle position (x,y)
        zone_jeu.coords(self.body , self.x, self.y-4, self.x, self.y)
    
    def movement(self):
        # Déplacement de la balle
        if self.bulletstatus:
            self.y -= bulletvelocity
            self.maj_position()
            self.hitregister()
            fenetre.after(5, self.movement)
      
    def hitregister(self):
        # Detection de la balle lorsqu'elle sort de la zone de jeu et lorsqu'elle touche
        if self.y < 0:
            self.bulletstatus = False
            zone_jeu.delete(self.body)
            del bullets[0]
            shoot.cpt -= 1
        # Detection de la balle lorsqu'elle touche
        else:
            for i in liste_invader:
                if i.vivant and self.y >= i.y and self.y <= i.y + alienheight and self.x <= i.x + alienwidth and self.x >= i.x:
                    self.remove()
                    print("[CONSOLE LOG] An alien got hit")
                    zone_jeu.delete(i.body)
                    i.vivant = False
                    invader.vitesse += acceleration
                    set_points(valeur)
                    win()

    def remove(self):
        # Destruction de la balle
        self.bulletstatus = False
        zone_jeu.delete(self.body)
        del bullets[0]
        shoot.cpt -= 1


class invader:
    cpt = 0
    def __init__(self):
        invader.cpt += 1
        self.cpt = invader.cpt
        self.vivant = True
        self.x = self.cpt * (aliengap + alienwidth)
        invader.y = position_ligne1
        invader.val = 1
        invader.vitesse = alienspeed
    
    def Creation(self,alea):
        # Création de l'apparence de l'invader
        self.body = zone_jeu.create_image(self.x, self.y, anchor = 'nw', image = alea)

    def maj_position(self):
        # Déplace l'affichage de l'invader à la nouvelle position (x,y)
        zone_jeu.coords(self.body, self.x, self.y)
    

class shootinvader:
    def __init__(self,i):
        # Création de la balle au niveau de l'invader
        self.x = liste_invader[i].x
        self.y = liste_invader[i].y
        self.body = zone_jeu.create_line(self.x, self.y-4, self.x, self.y, fill = 'lightgreen', width=5)
        self.bulletstatus = True
        self.movement()

    def maj_position(self):
        # Déplace l'affichage de la balle de l'invader à la nouvelle position (x,y)
        zone_jeu.coords(self.body, self.x, self.y-4, self.x, self.y)
        
    def movement(self):
        # Déplacement de la balle de l'invader
        if self.bulletstatus:
            self.y += bulletvelocity
            self.maj_position()
            self.hitregister()
            fenetre.after(5, self.movement)
    
    def hitregister(self):
        global vies
        # Detection de la balle lorsqu'elle sort de la zone de jeu et lorsqu'elle touche
        if self.y > zj_height:
            self.bulletstatus = False
            zone_jeu.delete(self.body)
            del alienbullets[0]
            
        # Detection de la balle lorsqu'elle touche le joueur
        elif self.y >= vaisseau.y - 5 and self.y <= vaisseau.y + 5 and self.x <= vaisseau.x + shipwidth/2 and self.x >= vaisseau.x - shipwidth/2:
            self.bulletstatus = False
            zone_jeu.delete(self.body)
            del alienbullets[0]
            vies -= 1
            vaisseau.gettinghit()
            display_lives(vies)
            if vies == 0:
                lose()
        # Detection de la balle lorsqu'elle touche les défenses
        else:
            for i in defenses:
                if i.shield > 0 and self.x >= i.x and self.x <= i.x + shieldwidth and self.y >= defense.y and self.y <= defense.y + shieldheight:
                    i.majdefense()
                    print("[CONSOLE LOG] Aliens hit a shield")
                    self.bulletstatus = False
                    zone_jeu.delete(self.body)
                    del alienbullets[0]
        
class defense:
    cpt = 0
    def __init__(self):
        # Création des défences 
        defense.cpt += 1
        self.cpt = defense.cpt
        self.x = 740 * self.cpt/(nbshield+1)
        defense.y = posY_shield
        self.shield = shield_hp
        self.body = zone_jeu.create_rectangle(self.x, self.y, self.x + shieldwidth, self.y + shieldheight, width = 2, outline = 'black', fill = 'white')
        
    def majdefense(self):
        # Mise à jour de la vie de la défense
        self.shield -= 1
        # La défense change de couleur selon le nombre de vies restants
        if self.shield > 0:
            if self.shield == 6:
                zone_jeu.itemconfig(self.body, fill = "magenta")
            elif self.shield == 5:
                zone_jeu.itemconfig(self.body, fill = "blue")
            elif self.shield == 4:
                zone_jeu.itemconfig(self.body, fill = "cyan")
            elif self.shield == 3:
                zone_jeu.itemconfig(self.body, fill = "green")
            elif self.shield == 2:
                zone_jeu.itemconfig(self.body, fill = "yellow")
            elif self.shield == 1:
                zone_jeu.itemconfig(self.body, fill = "red")
        else:
            self.remove()
    
    def remove(self):
        # Destruction de la défense
        zone_jeu.delete(self.body)





def invadermovement():
    global liste_invader
    # Déplacement automatique des invaders
    if gamestatus:
        L = [i.vivant for i in liste_invader]
        if True in L:
            i = L.index(True)
            L.reverse()
            j = L.index(True)
            if (liste_invader[-j-1].x + alienwidth >= zj_width and invader.val == 1) or (liste_invader[i].x - 7 <= 0 and invader.val == -1):
                invader.val *= -1
                invader.y += pas
                if invader.y + alienheight/2 >= defense.y:
                    lose()
            for i in liste_invader:
                i.x += invader.vitesse * invader.val
                i.maj_position()  
            fenetre.after(5, invadermovement)

def removebullets():
    # Suprresion des balles
    for i in bullets:
        i.bulletstatus = False
    for i in alienbullets:
        i.bulletstatus = False

def invadershoot():
    global liste_invader,alienbullets 
    # Generation des tirs des invaders
    if gamestatus:
        L = [i.vivant for i in liste_invader]
        i = randint(0, len(liste_invader)-1)
        if L[i]:
            alienbullets.append(shootinvader(i))
            fenetre.after(bulletdelayalien, invadershoot)
        else:
            fenetre.after(1, invadershoot)
      
            
def display_lives(vies):
    # Affichage du nombres de vies restants en cours
    label_vie.config(text = 'Vies : ' + str(vies))
    
    
def Clavier(event):
    global playershoot_time

    # Récupération des touches entrées par le joueur
    keyregister = event.keysym

    # Gauche : q ou fleche_gauche
    if keyregister ==  'q' or keyregister == 'Left':
        vaisseau.movement(-1)
        print('[P] Going left')

    # Droite : d ou fleche_droite
    elif keyregister == 'd' or keyregister == 'Right':
        vaisseau.movement(1)
        print('[P] Going right')

    # Tir : espace
    elif keyregister == 'space':
        playershoot_time1 = time()
        if playershoot_time1 - playershoot_time >= shootdelay or bullets == []:
            playershoot_time = playershoot_time1
            tir = shoot()
            bullets.append(tir)
            bullets[shoot.cpt-1].movement()
            print('[P] Player shoots')

def win():
    global gamestatus, gamelost
    # Définit quand la partie est gagnée 
    gagne = True
    for i in liste_invader:
        if i.vivant:
            gagne = False
    # Affichage d'un message à la place de la zone de jeu et apparition du bouton pour rejouer
    if gagne:
        label_gp.config(text = 'Félicitations ! Pas mal de chances .. ( ͡° ͜ʖ ͡°)')
        label_gp.grid()
        zone_jeu.delete("all")
        but_play.grid()
        but_play.config(text = 'Continuer')
        invader.vitesse = alienspeed
        gamestatus = False
        removebullets()
        gamelost = False

def lose():
    global gamestatus, gamelost
    # Définit quand la partie est perdue
    # Affichage d'un message à la place de la zone de jeu et apparition du bouton pour rejouer
    label_gp.config(text = 'Alors comme ça on a perdu..? ( ͡° ͜ʖ ͡°)')
    label_gp.grid()

    zone_jeu.delete("all")

    but_play.grid()
    but_play.config(text = 'Rejouer')

    invader.vitesse = alienspeed
    removebullets()
    gamestatus = False
    gamelost = True
    
    
def play():
    global liste_invader, vaisseau, gamestatus, score, vies, defenses
    # Initialise une partie
    zone_jeu.grid()
    zone_jeu.create_image(0,0,anchor='nw',image = backg)

    label_gp.grid_remove()
    but_play.grid_remove()

    vaisseau = player()
    print('[CONSOLE LOG] Game started')

    defense.cpt = 0
    defenses = [defense() for i in range(nbshield)]

    gamestatus = True

    if gamelost:
        vies = nombre_vies
        score = 0
        label_score.config(text = 'Score : '+str(score))

    liste_invader = []
    display_lives(vies)
    invader.cpt = 0

    for i in range(nb_ennemis):
        liste_invader.append(invader())

    for i in liste_invader:
        nb = randint(0,4)
        alea_alien = liste[nb]
        i.Creation(alea_alien)

    invadermovement()
    invadershoot()

def set_points(pts):
    # Attribution des points et affichage
    global score
    score += pts
    label_score.config(text = 'Score : ' + str(score))

def quit():
    # Quitte la fenetre
    fenetre.destroy()
    print('[CONSOLE LOG] Game quitted')

'''
--------- Espace Tkinter ---------
'''
# Création de la fenêtre
fenetre = Tk()
fenetre.title("SPACE INVADER")
fenetre.geometry("804x685")
fenetre.resizable(False, False)

# Importation des ressources images
joueurimg = PhotoImage(file = 'battleship.png')
joueurimg_hit = PhotoImage(file = 'battleship_hit.png')
alienimg = PhotoImage(file = 'Invader.png')
alienimg2 = PhotoImage(file = 'Invader2.png')
alienimg3 = PhotoImage(file = 'Invader3.png')
alienimg4 = PhotoImage(file = 'Invader4.png')
alienimg5 = PhotoImage(file = 'Invader5.png')
liste = [alienimg, alienimg2, alienimg3, alienimg4, alienimg5]
backg = PhotoImage(file = 'backg.png')
backg2 = PhotoImage(file = 'Planets.png')

# Zone supérieure possedant les informations du score et des vies restantes
zone_info = Canvas(fenetre, width = zj_width, height = 50, bg = 'grey')
zone_info.grid(row = 0, column = 0, columnspan = 2)

label_score= Label(zone_info, text = 'Score : 0',  bg = 'grey', fg = 'white')
label_score.place(x = 20 , y = 18)

label_vie= Label(zone_info,text = "Vies : 3",  bg = 'grey', fg = 'white')
label_vie.place(x = 745 , y = 18)

# Zone centrale avec le cadre du jeu
zone_jeu = Canvas(fenetre, height = zj_height, width = zj_width, highlightthickness=0)
zone_jeu.grid(row = 2, column = 0, columnspan = 2)
zone_jeu.create_image(0, 0, anchor = 'nw', image = backg2)
zone_jeu.focus_set()
zone_jeu.bind('<Key>',Clavier)

label_gp = Label(fenetre, text = 'Bravo !')
label_gp.grid(row = 2, column = 0, columnspan = 2)
label_gp.grid_remove()

# Zone inférieure pour les boutons
zone_but = Canvas(fenetre, width = zj_width, height = 50)
zone_but.grid(row = 5, column = 0, columnspan = 2, pady= 3)

but_play = Button(zone_but, text = 'Jouer' , command = play)
but_quit = Button(zone_but, text = 'Quitter', command = quit)

but_play.grid(row = 3, column = 0)
but_quit.grid(row = 3, column = 1)

fenetre.mainloop()