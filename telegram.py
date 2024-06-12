from tkinter import *
from tkinter.font import *
import tkinter.ttk
import telepot


class TelegramFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=12)
        telegramLabel = Label(frame, text='TELEGRAM', font=self.Labelfont, bg='light cyan')
        telegramLabel.place(x=0, y=270)

        self.image = PhotoImage(file="telegram.png")
        self.initButton(frame)

    def initButton(self, frame):
        self.telegramButton = Button(frame, width=70, height=70, image=self.image, command=self.initWindow)
        self.telegramButton.place(x=10, y=300)

    def initWindow(self):
        pass