# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:39:31 2022

@author: Ezra
"""
#2
#This file will take the input from the user and the files to do the comparisons

import nltk, tkinter,string
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import Button,Label,Toplevel,Entry
from PIL import ImageTk, Image 


from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer

import spacy

import userInput2
from userInput2 import gui, user_setup, file_setup

class sim:
    simScore=0
    
class comparison(user_setup,file_setup):
    nlp = spacy.load('en_core_web_md')
    input_desc = nlp(user_setup.filtered_spec)
    
    b=0
    mov_desc=["","","","",""]
    while b < 5:
        mov_desc[b]=nlp(file_setup.filtered_desc[b])
        b+=1
        
    simList = [0,0,0,0,0]#this contains the similarity scores
    simComp = [0,0,0,0,0]#this contains a sorted list of the scores
    simRank = [0,0,0,0,0]#this contains the movie ranks
    n=0
    t=0
   
    
    while n < 5:
        simList[n] = input_desc.similarity(mov_desc[n])
        simComp[n] = input_desc.similarity(mov_desc[n])
        n+=1
    simComp.sort(reverse=True)# sorts the list from highest to lowest    
    print("Comparison complete")
    n=0


    while t < 5:
        if simList[t]==simComp[n]: #if a movies score is the same as the value stored in simComp, then its position in simComp is its rank
            simRank[t]=n           #Ex: A has the same value has simComp[2], so its rank is 2
            print(simRank[t])
            n=0
            t+=1
        else: 
            n+=1
               

