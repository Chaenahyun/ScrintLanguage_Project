from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk
import urllib.request #api
import webbrowser #webbrowser open

client_id = '4j25bu6e3m'
client_secret = 'bWGvQe4gKJ7Hqm3SxvTW1u7OsOnV4HAsb5efTTO9'


class MapFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)
        mapLabel = Label(frame, text='지도', font=self.Labelfont)
        mapLabel.place(x=15, y=25)

        # 검색 라벨 생성
        self.initEntry(frame)
        #지도 연결 버튼
        self.initButton(frame)

    def initEntry(self, frame):
        self.mapEntry = Entry(frame, width=15, font=self.Labelfont)
        self.mapEntry.place(x=100, y=25)

    def initButton(self, frame):
        self.mapButton = Button(frame, text='열기', width=4, height=1, relief='raised',
                                font=Font(family='italic', size=15, weight='bold'), command=self.connectMap)
        self.mapButton.place(x=350, y=25)

    def connectMap(self):
        #지도 url열기
        url = 'https://map.naver.com/p/'
        option = '?sm=top_hty&fbm=1&ie=utf8&'
        query = 'query=' + urllib.parse.quote(self.mapEntry.get())

        url_query = url+option+query
        webbrowser.open_new(url_query)
        pass