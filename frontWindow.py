# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:20:27 2021

@author: Ezra
"""

import tkinter 
from tkinter import *
from PIL import ImageTk, Image 

window=Tk()
window.title('Movie Selection')
window.geometry('1000x1000')

# Open Movie 1 
moviePath="/Volumes/EZO-3/1917.jpeg"
open_movie1 = Image.open(moviePath)
open_movie1 = open_movie1 .resize((250, 300), Image.ANTIALIAS)
poster1 = ImageTk.PhotoImage(open_movie1)

#Display movie 1 in a label
movie_image1 = tkinter.Label(image=poster1)
movie_image1.image = poster1

# Position image
movie_image1.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)

# Movie 1 Label
L1=Label( text="Movie 1",font=(16), bg = "black", fg= "white")
L1.grid(row=0,column=0,padx=10,pady=10)

# Movie 1 Button
M1button=tkinter.Button(text=" Click to Watch")
M1button.grid(row=2,column=0,padx=10,pady=10)
#############################################

# Open Movie 2
open_movie2 = Image.open("/Volumes/EZO-3/wolv.jpeg")
open_movie2 = open_movie2 .resize((250, 300), Image.ANTIALIAS)
poster2 = ImageTk.PhotoImage(open_movie2 )

# Display Movie 2 in a label
movie_image2 = tkinter.Label(image=poster2)
movie_image2.image = poster2
# Position image
movie_image2.grid(row=1,column=1,padx=20,pady=20,ipadx=20,ipady=20)

# Movie 2 Label
L2=Label( text="Movie 2",font=(16), bg = "black", fg= "white")
L2.grid(row=0,column=1,padx=10,pady=10)

# Movie 2 Button
M2button=tkinter.Button(text=" Click to Watch")
M2button.grid(row=2,column=1,padx=10,pady=10)
###############################################

# Open movie3 
open_movie3 = Image.open("/Volumes/EZO-3/ironm.jpeg")
open_movie3= open_movie3.resize((250, 300), Image.ANTIALIAS)
poster3 = ImageTk.PhotoImage(open_movie3)

#Display movie3 in a label
movie_image3 = tkinter.Label(image=poster3)
movie_image3.image = poster3

# Position image
movie_image3.grid(row=1,column=2,padx=20,pady=20,ipadx=20,ipady=20)

# Movie 3 Label
L3=Label( text="Movie 3",font=(16), bg = "black", fg= "white")
L3.grid(row=0,column=2,padx=10,pady=10)

# Movie 3 Button
M3button=tkinter.Button(text=" Click to Watch")
M3button.grid(row=2,column=2,padx=10,pady=10)



window.mainloop()