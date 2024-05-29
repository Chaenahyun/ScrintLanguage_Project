from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from search import *
from map import *
from mail import *
from telegram import *

frameHeight = 580
WIDTH = 960
HEIGHT = 640

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Edu Hunter")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(False, False)

        APP = Font(family='210 나무고딕 EB', size=40, slant='roman')
        nameTag = Label(self.window, text='Edu Hunter', font=APP, width=40, anchor='w', bg='mistyrose')
        nameTag.grid(row=0, column=0)

        self.searchFrame = Frame(self.window, width=WIDTH, height=frameHeight, bg='light pink')
        self.searchFrame.place(x=0, y=60)
        SearchFrame(self.searchFrame)

        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=80, bg='light pink')
        self.mapFrame.place(x=450, y=100)
        MapFrame(self.mapFrame)

        self.funcFrame = Frame(self.window, width=95, height=frameHeight - 50, bg='mistyrose')
        self.funcFrame.place(x=855, y=100)
        MailFrame(self.funcFrame)
        TelegramFrame(self.funcFrame)

        self.window.mainloop()

MainGUI()
