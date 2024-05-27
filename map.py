from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk
class MapFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)
        mapLabel = Label(frame, text='지도', font=self.Labelfont)
        mapLabel.place(x=15, y=25)

        #지도 연결 버튼
        self.initButton(frame)

    def initButton(self, frame):
        self.mapButton = Button(frame, text='지도 보기', width=6, height=1, bd=4, relief='raised', font=self.Labelfont,
                                command=self.connectMap).place(x=15, y=100)

    def connectMap(self):
        pass