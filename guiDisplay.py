# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:39:31 2022

@author: Ezra
"""
#3
#This file will take the results from the comparisons and display the recommendations
import tkinter 
from tkinter import Button,Label,Toplevel,Entry
from PIL import ImageTk, Image 

global openMovie
global movieImage
global poster

import comparison
from comparison import *
class movie_system(file_setup):
    
    stackSize=file_setup.stackSize
    file_path= file_setup.img_file_list
    title_stack=file_setup.title_file_list

        
      
#End of movie_system class--------------------------------------------------------------  

#Start of movie_button class|||||||||||||||||||||||||||||||||||||||||||||||||||
"""This child class is for initializing the buttons on the Movie Selection Window.
Each button will open a Toplevel window that will display the selected movie  """
class movie_button(movie_system):
    def __init__(self):
        super().__init__()
        self.button_stack=[]
    #all of the buttons are contained within this stack   
    button_stack=[]    
    f=0
    
    while f < movie_system.stackSize:
        button=Button(text="Click Here")
        button_stack.append(button)
        button_stack[f].config(command= lambda f=f : movie_button.button_click(movie_system.file_path[f],movie_system.title_stack[f]))
        
        f+=1
            
    #Button Function for displaying the selected movie window
    def button_click(moviePath,movieTitle):
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
         ML=Label(top,text=movieTitle,font=(16), bg = "black", fg= "white")
         ML.grid(row=0,column=0,padx=10,pady=10)
         
         
    
 #End of movie_button class----------------------------------------------------------------   
class gui_display(movie_button,comparison,gui):
    def displayMovies(self):
        top=Toplevel()
        
        count=0
      
        
        #Loop for positioning widgets on the grid
        while count<movie_system.stackSize:
            if comparison.simRank[count] == 0:
            
                movie_button.button_stack[count]=Button(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=Label(top,text=movie_system.title_stack[count],font=(16), bg = "black", fg= "white")
                movieLabel.grid(row=0,column=0,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=2,column=0,padx=10,pady=10)
                
            if comparison.simRank[count] == 1:
             
                 movie_button.button_stack[count]=Button(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count]))
             # Open Movie Image
                 openMovie = Image.open(movie_system.file_path[count])
                 openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                 poster = ImageTk.PhotoImage(openMovie)
                 
                 #Display movie  in a label
                 movieImage = tkinter.Label(top,image=poster)
                 movieImage.image = poster
                 
                 # Movie Label
                 movieLabel=Label(top,text=movie_system.title_stack[count],font=(16), bg = "black", fg= "white")
                 movieLabel.grid(row=0,column=1,padx=10,pady=10)
                 
                 # Position image
                 movieImage.grid(row=1,column=1,padx=20,pady=20,ipadx=20,ipady=20)
                 
                 #position button
                 movie_button.button_stack[count].grid(row=2,column=1,padx=10,pady=10)
            
            if comparison.simRank[count] == 2:
            
                movie_button.button_stack[count]=Button(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=Label(top,text=movie_system.title_stack[count],font=(16), bg = "black", fg= "white")
                movieLabel.grid(row=0,column=2,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=1,column=2,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=2,column=2,padx=10,pady=10)
           
            if comparison.simRank[count] == 3:
            
                movie_button.button_stack[count]=Button(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=Label(top,text=movie_system.title_stack[count],font=(16), bg = "black", fg= "white")
                movieLabel.grid(row=3,column=0,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=4,column=0,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=5,column=0,padx=10,pady=10)
                
            if comparison.simRank[count] == 4:
            
                movie_button.button_stack[count]=Button(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=Label(top,text=movie_system.title_stack[count],font=(16), bg = "black", fg= "white")
                movieLabel.grid(row=3,column=1,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=4,column=1,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=5,column=1,padx=10,pady=10)
         
            count+=1
        top.mainloop()
            
#End of displayMovies++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#End of gui_display class-----------------------------------------------------------------------------------
