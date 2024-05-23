from tkinter import Tk, Label, Frame, Button
from tkinter.font import Font
from search import SearchFrame

frameHeight = 580
WIDTH = 960
HEIGHT = 640

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.resizable(False, False)

        APP = Font(family='bauhaus 93', size=40, slant='italic')
        nameTag = Label(self.window, text='APP', font=APP, width=4)
        nameTag.grid(row=0, column=0, sticky='w')

        self.searchFrame = Frame(self.window, width=WIDTH / 2 - 30, height=frameHeight)
        self.searchFrame.grid(row=1, column=0)
        SearchFrame(self.searchFrame)

        self.buttonFont = Font(family='italic', weight='bold', slant='roman', size=30)
        self.button = Button(self.window, text='검색', width=4, height=1, relief='raised', bd=4, font=self.buttonFont,
                             command=SearchFrame.search)
        self.button.place(x=300, y=100)

        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=frameHeight)
        self.mapFrame.grid(row=1, column=1)

        self.funcFrame = Frame(self.window, width=90, height=frameHeight)
        self.funcFrame.grid(row=1, column=2)

        self.window.mainloop()

MainGUI()
