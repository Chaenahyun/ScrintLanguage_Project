from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from search import *
from map import *

frameHeight = 580
WIDTH = 960
HEIGHT = 640
class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(False, False)
        APP = Font(family='bauhaus 93', size=40, slant='italic')
        nameTag = Label(self.window, text='APP', font=APP, width=4)
        nameTag.grid(row=0, column=0, sticky='w')
        self.searchFrame = Frame(self.window, width=WIDTH, height=frameHeight, bg='light gray')
        self.searchFrame.place(x=0, y=60)
        SearchFrame(self.searchFrame)
        self.buttonFont = Font(family='italic', weight='bold', slant='roman', size=20)
        self.button = Button(self.window, text='검색', width=4, height=1, relief='raised', bd=4, font=self.buttonFont,
                             command=SearchFrame.search)
        self.button.place(x=350, y=100)

        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=frameHeight - 50, bg='magenta')
        self.mapFrame.place(x=450, y=100)
        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=frameHeight - 80, bg='magenta')
        self.mapFrame.place(x=450, y=130)
        MapFrame(self.mapFrame)

        self.funcFrame = Frame(self.window, width=70, height=frameHeight - 50, bg='cyan')
        self.funcFrame.place(x=880, y=100)
        self.resultFrame = Frame(self.window, width=WIDTH / 2 - 50, height=frameHeight / 2 + 60, bg='green')
        self.resultFrame.place(x=10, y=280)
        self.window.mainloop()
        pass
MainGUI()