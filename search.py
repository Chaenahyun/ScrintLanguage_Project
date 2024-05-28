from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk
import requests
from bs4 import BeautifulSoup
import urllib

open_api_key = 'ff47d1d708e3432cb12c14f70bdffb56'
url = 'https://openapi.gg.go.kr/TninsttInstutM?KEY='

class SearchFrame:
    def __init__(self, frame):
        self.Combofont = Font(family='italic', weight='bold', slant='roman', size=14)
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)

        # 시/군 라벨 생성, 위치 지정
        Label(frame, text='시/군', font=self.Labelfont).place(x=15, y=25)
        #행정구역 더 추가해야함
        cities = ['고양시', '과천시', '광명시']
        self.cityCombo = tkinter.ttk.Combobox(frame, values=cities, height=5, font=self.Combofont)
        self.cityCombo.configure(state='readonly')
        self.cityCombo.place(x=90, y=30)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.cityCombo.set('목록')

        # 업종 라벨 생성, 위치 지정
        Label(frame, text='업종', font=self.Labelfont).place(x=15, y=80)
        #업종
        industries = ['교습소', '평생직업교육학원', '학교교과교습학원']
        self.industryCombo = tkinter.ttk.Combobox(frame, values=industries, height=3, font=self.Combofont)
        self.industryCombo.configure(state='readonly')
        self.industryCombo.place(x=90, y=85)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.industryCombo.set('목록')

        # 검색 버튼 생성, 위치 지정
        Button(frame, text='검색', width=4, height=1, relief='raised', bd=4, font=self.Labelfont,
                             command=self.search).place(x=350, y=50)
        # 라벨 생성, 위치 지정
        Label(frame, text='학원 및 교습소 명', font=self.Labelfont).place(x=15, y=160)
        #학원 리스트 박스
        self.academyListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.academyListBox.place(x=15, y=230)

    def search(self):
        self.academyListBox.delete(0, self.academyListBox.size())
        SIGUN_NM = urllib.parse.quote(self.cityCombo.get())
        INDUTYPE = urllib.parse.quote(self.industryCombo.get())
        params = '&SIGUN_NM=' + SIGUN_NM + '&INDUTYPE_DIV_NM=' + INDUTYPE
        open_url = url + open_api_key + params

        req = requests.get(open_url)
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        academies = soup.find_all('faclt_nm')
        telephones = soup.find_all('telno')

        academyList = [x.text for x in academies]
        phoneList = [x.text for x in telephones]
        for x in range(len(academyList)):
            academy = academyList[x]
            phone = phoneList[x]
            self.academyListBox.insert(x, academy + '  ' + phone)