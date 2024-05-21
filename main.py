'''
[main.py]
메인모듈
'''
from tkinter import *
from tkinter.font import *
from search import *

frameHeight = 580
WIDTH = 960
HEIGHT = 640

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(False, False)

        title_font = Font(family='italic', size=40, slant='italic')

        nameTag = Label(self.window, text='APP', font=title_font)
        nameTag.grid(row=0, column=0)

        self.searchFrame = Frame(self.window, width=int(WIDTH / 2 - 30), height=frameHeight, relief=GROOVE)
        self.searchFrame.grid(row=1, column=0, sticky="nsew")
        SearchFrame(self.searchFrame)

        self.mapFrame = Frame(self.window, width=int(WIDTH / 2 - 60), height=frameHeight)
        self.mapFrame.grid(row=1, column=1, sticky="nsew")

        self.funcFrame = Frame(self.window, width=90, height=frameHeight)
        self.funcFrame.grid(row=1, column=2, sticky="nsew")

        self.leftFrame = Frame(self.window, width=540, height=700)
        self.leftFrame.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.rightFrame = Frame(self.window, width=540, height=700)
        self.rightFrame.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.window.mainloop()

MainGUI()
