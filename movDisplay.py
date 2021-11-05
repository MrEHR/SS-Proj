# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter
from tkinter import *
from PIL import ImageTk, Image 

window=Tk()
window.title('Movie Selection')
window.geometry('1000x1000')

# Movie Image 
image1 = Image.open("/Users/e.h.ricks/Pictures/champloo wp.png")
image1= image1.resize((400, 400), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.grid(row=1,column=0)

# Movie  Label
ML=Label( text="Movie Playing",font=(16), bg = "black", fg= "white")
ML.grid(row=0,column=0,padx=10,pady=10)

# Recommendation Label
RecLabel = Label( text="Recommended movies to watch",font=(16), bg = "black", fg= "white")
RecLabel.grid(row=2,column=0,padx=10,pady=10)

#Recommended Movie 1 Label
RM1Label = Label( text="Movie 1",font=(16), bg = "black", fg= "white")
RM1Label.grid(row=3,column=0,padx=10,pady=10)

#Recommended Movie 1
RM1 = tkinter.Canvas(window, bg="black", height=100, width=100)
RM1.grid(row=4,column=0, padx=10,pady=10)

#Recommended Movie 1 Button
RM1button=tkinter.Button(text=" Click to Watch")
RM1button.grid(row=5,column=0,padx=10,pady=10)


#Recommended Movie 2 Label
RM2Label = Label( text="Movie 2",font=(16), bg = "black", fg= "white")
RM2Label.grid(row=3,column=1,padx=10,pady=10)

#Recommended Movie 2
RM2 = tkinter.Canvas(window, bg="black", height=100, width=100)
RM2.grid(row=4,column=1, padx=10,pady=10)

#Recommended Movie 2 Button
RM2button=tkinter.Button(text=" Click to Watch")
RM2button.grid(row=5,column=1,padx=10,pady=10)


window.mainloop()
