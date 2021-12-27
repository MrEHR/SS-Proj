# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:41:04 2021

@author: Ezra
"""

import tkinter 
from tkinter import *
from PIL import ImageTk, Image 
global openMovie2
global movieImage2
global poster2
 #Class Definition
class Movie:
    def __init__(self,moviePath,movieButton):
        self.moviePath = moviePath
        self.movieButton= movieButton
       
    
        

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
        
        #position button
        movieStack[count].movieButton.grid(row=row_but,column=col_but,padx=10,pady=10)
       
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
#Button Function for displaying the second window
def button_click(moviePath):
    top = Toplevel(width=1000,height=1000)
  
    # Open Movie Image
    openMovie2 = Image.open(moviePath)
    openMovie2= openMovie2.resize((250, 300), Image.ANTIALIAS)
    poster2 = ImageTk.PhotoImage(openMovie2)
        
        #Display movie  in a label
    movieImage2 = tkinter.Label(top,image=poster2)
    movieImage2.image = poster2
    
     #Display Movie
    movieImage2.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)
     
        # Movie Label
    ML=Label(top,text="Movie Playing",font=(16), bg = "black", fg= "white")
    ML.grid(row=0,column=0,padx=10,pady=10)
    
   
 
   
        
#############################################################################################   
window=Tk()
window.title('Movie Selection')
window.geometry('1300x1300')

file=open('D:/iofileW.txt','r')
#stack for storing file paths
file_path=[]
#stack for storing Movie Objects
movieStack=[]
stackSize=0
#increment
i=0
#this loop is going to store the file path in a class object,
#then the object will be stored in a stack
button=Button()
for path in file:
    print(path)
    path = path.rstrip()
    movieObj=Movie(path,button)
    movieStack.append(movieObj)
    movieStack[i].movieButton = Button(text="Click",command = lambda : button_click(path))
    stackSize+=1
    i+=1
count=0



displayMovie(movieStack, stackSize, count)


    
   
window.mainloop()
