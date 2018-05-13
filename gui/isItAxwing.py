#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from PIL import Image, ImageTk
import boto3
from io import BytesIO

#lPhotos = ['1.png', '2.jpg', '3.jpg']
i = 0

s3 = boto3.resource('s3')
bucket = s3.Bucket('deeplens-xwing')
bucket_prefix="train"
lPhotos = iter(bucket.objects.filter(
    Prefix = bucket_prefix))

def load():
    global i
    print(i)
    key = next(lPhotos)
    while key.key[-1] == '/' or '.lst' in key.key:
        key = next(lPhotos)
    i += 1
    obj_body = key.get()['Body'].read()
    image = Image.open(BytesIO(obj_body))
    image = image.resize((500,250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(250, 125, image=photo)
    canvas.image = photo #Changer image

def validate():
    global i
    print(i)
    answer= value.get()
    if answer == "":
        print("Merci de répondre")
    else:
        print("Réponse : "+answer)
    load()        
            
            

fenetre = Tk()

label = Label(fenetre, text="Est-ce un X-Wing ?")
label.grid(row=1, column=1, columnspan = 2)

canvas = Canvas(fenetre, width=500, height=250, bg='ivory')
load()
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
