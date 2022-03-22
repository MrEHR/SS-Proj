
"""
Created on Tue Mar  1 12:39:31 2022

@author: Ezra
"""
#3
#This file will take the results from the comparisons and display the recommendations
import tkinter,customtkinter 
from tkinter import Button,Label,Toplevel,Entry
from PIL import ImageTk, Image 
from tkvideo import tkvideo
global openMovie
global movieImage
global poster

import comparison2
from comparison2 import *
class movie_system(file_setup):
    
    stackSize=file_setup.stackSize
    file_path= file_setup.img_file_list
    title_stack=file_setup.title_file_list
    video_stack=file_setup.video_file_list
        
      
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
        button=customtkinter.CTkButton(text="Click Here")
        button_stack.append(button)
        button_stack[f].config(command= lambda f=f : movie_button.button_click(movie_system.file_path[f],movie_system.title_stack[f],movie_system.video_stack[f]))
        
        f+=1
    
    def playMovie(movieVideo):
        movie_window=customtkinter.CTkToplevel(width=1000,height=1000)
        movie_window.title("Playing Movie")
        video_label=Label(movie_window)
        video_label.grid(row=1,column=0)
        
        player = tkvideo(movieVideo,video_label,loop = 1, size = (1280,720))
        player.play()
    def playMovie_Rec(movieRec_vid):
        movie_window=customtkinter.CTkToplevel(width=1000,height=1000)
        movie_window.title("Playing Movie")
        video_label=Label(movie_window)
        video_label.grid(row=1,column=0)
        
        player = tkvideo(movieRec_vid,video_label,loop = 1, size = (1280,720))
        player.play()
    #Button Function for displaying the selected movie window
    def button_click(moviePath,movieTitle,movieVideo,movieRec_title1,movieRec_img1,movieRec_vid1,movieRec_title2,movieRec_img2,movieRec_vid2):
         top = customtkinter.CTkToplevel(width=1000,height=1000)
         top.title("Selected Movie")
         
         openMovie2 = Image.open(moviePath)
         openMovie2= openMovie2.resize((300, 300), Image.ANTIALIAS)
         poster2 = ImageTk.PhotoImage(openMovie2)
             
              #Display movie  in a label
         movieImage2 = tkinter.Label(top,image=poster2)
         movieImage2.image = poster2
         
           #Display Movie
         movieImage2.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)
          
              # Movie Label
         ML=customtkinter.CTkLabel(top,text=movieTitle)
         ML.grid(row=0,column=0,padx=10,pady=10)
         
         play_button=customtkinter.CTkButton(top,text="Click to play", command= lambda : movie_button.playMovie(movieVideo))
         play_button.grid(row=2,column=0)
        #Recommendation Label
         rec_label = customtkinter.CTkLabel(top,text="Recommended movies to watch")
         rec_label.grid(row=3,column=0)
         
          # Recommendation 1
         openMovie2 = Image.open(movieRec_img1)
         openMovie2= openMovie2.resize((150, 200), Image.ANTIALIAS)
         poster2 = ImageTk.PhotoImage(openMovie2)
             
               #Display movie  in a label
         movieImage2 = tkinter.Label(top,image=poster2)
         movieImage2.image = poster2
         
            #Display Movie
         movieImage2.grid(row=5,column=0,padx=20,pady=20,ipadx=20,ipady=20)
          
               # Movie Label
         ML=customtkinter.CTkLabel(top,text=movieRec_title1)
         ML.grid(row=4,column=0,padx=10,pady=10)
         recButton1=customtkinter.CTkButton(top,text="Click", command= lambda : movie_button.playMovie_Rec(movieRec_vid1))
         recButton1.grid(row=6,column=0)
         # #--------------------------------------------------------------------
         # # Recommendation 2
         openMovie2 = Image.open(movieRec_img2)
         openMovie2= openMovie2.resize((150, 200), Image.ANTIALIAS)
         poster2 = ImageTk.PhotoImage(openMovie2)
             
               #Display movie  in a label
         movieImage2 = tkinter.Label(top,image=poster2)
         movieImage2.image = poster2
         
            #Display Movie
         movieImage2.grid(row=5,column=1,padx=20,pady=20,ipadx=20,ipady=20)
          
               # Movie Label
         ML=customtkinter.CTkLabel(top,text=movieRec_title2)
         ML.grid(row=4,column=1,padx=10,pady=10)
         
         recButton2=customtkinter.CTkButton(top,text="Click", command= lambda : movie_button.playMovie_Rec(movieRec_vid2))
         recButton2.grid(row=6,column=1)
         

          
         
        
         
    
 #End of movie_button class----------------------------------------------------------------   
