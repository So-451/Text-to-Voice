import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.config(bg="RoyalBlue4")


engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def download():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


root.iconbitmap("./favicon-megaphone.ico")


Top_frame=Frame(root, bg="white smoke",width= 900, height= 100)
Top_frame.pack()


Logo = Image.open("./microphone.png")
Logo_canvaLogo = ImageTk.PhotoImage(Logo.resize((95, 95)))  
label = Label(root, image= Logo_canvaLogo)
label.place(x = 0, y = 0)

Label(Top_frame, text= "TEXT TO SPEECH",font="arial 20 bold", bg="white smoke",fg="black").place(x=100, y=30)

text_area=Text(root,font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="RoyalBlue4",fg="white").place(x=580,y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="RoyalBlue4",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root, values=['Male','Female'],font="arial 14",state='r', width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.current(0)

speed_combobox=Combobox(root, values=['Fast','Normal', 'Slow'],font="arial 14",state='r', width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.current(1)

imageicon=PhotoImage(file="megaphone.png")
photoimage= imageicon.subsample(10, 10)
btn=Button(root,text="Speak",compound=LEFT,image=photoimage,width=130,font="arial 14 bold", command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="Download.png")
photoimage2= imageicon2.subsample(38, 38)
savebtn=Button(root,text="Save",compound=LEFT,image=photoimage2, bg ="light blue",width=130,font="arial 14 bold", command=download)
savebtn.place(x=730,y=280)



root.mainloop()