'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry, StringVar
# from  tkinter import *

global score
global vie
score = 0
vie = 3

h = 500
l = 800

def gauche(val):
    zone_jeu.move(joueur, -10,0)

def droit(val):
    zone_jeu.move(joueur, 10,0)

# ========= TK =============

fenetre = Tk()
fenetre.title("SPACE INVADER")
fenetre.geometry("804x600")
# fenetre.resizable(False, False)

backg = PhotoImage(file = 'backg.png')
joueurimg = PhotoImage(file = 'joueur.gif')

h = 500
l = 800


zone_info = Canvas(fenetre, width = l, height = 50, bg = 'grey')
zone_jeu = Canvas(fenetre, width = l, height = h)
zone_but= Canvas(fenetre, width = l, height = 50)
image_fond = zone_jeu.create_image(250,250,anchor = "c", image = backg)
joueur = zone_jeu.create_image(l/2, l/2, image = joueurimg)

zone_jeu.bind_all('<Left>',gauche)
zone_jeu.bind_all('<Right>',droit)

label_score=Label(zone_info, text = "Score : "+str(score), bg = 'grey')
label_score.place(x = 20 , y = 15)

label_vie=Label(zone_info, text = "Nombre de vies restantes : "+str(vie), bg = 'grey')
label_vie.place(x = 635 , y = 15)

zone_info.grid(row = 0, column = 0, columnspan = 2)
zone_jeu.grid(row = 1, column = 0, columnspan = 2)
zone_but.grid(row = 2, column = 0, columnspan = 2)

but_new=Button(zone_but,text='New Game')
but_quit=Button(zone_but,text='Quit', command=fenetre.destroy)

# backg=PhotoImage(master=fenetre, file='backg.png')



# zone_jeu = Canvas(fenetre, height= 550, width=800)
# item = zone_jeu.create_image(0,600,image=backg)

# # score=StringVar()
# # score.set("Score : "+str(score))




# zone_info.grid(row=1)
# zone_jeu.grid(row=2,rowspan=6,column=1,columnspan=2)

but_new.grid(row = 3, column = 0)
but_quit.grid(row = 3, column = 1)

fenetre.mainloop()

