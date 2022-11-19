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
root.geometry("1000x580+200+80")
root.resizable(False, False)
root.configure(bg = "#b5e48c")
# root.mainloop()

self_logo = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_1.png")
Label(root, image = self_logo, bg="#b5e48c").place(x = 550, y = 260)
logo_image = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_2.png")
root.iconphoto(False, logo_image)
root.mainloop()