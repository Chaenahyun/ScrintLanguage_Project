from xml import *
from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import tkinter.ttk


class SearchFrame:
    def __init__(self, frame):
        self.font = Font(family='italic', slant='italic')
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel.place(x=30, y=30)
        cityCombo = Combobox()
        values = [str(i) for i in range(10)]
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)
        cityCombo.configure(state='readonly')
        cityCombo.place(x=100, y=30)
        cityCombo.set('목록')
        pass