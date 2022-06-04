import pyttsx3
import pdfplumber
import PyPDF2
import os
from gtts import gTTS
import googletrans
from googletrans import Translator

file = 'Think-And-Grow-Rich.pdf'

pdfFileObj = open(file,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

#pdf plumber object and loop through all the pages

with pdfplumber.open(file) as pdf:
    for i in range(0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)

        # creating a speaker for English listeners
        # speaker = pyttsx3.init()
        # speaker.say(text)
        # speaker.runAndWait()

        # Convert text to hindi

        translator= Translator()
        translate_text= translator.translate(text, dest='hi')
        print('Hindi Translation : ',translate_text)

        #  convert text to Audio file
        outPut=gTTS(text=str(translate_text),lang='hi',slow=False)

        # Save Audio file
        outPut.save('AudioBook'+str(i+1)+'.mp3')

        # play audio 
        #os.system('AudioBook.mp3')

        """
        Future Work
        For long documents: Combine all the audio files
        Filter for repeating elements
        MAke an app for Play store/App Store

        Remove extra lines
        Play the book togather alongside the audio
        """