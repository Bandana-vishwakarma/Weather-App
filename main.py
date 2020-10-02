
"""Importing required modules"""
import json
import tkinter as tk
from tkinter import messagebox, StringVar, Entry
from tkinter import ttk
import requests
from PIL import Image, ImageTk

try:
    """For high DPI displays only window machines"""
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    pass


# noinspection PyAttributeOutsideInit
class App(tk.Tk):
    city_entry: Entry
    city_name: StringVar

    def __init__(self):
        super().__init__()

        HEIGHT = 600
        WIDTH = 700

        self.title('Weather')
        self.geometry('{}x{}'.format(WIDTH, HEIGHT))
        self.resizable(False, False)
        self.iconbitmap('icon.ico')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, background='#76ffff')
        canvas.grid(sticky='NSEW')

        background = ImageTk.PhotoImage(Image.open('w.jpg'))
        canvas.background = background
        bg = canvas.create_image(350, 90, image=background)

        self.main_frame = tk.Frame(canvas, borderwidth=10, relief='ridge', background='#03a9f4')
        self.main_frame.grid(row=0, column=0, sticky='NSEW', padx=80, pady=100, ipadx=15, ipady=15)

        self.CreateWidgets()
