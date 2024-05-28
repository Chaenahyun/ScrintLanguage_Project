from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from search import *
from map import *
from mail import *
from gif import LoadGIFImage

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
        nameTag = Label(self.window, text='STUDY WITH ME', font=APP, width=40, anchor='w', bg='light cyan')
        nameTag.grid(row=0, column=0)

        self.searchFrame = Frame(self.window, width=WIDTH, height=frameHeight, bg='light green')
        self.searchFrame.place(x=0, y=60)
        SearchFrame(self.searchFrame)

        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=80, bg='light green')
        self.mapFrame.place(x=450, y=100)
        MapFrame(self.mapFrame)

        #telegram., mail icon frame
        self.funcFrame = Frame(self.window, width=95, height=frameHeight - 50, bg='light cyan')
        self.funcFrame.place(x=855, y=100)
        MailFrame(self.funcFrame)

        #Gif
        # Load GIFs
        self.gifFrame = Frame(self.window, width=WIDTH, height=frameHeight, bg='white')
        self.gifFrame.place(x=0, y=500)

        # 여러 GIF 로드
        self.loadGIF1 = LoadGIFImage(self.gifFrame, 'resources/gif1.gif', x=10, y=10, speed=100)
        self.loadGIF2 = LoadGIFImage(self.gifFrame, 'resources/gif2.gif', x=310, y=10, speed=200)
        self.loadGIF3 = LoadGIFImage(self.gifFrame, 'resources/gif3.gif', x=610, y=10, speed=300)
        self.loadGIF4 = LoadGIFImage(self.gifFrame, 'resources/gif4.gif', x=610, y=10, speed=300)
        self.loadGIF5 = LoadGIFImage(self.gifFrame, 'resources/gif5.gif', x=610, y=10, speed=300)

        self.window.mainloop()
        pass

MainGUI()