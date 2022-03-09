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

import untitled4
from untitled4 import gui, user_setup, file_setup
#from untitled4 import *
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
        
    simList = [0,0,0,0,0]
    simComp = [0,0,0,0,0]
    simRank = [0,0,0,0,0]
    n=0
    t=0
    # sim_var=sim()
    # while t < 5:
    #     simList[t]=sim_var
    #     t+=1
    
    while n < 5:
        simList[n] = input_desc.similarity(mov_desc[n])
        simComp[n] = input_desc.similarity(mov_desc[n])
        n+=1
    simComp.sort(reverse=True)    
    print("Comparison complete")
    n=0

    while t < 5:
        if simList[t]==simComp[n]:
            simRank[t]=n
            print(simRank[t])
            n=0
            t+=1
        else: 
            n+=1
               


