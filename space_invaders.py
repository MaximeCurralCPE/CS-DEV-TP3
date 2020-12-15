'''
Sujet : CS-DEV TP 3 : space invaders
Auteur : Maxime Curral & Hien Nguyen
Date de creation : 15/12/2020
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry


# ====== code ============





# ========= TK =============

fenetre = Tk()
fenetre.title("SPACE INVADER")
fenetre.geometry("800x600")
fenetre.resizable(False, False)

backg=PhotoImage(master=fenetre, file='bg.jpg')


Canevas=Canvas(fenetre, height= 500, width=700)
item = Canevas.create_image(150,150,image=backg)
Canevas.grid(row=1,rowspan=6)

fenetre.mainloop()

