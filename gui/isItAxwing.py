#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from PIL import Image, ImageTk

lPhotos = ["xwing.jpg", "xwing2.jpg", "dragon.jpg"]
i = 0

def validate():
        global i
        print(i)
        answer= value.get()
        if answer == "":
            print("Merci de répondre")
        else:
            print("Réponse : "+answer)
            i += 1
            print(i)
            
            image = Image.open(lPhotos[i])
            image = image.resize((500,250), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            canvas.create_image(250, 125, image=photo)
            #canvas.configure(image=photo) #Configure
            canvas.image = photo #Changer image
            
            

fenetre = Tk()

label = Label(fenetre, text="Est-ce un X-Wing ?")
label.grid(row=1, column=1, columnspan = 2)

canvas = Canvas(fenetre, width=500, height=250, bg='ivory')
image = Image.open(lPhotos[i])
image = image.resize((500,250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
canvas.create_image(250, 125, image=photo)
canvas.grid(row=2, column=1, columnspan = 2)

# radiobutton
value = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value="Y", indicatoron=0, command=validate)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value="N", indicatoron=0, command=validate)
bouton1.grid(row=3, column=1)
bouton2.grid(row=3, column=2)


#bouton=Button(fenetre, text="Valider", command=validate)
#bouton.grid(row=4, column=1, columnspan = 2)



fenetre.mainloop()
