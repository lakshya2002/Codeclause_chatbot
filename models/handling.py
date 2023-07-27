# importing the utilities
import nltk
import spacy
import pickle
import numpy as np
import pandas as pd
import json
import random
from keras.models import load_model
import tensorflow as tf 
import re
import tkinter
from tkinter import *
import sys
import os

# ======================================= Loading Data ======================================================================
model = load_model("bot_model.h5")
intents = json.loads(open('Data/intent.json','r',encoding='UTF-8').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

# ============================================================================================================================
def pre_process(sentence):
    nlp = spacy.load('en_core_web_sm')
    # Tokenize the sentence and create a list of lemmatized words
    sentence_words = [token.lemma_ for token in nlp(sentence)]
    return sentence_words

def bow(sentence, words, show_details=True):
    # Tokenize the pattern
    sentence_words = pre_process(sentence)
    # Bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                # Assign 1 if the current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("Found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def start_chat():
     name = input("Enter Your Name: ")
     print("Welcome " + name + " to the Code Clause Bot Service! Let me know how can I help you?\n")
     while True:
         inp = str(input()).lower()
         if inp.lower()=="end":
             break
         if inp.lower()== '' or inp.lower()== '*':
             print('Please re-phrase your query!')
             print("-"*50)
         else:
             print(f"Code Clause: {chatbot_response(inp)}"+'\n')
             print("-"*50)

# start_chat()


import os
from tkinter import Tk, Text, Button, Scrollbar, DISABLED, END, FALSE

if os.environ.get('DISPLAY', '') == '':
    print('no DISPLAY found. Using: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# Dark Theme
base.config(bg="#121212")

# Create Chat window
ChatLog = Text(base, bd=0, bg="#121812", fg="#f0f0f0", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Verdana", 10, 'bold'), text="Send", width="10", height=1,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff')

# Create the box to enter message
EntryBox = Text(base, bd=0, bg="#1c1c1c", fg="#f0f0f0", width="29", height="5", font="Arial")

# Function to send the message
def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state='normal')
        ChatLog.tag_config("user", justify='right')  # Align user response to the right
        ChatLog.tag_config("bot", justify='left')  # Align bot response to the left

        ChatLog.insert(END, "You: " + msg + '\n\n', "user")
        res = chatbot_response(msg)  # Call the chatbot_response function here to get the chatbot's response
        ChatLog.insert(END, "Bot: " + res + '\n\n', "bot")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

# Bind Enter key to send message
def on_enter(event):
    send()

EntryBox.bind("<Return>", on_enter)

# Place all components on the screen
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
