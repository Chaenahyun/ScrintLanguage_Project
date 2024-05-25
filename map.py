
from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk


class MapFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)
        mapLabel = Label(frame, text='지도', font=self.Labelfont)
        mapLabel.place(x=15, y=25)