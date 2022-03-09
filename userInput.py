# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:39:31 2022

@author: Ezra
"""
#1
import nltk, tkinter
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import Button,Label,Toplevel,Entry
from PIL import ImageTk, Image 


from nltk.corpus import stopwords,wordnet

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


    

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
    
    
    def quick_input():
        gui.entry.insert(0,"action")
        gui.genre_entry.insert(0,"action")

        
    def run_comp():
       global user_input
       global genre_input
       global desc_path
       global title_path
       global img_path  
       
       user_input=gui.entry.get()
       genre_input= gui.genre_entry.get()
       
       if genre_input == "Action" or genre_input =="action":
           desc_path="D:/SP/movieRec/actionDesc.txt"
           title_path="D:/SP/movieRec/actionTitles.txt"
           img_path="D:/SP/movieRec/actionImg.txt"
           
       if genre_input == "Comedy" or genre_input =="comedy":
           desc_path="D:/SP/movieRec/comedyDesc.txt"
           title_path="D:/SP/movieRec/comedyTitles.txt"
           img_path="D:/SP/movieRec/comedyImg.txt"
           
       gui.check=1
       
    #window.mainloop()
    
    
    
    
#End of gui class |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  

#Start of user_setup[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]  
class user_setup(gui):
    #these lines of code are here because I could not get the button command to work inside of the gui class
    u_button=Button(gui.window,text="click",command= lambda: gui.run_comp())
    u_button.grid(row=2,column=0)
    q_button=Button(gui.window,text="quick",command= lambda: gui.quick_input())
    q_button.grid(row=3,column=0)
    #MAINLOOP
    gui.window.mainloop()
    
    '''this loop will run until the user inputs some data, '''
    while gui.check==0:
        continue
    
    
    stop_words = set(stopwords.words("english"))
    filtered_spec=""
    
    stemmer = PorterStemmer()
    lematizer = WordNetLemmatizer()
    
    for word in user_input:
        if word.casefold() not in stop_words:
            filtered_spec+=lematizer.lemmatize(word)
    

#End of user_setup|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    
#Start of file_setup class [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
class file_setup(gui):
    def __init__(self):
        
        self.stemmer=PorterStemmer()
        self.lematizer = WordNetLemmatizer()
    
    opened_img_file=open(img_path,'r')
    opened_desc_file=open(desc_path,'r')
    opened_title_file=open(title_path,'r')
    
    #stack for storing file paths
    img_file_list=[]
    title_file_list=[]
    desc_file=[]
    stackSize=0
    
    stop_words = set(stopwords.words("english"))
    filtered_desc=["","","","",""]
    stemmer = PorterStemmer()
    lematizer = WordNetLemmatizer()
    
    #increment
    i=0
    #this loop is going to store the file path in a class object,
    #then the object will be stored in a stack
    button=Button()
    for desc in opened_desc_file:
        desc = desc.rstrip()
        desc = word_tokenize(desc)
        
        for word in desc:
            if word.casefold() not in stop_words:
                
                filtered_desc[i]+=" "+ lematizer.lemmatize(word)
        #filtered_desc[i]= filtered_desc[i].split()
        i+=1      
               
    for path in opened_img_file:
        path = path.rstrip()
        img_file_list.append(path)
        stackSize+=1
    
    for path in opened_title_file:
        path = path.rstrip()
        title_file_list.append(path)
        
        
#End of file_setup class|||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Start of main [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    
