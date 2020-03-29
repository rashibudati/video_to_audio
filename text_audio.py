# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:27:00 2020

@author: BUD3KOR
"""

# Import the required module for text 
# to speech conversion 
#from gtts import gTTS 
#
mytext = open('C:/Users/BUD3KOR/Downloads/video_text/filesss/text.txt','r')
k = mytext.read()
#print(k)

import pyttsx3
engine = pyttsx3.init()
##engine.say("hello crazy programmer")
engine.setProperty('rate',120)
engine.setProperty('volume', 0.9)
engine.save_to_file(k, "C:/Users/BUD3KOR/Downloads/video_text/filesss/output.mp3")
engine.runAndWait()
