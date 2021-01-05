'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry, StringVar
# from  tkinter import *

class Spaceship:
    def __init__(self):
        self.x = abscisse
        self.y = ordonnee
        self.body = zone_jeu.create_image(self.x, self.y, anchor = 'center', image = joueurimg)
    
    def print_coord(self):
        # affiche les coordonnées du vaisseau alien
        print('x=' + str(self.x), 'y=' + str(self.y))

    def direction(self,val):
        if (self.x >= 32) and val == -1:
            self.x += speed * val

        elif (self.x <= l - 32) and val == 1:
            self.x += speed * val

        self.maj_position()    

    def maj_position(self):
        zone_jeu.coords(self.body,self.x,self.y)


# def gauche(val):
#     zone_jeu.move(vaisseau.apparence, -10,0)

# def droit(val):
#     zone_jeu.move(vaisseau.apparence, 10,0)

def move(event):
    caractere = event.keysym
    if (caractere == 'q' or caractere == 'Left') and (vaisseau.x - speed > 0):
        vaisseau.direction(-1)
    elif (caractere == 'd' or caractere == 'Right') and (vaisseau.x + speed < l):
        vaisseau.direction(1)


global score
global vie
score = 0
vie = 3
speed = 15
h = 500
l = 800

abscisse = l/2
ordonnee = h - 37

# ========= TK =============

fenetre = Tk()
fenetre.title("SPACE INVADER")
fenetre.geometry("804x600")
# fenetre.resizable(False, False)

backg = PhotoImage(file = 'backg.png')
joueurimg = PhotoImage(file = 'battleship.png')




zone_info = Canvas(fenetre, width = l, height = 50, bg = 'grey')
zone_jeu = Canvas(fenetre, width = l, height = h)
zone_but= Canvas(fenetre, width = l, height = 50)
image_fond = zone_jeu.create_image(250,250,anchor = "c", image = backg)

label_score=Label(zone_info, text = "Score : "+str(score), bg = 'grey')
label_score.place(x = 20 , y = 15)

label_vie=Label(zone_info, text = "Nombre de vies restantes : "+str(vie), bg = 'grey')
label_vie.place(x = 635 , y = 15)

zone_info.grid(row = 0, column = 0, columnspan = 2)
zone_jeu.grid(row = 1, column = 0, columnspan = 2)
zone_but.grid(row = 2, column = 0, columnspan = 2)

but_new=Button(zone_but,text='New Game')
but_quit=Button(zone_but,text='Quit', command=fenetre.destroy)


but_new.grid(row = 3, column = 0)
but_quit.grid(row = 3, column = 1)

vaisseau=Spaceship()
zone_jeu.bind_all('<Left>',move)
zone_jeu.bind_all('<Right>',move)
# zone_jeu.bind_all('<Space>',clavier)


fenetre.mainloop()

