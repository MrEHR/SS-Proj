#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:14:59 2021

@author: e.h.ricks
"""
import tkinter 
from tkinter import *
from PIL import ImageTk, Image 

 #Class Definition
class Movie:
    #movieButton,movieLabel,openMovie,poster
    def __init__(self,moviePath):
        self.moviePath = moviePath
        
        
    #def buttonCommand():
        

def displayMovie(movieStack,stackSize,count):
      #Label row position
    row_lab=0
    #Label column position
    col_lab=0
    
    #Image row position
    row_img=1
    #Image column position
    col_img=0
    
     #Button row position
    row_but=2
    #Button column position
    col_but=0 
     
    pos_reset=0
    
    #Loop for positioning widgets on the grid
    while count<stackSize: 
    # Open Movie Image
        openMovie = Image.open(movieStack[count].moviePath)
        openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
        poster = ImageTk.PhotoImage(openMovie)
        
        #Display movie  in a label
        movieImage = tkinter.Label(image=poster)
        movieImage.image = poster
        
        # Movie Label
        movieLabel=Label( text="Movie 1",font=(16), bg = "black", fg= "white")
        movieLabel.grid(row=row_lab,column=col_lab,padx=10,pady=10)
        
        # Position image
        movieImage.grid(row=row_img,column=col_img,padx=20,pady=20,ipadx=20,ipady=20)
        
        # Movie Button
        movieButton=tkinter.Button(text=" Click to Watch")
        movieButton.grid(row=row_but,column=col_but,padx=10,pady=10)
        
        row_lab+=1
        row_img+=1
        row_but+=1
        pos_reset+=1
        
        #if pos_reset==3:
            #col_lab+=1
            #col_img+=1
            #col_but+=1
        count+=1     
   
     
        
#############################################################################################
       
window=Tk()
window.title('Movie Selection')
window.geometry('1000x1000')

file=open('/Volumes/EZO-3/iofile.txt','r')
stack=[]
movieStack=[]
stackSize=0
#increment
i=0
for x in file:
    x = x.rstrip()
    stack.append(x)
    movieObj=Movie(stack[i])
    movieStack.append(movieObj)
    stackSize+=1
    i+=1
count=0

displayMovie(movieStack, stackSize, count)


    
   
window.mainloop()