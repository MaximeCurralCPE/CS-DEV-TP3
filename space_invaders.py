'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry, StringVar
# from  tkinter import *

# ========= TK =============

fenetre = Tk()
fenetre.title("SPACE INVADER")
fenetre.geometry("817x610")
fenetre.resizable(False, False)

backg=PhotoImage(master=fenetre, file='backg.png')

h = 550
w = 800
Canevas=Canvas(fenetre, height= h, width=w)
item = Canevas.create_image(0,600,image=backg)

score=StringVar()
score.set("Score : "+str(score))
label_score=Label(fenetre)

but_new=Button(fenetre,text='New Game')
but_quit=Button(fenetre,text='Quit', command=fenetre.destroy)

label_score.grid(row=1)
Canevas.grid(row=2,rowspan=6,column=1,columnspan=2)
but_new.grid(row=9, column=1)
but_quit.grid(row=9,column=2)

fenetre.mainloop()

