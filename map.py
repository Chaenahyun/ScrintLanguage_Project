from tkinter import *
from tkinter.font import *
import urllib.parse
import webview

client_id = '4j25bu6e3m'
client_secret = 'bWGvQe4gKJ7Hqm3SxvTW1u7OsOnV4HAsb5efTTO9'


class MapFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='210 나무고딕 EB', weight='bold', slant='roman', size=20)
        mapLabel = Label(frame, text='지도', font=self.Labelfont, bg='light pink')
        mapLabel.place(x=3, y=35)

        # 검색 라벨 생성
        self.initEntry(frame)
        # 지도 연결 버튼
        self.initButton(frame)

    def initEntry(self, frame):
        self.mapEntry = Entry(frame, width=15, font=self.Labelfont)
        self.mapEntry.place(x=70, y=35)

    def initButton(self, frame):
        self.mapButton = Button(frame, text='열기', width=4, height=1, relief='raised', bg='mistyrose',
                                font=Font(family='210 나무고딕 EB', size=15, weight='bold'), command=self.connectMap)
        self.mapButton.place(x=310, y=35)

    def connectMap(self):
        # 지도 url 생성
        base_url = 'https://map.naver.com/v5/search/'
        if self.mapEntry.get() == '':
            return False
        query = urllib.parse.quote(self.mapEntry.get())

        url_query = base_url + query

        # 새로운 웹뷰 창을 열어 지도 표시
        self.showMapWindow(url_query)

    def showMapWindow(self, url):
        webview.create_window('Naver Map', url)
        webview.start()

