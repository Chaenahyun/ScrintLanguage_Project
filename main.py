from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from search import *
from map import *
from mail import *
from telegram import *
#gif
from gif import LoadGIFImage1,  LoadGIFImage2,  LoadGIFImage3,  LoadGIFImage4, LoadGIFImage5, LoadCatGIFImage, LoadTitleImage

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

        ##GIF
        # Load GIF1
        self.gifFrame = Frame(self.window, width=40, height=40, bg='light pink')
        self.gifFrame.place(x=210, y=215)
        self.loadGIF1 = LoadGIFImage1(self.gifFrame, 'resources/gif1.gif', x=0, y= 0, speed=200)
        # Load GIF2
        self.gifFrame = Frame(self.window, width=50, height=50, bg='mistyrose')
        self.gifFrame.place(x=300, y=10)
        self.loadGIF2 = LoadGIFImage2(self.gifFrame, 'resources/gif2.gif', x=0, y=0, speed=300)
        # Load GIF3
        self.gifFrame = Frame(self.window, width=40, height=40, bg='light pink')
        self.gifFrame.place(x=525, y=215)
        self.loadGIF3 = LoadGIFImage3(self.gifFrame, 'resources/gif3.gif', x=0, y=0, speed=300)
        # Load GIF4
        self.gifFrame = Frame(self.window, width=100, height=40, bg='light pink')
        self.gifFrame.place(x=700, y=90)
        self.loadGIF3 = LoadGIFImage4(self.gifFrame, 'resources/gif4.gif', x=0, y=0, speed=300)
        self.window.mainloop()
        # Load GIF5
        self.gifFrame = Frame(self.window, width=40, height=40, bg='light pink')
        self.gifFrame.place(x=0, y=0)
        self.loadGIF5 = LoadGIFImage5(self.gifFrame, 'resources/gif5.gif', x=0, y=0, speed=300)
        self.window.mainloop()
        # Load catGIF
        self.gifFrame = Frame(self.window, width=20, height=20, bg='mistyrose')
        self.gifFrame.place(x=895, y=600)
        self.loadCatGIF = LoadCatGIFImage(self.gifFrame, 'resources/cat.gif', x=0, y=0, speed=300)
        # Load TitleGIF
        self.gifFrame = Frame(self.window, width=500, height=500, bg='mistyrose')
        self.gifFrame.place(x=0, y=0)
        self.loadTitleGIF = LoadTitleImage(self.gifFrame, 'resources/title_banner.png.gif', x=0, y=0, speed=300)


MainGUI()
