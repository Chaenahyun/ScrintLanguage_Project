from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk

class SearchFrame:
    def __init__(self, frame):
        self.font = Font(family='italic', weight='bold', slant='roman')
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel.place(x=30, y=25)
        self.Combofont = Font(family='italic', weight='bold', slant='roman', size=14)
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)

        cityLabel = Label(frame, text='시/군', font=self.Labelfont)
        cityLabel.place(x=15, y=25)
        values = [str(i) for i in range(10)]
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5, font=self.Combofont)
        cityCombo.configure(state='readonly')
        cityCombo.place(x=100, y=30)
        cityCombo.place(x=90, y=30)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        cityCombo.set('목록 선택')

        jobLabel = Label(frame, text='업종', font=self.font)
        jobLabel.place(x=30, y=80)
        jobLabel = Label(frame, text='업종', font=self.Labelfont)
        jobLabel.place(x=15, y=80)
        values = [str(i) for i in range(10)]
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5, font=self.Combofont)
        cityCombo.configure(state='readonly')
        cityCombo.place(x=100, y=85)
        cityCombo.place(x=90, y=85)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        cityCombo.set('목록 선택')


        resultLabel = Label(frame, text='학원 및 교습소 명', font=self.Labelfont)
        resultLabel.place(x=15, y=160)

    def search(self):
        pass
