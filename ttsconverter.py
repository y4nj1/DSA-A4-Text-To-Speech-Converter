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
root.configure(bg = "#b5e48c")


self_logo = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_1.png")
Label(root, image = self_logo, bg="#b5e48c").place(x = 550, y = 460)

logo_image = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_2.png")
root.iconphoto(False, logo_image)

upper_frame = Frame(root, bg = "#168aad", width = 1200, height = 190)
upper_frame.place(x=0, y=0)

picture = PhotoImage(file="C:\\Users\\Estrella\\Desktop\\logo_2.png")
Label(upper_frame, image=picture, bg = "#168aad").place(x = 40, y = -30)
Label(upper_frame, text="Text to Speech Converter", font="Helvetica 40 bold italic", bg = "#168aad", fg = "white").place(x = 280, y = 65)

root.mainloop()