class gui_display(movie_button,comparison,gui):
    def displayMovies(self):
        top=customtkinter.CTkToplevel()
        top.title("Movie Recommendations")

        count=0
      
        
        #Loop for positioning widgets on the grid
        while count<movie_system.stackSize:
            if comparison.simRank[count] == 0:
            
                movie_button.button_stack[count]=customtkinter.CTkButton(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count],movie_system.video_stack[count]
                                                    ,movie_system.title_stack[count+1],movie_system.file_path[count+1],movie_system.video_stack[count+1],movie_system.title_stack[count+2],movie_system.file_path[count+2],movie_system.video_stack[count+2]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=customtkinter.CTkLabel(top,text=movie_system.title_stack[count])
                movieLabel.grid(row=0,column=0,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=1,column=0,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=2,column=0,padx=10,pady=10)
                
            if comparison.simRank[count] == 1:
             
                 movie_button.button_stack[count]=customtkinter.CTkButton(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count],movie_system.video_stack[count]
                                                                                                    ,movie_system.title_stack[count-1],movie_system.file_path[count-1],movie_system.video_stack[count-1],movie_system.title_stack[count+1],movie_system.file_path[count+1],movie_system.video_stack[count+1]))
             # Open Movie Image
                 openMovie = Image.open(movie_system.file_path[count])
                 openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                 poster = ImageTk.PhotoImage(openMovie)
                 
                 #Display movie  in a label
                 movieImage = tkinter.Label(top,image=poster)
                 movieImage.image = poster
                 
                 # Movie Label
                 movieLabel=customtkinter.CTkLabel(top,text=movie_system.title_stack[count])
                 movieLabel.grid(row=0,column=1,padx=10,pady=10)
                 
                 # Position image
                 movieImage.grid(row=1,column=1,padx=20,pady=20,ipadx=20,ipady=20)
                 
                 #position button
                 movie_button.button_stack[count].grid(row=2,column=1,padx=10,pady=10)
            
            if comparison.simRank[count] == 2:
            
                movie_button.button_stack[count]=customtkinter.CTkButton(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count],movie_system.video_stack[count]
                                                                                            ,movie_system.title_stack[count-1],movie_system.file_path[count-1],movie_system.video_stack[count-1],movie_system.title_stack[count-2],movie_system.file_path[count-2],movie_system.video_stack[count-2]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=customtkinter.CTkLabel(top,text=movie_system.title_stack[count])
                movieLabel.grid(row=0,column=2,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=1,column=2,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=2,column=2,padx=10,pady=10)
           
            if comparison.simRank[count] == 3:
            
                movie_button.button_stack[count]=customtkinter.CTkButton(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count],movie_system.video_stack[count]
                                                                                                                ,movie_system.title_stack[count-1],movie_system.file_path[count-1],movie_system.video_stack[count-1],movie_system.title_stack[count-2],movie_system.file_path[count-2],movie_system.video_stack[count-2]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=customtkinter.CTkLabel(top,text=movie_system.title_stack[count])
                movieLabel.grid(row=3,column=0,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=4,column=0,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=5,column=0,padx=10,pady=10)
                
            if comparison.simRank[count] == 4:
            
                movie_button.button_stack[count]=customtkinter.CTkButton(top,text="Click Here",command= lambda count=count : movie_button.button_click(movie_system.file_path[count],movie_system.title_stack[count],movie_system.video_stack[count]
                                                                                                             ,movie_system.title_stack[count-1],movie_system.file_path[count-1],movie_system.video_stack[count-1],movie_system.title_stack[count-2],movie_system.file_path[count-2],movie_system.video_stack[count-2]))
            # Open Movie Image
                openMovie = Image.open(movie_system.file_path[count])
                openMovie= openMovie.resize((250, 300), Image.ANTIALIAS)
                poster = ImageTk.PhotoImage(openMovie)
                
                #Display movie  in a label
                movieImage = tkinter.Label(top,image=poster)
                movieImage.image = poster
                
                # Movie Label
                movieLabel=customtkinter.CTkLabel(top,text=movie_system.title_stack[count])
                movieLabel.grid(row=3,column=1,padx=10,pady=10)
                
                # Position image
                movieImage.grid(row=4,column=1,padx=20,pady=20,ipadx=20,ipady=20)
                
                #position button
                movie_button.button_stack[count].grid(row=5,column=1,padx=10,pady=10)
            
            count+=1
        top.mainloop()
            
#End of displayMovies++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#End of gui_display class-----------------------------------------------------------------------------------
