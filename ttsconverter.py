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
root.resizable(True, True)
root.configure(bg = "#b5e48c")
root.mainloop()