import operator
from gtts import gTTS
import gtts
from playsound import playsound
import speech_recognition as sr
import os
import pywhatkit as kit
import pafy
import urllib3
import vlc
import requests
import youtube_dl
import re, requests, subprocess, urllib.parse, urllib.request
import time
import random
import google
import numbers
# Imports above

#Reconize Mic
r = sr.Recognizer()
#language useless
language = 'en'
#Loop Mic + reconize voice
while(1):   
     

        with sr.Microphone() as source2:
              
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            audio2 = r.listen(source2)
              
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

#Print Speech
            print(MyText)

#Add commands here! O_O
            if 'hello' in MyText:
                speakkido = 'hello sir'
                myobj = gTTS(text=speakkido, lang=language, slow=False)  
                myobj.save("speech.mp3")
                playsound('speech.mp3')

    

            if 'i am fine' in MyText:
                speakkido = 'good to know sir'
                myobj = gTTS(text=speakkido, lang=language, slow=False)  
                myobj.save("speech.mp3")
                playsound('speech.mp3')
            


            if 'exit' in MyText:
                speakkido = "Exiting now..."
                myobj = gTTS(text=speakkido, lang=language, slow=False)  
                myobj.save("speech.mp3")
                playsound('speech.mp3')
                print("Task Completed")
                quit()
            
            if 'play' in MyText:
                if 'audio' in MyText:
                    kit.playonyt(MyText)
             
            if 'search' in MyText:
               kit.search(MyText)
               speakkido = "This is what i found on the web!"
            
            if 'repeat' in MyText:
                if 'after' in MyText:
                   if 'me' in MyText:
                       speakkido = MyText 
                       myobj = gTTS(text=speakkido, lang=language, slow=False)
                       myobj.save("speech.mp3")
                       playsound('speech.mp3')

