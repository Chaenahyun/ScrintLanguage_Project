from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from PIL import Image as PILImage, ImageTk

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

        self.title_frame = Frame(self.window, width=WIDTH, height=HEIGHT)
        self.title_frame.pack()

        #타이틀 로딩 이미지 버전
        # self.title_image = PILImage.open('resources/title.png')
        # self.title_photo = ImageTk.PhotoImage(self.title_image)
        # self.title_label = Label(self.title_frame, image=self.title_photo)
        # self.title_label.pack()

        #타이틀 로딩(gif)
        self.gifFrame1 = Frame(self.window, width=960, height=640, bg='black')
        self.gifFrame1.place(x=0, y=0)
        self.LoadingGIFImage = LoadGIFImage1(self.gifFrame1, 'resources/loading.gif', x=0, y=0, speed=50)

        self.window.after(1000, self.start_main_gui)  # 3초 후에 start_main_gui 호출

        # 타이틀
        self.window.title("Edu Hunter")
        self.window.geometry(f'{WIDTH}x{HEIGHT}')
        self.window.resizable(False, False)

        self.window.mainloop()

    def start_main_gui(self):
        self.title_frame.pack_forget()
        self.setup_main_gui()

    def setup_main_gui(self):
        APP = Font(family='210 나무고딕 EB', size=40, slant='roman')
        nameTag = Label(self.window, text='Edu Hunter', font=APP, width=40, anchor='w', bg='mistyrose')
        nameTag.grid(row=0, column=0)

        self.TitleFrame = Frame(self.window, width=95, height=frameHeight - 50, bg='mistyrose')
        self.TitleFrame.place(x=855, y=100)

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
        self.gifFrame1 = Frame(self.window, width=40, height=40, bg='light pink')
        self.gifFrame1.place(x=210, y=215)
        self.loadGIF1 = LoadGIFImage1(self.gifFrame1, 'resources/gif1.gif', x=0, y=0, speed=200)
        # Load GIF2
        self.gifFrame2 = Frame(self.window, width=50, height=50, bg='mistyrose')
        self.gifFrame2.place(x=300, y=10)
        self.loadGIF2 = LoadGIFImage2(self.gifFrame2, 'resources/gif2.gif', x=0, y=0, speed=300)
        # Load GIF3
        self.gifFrame3 = Frame(self.window, width=40, height=40, bg='light pink')
        self.gifFrame3.place(x=525, y=215)
        self.loadGIF3 = LoadGIFImage3(self.gifFrame3, 'resources/gif3.gif', x=0, y=0, speed=300)
        # Load GIF4
        self.gifFrame4 = Frame(self.window, width=100, height=40, bg='light pink')
        self.gifFrame4.place(x=700, y=90)
        self.loadGIF4 = LoadGIFImage4(self.gifFrame4, 'resources/gif4.gif', x=0, y=0, speed=300)
        # Load GIF5
        self.gifFrame5 = Frame(self.window, width=40, height=40, bg='mistyrose')
        self.gifFrame5.place(x=887, y=100)
        self.loadGIF5 = LoadGIFImage5(self.gifFrame5, 'resources/gif5.gif', x=0, y=0, speed=300)
        # Load catGIF
        self.gifFrame6 = Frame(self.window, width=20, height=20, bg='mistyrose')
        self.gifFrame6.place(x=895, y=600)
        self.loadCatGIF = LoadCatGIFImage(self.gifFrame6, 'resources/cat.gif', x=0, y=0, speed=300)


if __name__ == "__main__":
    MainGUI()
