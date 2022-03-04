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

"""This class contains the stacks that store the titles and file paths for each movie.  """
class movie_system:
    file=open('C:/Users/Ezra/Desktop/SSP/iofileW.txt','r')
    title_file=open('C:/Users/Ezra/Desktop/SSP/titles.txt','r')
    def __init__(self):
        self.stackSize=0
        self.file_path = []
    stackSize=0
    file_path=[]
    title_stack=[]
    for path in file:
        path = path.rstrip()    
        file_path.append(path)
        stackSize+=1
        
    for title in title_file:
        title = title.rstrip()
        title_stack.append(title)
        
    file.close()
    title_file.close()      
# End of movie_system class--------------------------------------------------------------  

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
         
         demo_label2=Label(text=" Additional Recommended movies will be shown below the displayed movie here",font=10)
         demo_label2.grid(row=2,column=0)
    
 #End of movie_button class----------------------------------------------------------------   
class gui_display(movie_button):
    def displayMovies(self):
        top=Toplevel()
        
        count=0
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
        
        """scrollbar=Scrollbar(top)
        #Scroll bar row position
        row_scroll=0
        #Scroll bar column position
        col_scroll=3"""
        
        #Loop for positioning widgets on the grid
        while count<movie_system.stackSize:
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
            movieLabel.grid(row=row_lab,column=col_lab,padx=10,pady=10)
            
            # Position image
            movieImage.grid(row=row_img,column=col_img,padx=20,pady=20,ipadx=20,ipady=20)
            
            #position button
            movie_button.button_stack[count].grid(row=row_but,column=col_but,padx=10,pady=10)
           
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
        demo_label=Label(top,text="After a movie is selected, it will be displayed on the next page",font=15)
        demo_label.grid(row=2,column=3)
#End of displayMovies++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#End of gui_display class-----------------------------------------------------------------------------------

#Main
window=tkinter.Tk()
window.title('Movie Selection')

window.geometry('900x200')


file_path=[]
stackSize=0
start_button=Button(window,text="Enter", command = lambda : start_func())
start_button.grid(row=2,column=0)
start_label=Label(window,text="The User will enter their description into a text field. The movies recommended by the system will display on the next page",font = 15)
start_label.grid(row=0,column=0)
start_field= Entry(window)
start_field.grid(row=1,column=0)    
def start_func():   
    startup=movie_system()

    mov_but=movie_button()
    
    gui=gui_display()
    gui.displayMovies()


window.mainloop()
