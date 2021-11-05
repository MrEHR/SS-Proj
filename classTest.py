#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:42:08 2021

@author: e.h.ricks
"""
import tkinter 
from tkinter import *
from PIL import ImageTk, Image 

# Class Definition
class Movie:
    #movieButton,movieLabel,openMovie,poster
    def __init__(self,moviePath):
        self.moviePath = moviePath
        
        
    def showMovie(self):
        # Open Movie Image
        openMovie = Image.open(self.moviePath)
        openMovie= openMovie .resize((250, 300), Image.ANTIALIAS)
        poster = ImageTk.PhotoImage(openMovie)
        
        #Display movie  in a label
        movieImage = tkinter.Label(image=poster)
        movieImage.image = poster
        
        # Position image
        movieImage.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)
        
        # Movie Label
        movieLabel=Label( text="Movie 1",font=(16), bg = "black", fg= "white")
        movieLabel.grid(row=0,column=0,padx=10,pady=10)
        
        # Movie Button
        movieButton=tkinter.Button(text=" Click to Watch")
        movieButton.grid(row=2,column=0,padx=10,pady=10)
       
window=Tk()
window.title('Movie Selection')
window.geometry('1000x1000')

movieTest = Movie("/Volumes/EZO-3/1917.jpeg")
movieStack=[]
movieStack.append(movieTest)
movieStack[0].showMovie()



window.mainloop()
        
        