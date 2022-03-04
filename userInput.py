# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:39:31 2022

@author: Ezra
"""
#1
import nltk, tkinter
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import Button,Label,Toplevel,Entry,Radiobutton
from PIL import ImageTk, Image 


from nltk.corpus import stopwords,wordnet

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

global desc_path
global title_path
global img_path
 
    

#Start of gui class[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
class gui:
   
    window=tkinter.Tk()
    window.title('Movie Selection')
    window.geometry('350x250')
    
    label=Label(window,text="Enter your description")
    entry=Entry(window)
    genre_label=Label(window,text="Enter the genre")
    genre_entry=Entry(window)
    
    
    label.grid(row=0,column=0)
    entry.grid(row=0,column=1)
    genre_label.grid(row=1,column=0)
    genre_entry.grid(row=1,column=1)
        
    check=0
    
    
    
    def run_comp():
       global user_input
       global genre_input
       global desc_path
       global title_path
       global img_path  
       
       user_input=gui.entry.get()
       genre_input= gui.genre_entry.get()
       
       if genre_input == "Action" or genre_input =="action":
           desc_path="C:/Users/Ezra/Desktop/SSP/actionDesc.txt"
           title_path="C:/Users/Ezra/Desktop/SSP/actionTitles.txt"
           img_path="C:/Users/Ezra/Desktop/SSP/actionImg.txt"
           
       if genre_input == "Comedy" or genre_input =="comedy":
           desc_path="C:/Users/Ezra/Desktop/SSP/comedyDesc.txt"
           title_path="C:/Users/Ezra/Desktop/SSP/comedyTitles.txt"
           img_path="C:/Users/Ezra/Desktop/SSP/comedyImg.txt"
           
       gui.check=1
       
    #window.mainloop()
    
    
    
    
#End of gui class |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  

#Start of user_setup[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]  
class user_setup(gui):
    #these lines of code are here because I could not get the button command to work inside of the gui class
    u_button=Button(gui.window,text="click",command= lambda: gui.run_comp())
    u_button.grid(row=2,column=0)
    gui.window.mainloop()
    
    '''this loop will run until the user inputs some data, '''
    while gui.check==0:
        continue
    
    
    stop_words = set(stopwords.words("english"))
    filtered_spec=[]
    
    stemmer = PorterStemmer()
    lematizer = WordNetLemmatizer()
    
    for word in user_input:
        if word.casefold() not in stop_words:
            filtered_spec.append(lematizer.lemmatize(word))
    

#End of user_setup|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    
#Start of file_setup class [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
class file_setup(gui):
    def __init__(self):
        
        self.stemmer=PorterStemmer()
        self.lematizer = WordNetLemmatizer()
    
    file0=open(img_path,'r')
    file1=open(desc_path,'r')
    
    #stack for storing file paths
    file_path=[]
    desc_file=[]
    stackSize=0
    
    stop_words = set(stopwords.words("english"))
    filtered_desc=[]
    
    stemmer = PorterStemmer()
    lematizer = WordNetLemmatizer()
    
    #increment
    i=0
    #this loop is going to store the file path in a class object,
    #then the object will be stored in a stack
    button=Button()
    for desc in file1:
        desc = desc.rstrip()
        desc_words = word_tokenize(desc)
        for word in desc_words:
            if word.casefold() not in stop_words:
                filtered_desc.append(lematizer.lemmatize(word))
        i+=1      
                
    for path in file0:
        path = path.rstrip()
        file_path.append(path)
        stackSize+=1
        i+=1
#End of file_setup class|||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Start of main [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

GUI=gui()
u=user_setup()
file_setup=file_setup()
    
    
    
