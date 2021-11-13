#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#I was able to get the other images to show, I just needed a larger window.
#I think if I add a scroll bar,it should be fine(no promises)
#Also I gotta get them positioned properly 
#I forgot to add a function for a button opening the displayed movie window
#(I mean the window after you select a movie to watch)
#The movie labels are all still the same, I gotta fix that
"""
Created on Sat Oct 23 12:14:59 2021

@author: e.h.ricks
"""
import tkinter 
from tkinter import *
from PIL import ImageTk, Image 

 #Class Definition
class Movie:
    def __init__(self,moviePath):
        self.moviePath = moviePath
        
        

        

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
    
    scrollbar=Scrollbar(window)
    #Scroll bar row position
    row_scroll=0
    #Scroll bar column position
    col_scroll=3
    
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
        #position button
        movieButton.grid(row=row_but,column=col_but,padx=10,pady=10)
        
        col_lab+=1
        col_img+=1
        col_but+=1
        
        pos_reset+=1
        
        
        if pos_reset==3:
            pos_reset=0
            row_lab+=3
            row_img+=3
            row_but+=3
            
            col_lab=0
            col_img=0
            col_but=0
        count+=1     
   
     
        
#############################################################################################
       
window=Tk()
window.title('Movie Selection')
window.geometry('2000x2000')

file=open('/Volumes/EZO-3/iofile.txt','r')
#stack for storing file paths
file_path=[]
#stack for storing Movie Objects
movieStack=[]
stackSize=0
#increment
i=0
#this loop is going to store the file path in a class object,
#then the object will be stored in a stack
for x in file:
    x = x.rstrip()
    movieObj=Movie(x)
    movieStack.append(movieObj)
    stackSize+=1
    i+=1
count=0

displayMovie(movieStack, stackSize, count)


    
   
window.mainloop()
