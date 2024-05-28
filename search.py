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
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=18)

        # 시/군 라벨 생성, 위치 지정
        Label(frame, text='시/군', font=self.Labelfont, bg='light green').place(x=15, y=25)
        cities = ['고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시',
                  '부천시', '성남시', '수원시', '시흥시a', '안산시', '안성시', '안양시', '양주시', '여주시',
                  '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시',
                  '가평군', '양평군', '연천군']
        self.cityCombo = tkinter.ttk.Combobox(frame, values=cities, height=5, font=self.Combofont)
        self.cityCombo.configure(state='readonly')
        self.cityCombo.place(x=90, y=30)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.cityCombo.set('목록')

        # 업종 라벨 생성, 위치 지정
        Label(frame, text='업종', font=self.Labelfont, bg='light green').place(x=15, y=80)
        #업종
        industries = ['교습소', '평생직업교육학원', '학교교과교습학원']
        self.industryCombo = tkinter.ttk.Combobox(frame, values=industries, height=3, font=self.Combofont)
        self.industryCombo.configure(state='readonly')
        self.industryCombo.place(x=90, y=85)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.industryCombo.set('목록')

        # 검색 버튼 생성, 위치 지정
        Button(frame, text='검색', width=4, height=1, relief='raised', bd=4, font=self.Labelfont,
                             command=self.search, bg='light cyan').place(x=350, y=60)
        # 라벨 생성, 위치 지정
        Label(frame, text='학원 및 교습소 명', font=self.Labelfont, bg='light green').place(x=15, y=160)
        #학원 리스트 박스
        self.academyListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.academyListBox.place(x=15, y=230)

        # book mark init
        notebook = tkinter.ttk.Notebook(frame, width=50, height=20)

        # 북마크 라벨
        Label(frame, text='북마크', font=self.Labelfont, bg='light green').place(x=450, y=160)

        # 북마크 리스트 박스
        self.bookmarkListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.bookmarkListBox.place(x=450, y=230)

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