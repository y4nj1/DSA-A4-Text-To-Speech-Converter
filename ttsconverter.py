import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound

root = Tk()
root.title("Text to Speech Converter")
root.geometry("1000x780+200+80")
root.resizable(False, False)
root.configure(bg = "#76c893")


self_logo = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_1.png")
Label(root, image = self_logo, bg="#76c893").place(x = 770, y = 620)

logo_image = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_2.png")
root.iconphoto(False, logo_image)

upper_frame = Frame(root, bg = "#168aad", width = 1200, height = 190)
upper_frame.place(x=0, y=0)

picture = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_2.png")
Label(upper_frame, image=picture, bg = "#168aad").place(x = 40, y = -30)
Label(upper_frame, text="Text to Speech Converter", font="Helvetica 40 bold italic", bg = "#168aad", fg = "white").place(x = 280, y = 65)

Label(text="Enter your text here:", font="Helvetica 20 bold italic", bg = "#76c893", fg = "black").place(x = 30, y = 200)
text_box = Text(root, font="calibri 12", bg = "white", relief = GROOVE, wrap = WORD, bd = 0)
text_box.place(x = 30, y = 240, width = 940, height = 180)

gender_box = Combobox(root, values = ['Male', 'Female'], font = "Robote 12", state='r', width = 12)
gender_box.place(x = 240, y = 500)
gender_box.set('Male')
Label(text="Choose your Speaker", font="Helvetica 12 bold italic", bg = "#76c893", fg = "black").place(x = 220, y = 470)

speed_box = Combobox(root, values = ['Fast', 'Medium', 'Slow'], font = "Robote 12", state='r', width = 12)
speed_box.place(x = 620, y = 500)
speed_box.set('Medium')
Label(text="Choose your Speaking Speed", font="Helvetica 12 bold italic", bg = "#76c893", fg = "black").place(x = 570, y = 470)

root.mainloop()