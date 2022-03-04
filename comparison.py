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


from nltk.corpus import stopwords,wordnet, PlaintextCorpusReader
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# import userInput
# from userInput import *

# These strings need to be replaced with the input from the user and the desc files
input_desc= "havoc."
input_desc=input_desc.translate(str.maketrans('','',string.punctuation))#removes punctuation from the string
mov_desc= "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
mov_desc=mov_desc.translate(str.maketrans('','',string.punctuation))



spec_input_words=[]
spec_mov_words=[]
i=0
# These loops are for catching words that don't have synsets. Those words will be removed from the strings and stored in separate arrays
#The removed words will be compared to each other for an exact match
#Error: The spaces in the strings are being mistaken for errors 

    
         

filtered_input_desc=[]
filtered_mov_desc=[]
compCount=0
stop_words = set(stopwords.words("english"))
lemmatizer= WordNetLemmatizer()
simSum=0
sim=0
simNum=0
input_desc = word_tokenize(input_desc)
for word in input_desc:
    if word.casefold() not in stop_words:
        filtered_input_desc.append(lemmatizer.lemmatize(word))

mov_desc = word_tokenize(mov_desc)
for word in mov_desc:
    if word.casefold() not in stop_words:
        filtered_mov_desc.append(lemmatizer.lemmatize(word))


i=0
for words in  filtered_input_desc:
    try:
        #skips an interation in the loop if a space is read
        if (words == " "):
            continue
        
        input_word=wordnet.synsets(words)[0]
        i=i+1
    except:
        spec_input_words.append(words)
        filtered_input_desc[i]=""
        i=i+1

        
g=0
for words in filtered_mov_desc:
    try:
        if (words == " "):
            continue
        
        mov_word=wordnet.synsets(words)[0]
        g=g+1
    except:
        spec_mov_words.append(words)
        filtered_mov_desc[g]=""
        g=g+1
        




for x in filtered_input_desc:
    #print(x)
    if(x==""): #skips any blank spaces in the filtered_mov_desc array
        continue
    input_word=wordnet.synsets(x)[0]
    for y in filtered_mov_desc:
        #print(y)
        if(y==""): #skips any blank spaces in the filtered_mov_desc array
            continue
        mov_word=wordnet.synsets(y)[0]
        sim=input_word.wup_similarity(mov_word)
        if(sim == None): # skips none type variables
            continue
        simSum=sim+simSum
        simNum=simNum+1
        #print(sim)

avgSim=(simSum/simNum)*100   
print(avgSim)

ct=0#counter
ct2=0
exactMatches=0
for input_word in spec_input_words:
    for mov_word in spec_mov_words:
        if(input_word == mov_word):
            exactMatches+=1
    
#print(exactMatches)   