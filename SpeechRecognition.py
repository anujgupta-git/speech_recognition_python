#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition as s
sr=s.Recognizer()
print("i am your specch recognizer")
with s.Microphone() as m:
        audio=sr.listen(m)
        query =sr.recognize_google(audio,language='en')
        print(query)
        

