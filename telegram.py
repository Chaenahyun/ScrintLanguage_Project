from tkinter import *
from tkinter.font import *
import tkinter.ttk
import telepot


class TelegramFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='210 나무고딕 EB', weight='bold', slant='roman', size=12)
        telegramLabel = Label(frame, text='TELEGRAM', font=self.Labelfont, bg='mistyrose')
        telegramLabel.place(x=0, y=270)

        self.image = PhotoImage(file="telegram.png")
        self.initButton(frame)

    def initButton(self, frame):
        self.telegramButton = Button(frame, width=80, height=80, image=self.image, command=self.initWindow)
        self.telegramButton.place(x=10, y=300)

    def initWindow(self):
        pass