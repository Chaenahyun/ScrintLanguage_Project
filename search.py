import requests
from bs4 import BeautifulSoup
import urllib.parse
from tkinter import *
from tkinter.font import Font
import tkinter.ttk
import subprocess

open_api_key = '26f2848737a442ae8b5ac596428e106c'
url = 'https://openapi.gg.go.kr/TninsttInstutM'


class SearchFrame:
    def __init__(self, frame):
        self.Combofont = Font(family='210 나무고딕 EB', weight='bold', slant='roman', size=14)
        self.Labelfont = Font(family='210 나무고딕 EB', weight='bold', slant='roman', size=18)

        # 시/군 라벨 생성, 위치 지정
        Label(frame, text='시/군', font=self.Labelfont, bg='light pink').place(x=15, y=25)
        self.cities = ['고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시',
                       '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '여주시',
                       '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시',
                       '가평군', '양평군', '연천군']
        self.cityCombo = tkinter.ttk.Combobox(frame, values=self.cities, height=5, font=self.Combofont)
        self.cityCombo.configure(state='readonly')
        self.cityCombo.place(x=90, y=30)
        self.cityCombo.bind("<<ComboboxSelected>>", self.updateEmdList)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.cityCombo.set('목록 선택')

        # 구/읍면동 라벨 생성, 위치 지정
        Label(frame, text='행정구', font=self.Labelfont, bg='light pink').place(x=15, y=80)
        self.emdCombo = tkinter.ttk.Combobox(frame, values=[], height=3, font=self.Combofont)
        self.emdCombo.configure(state='readonly')
        self.emdCombo.place(x=90, y=85)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.emdCombo.set('목록 선택')

        # 검색 버튼 생성, 위치 지정
        Button(frame, text='검색', width=3, height=1, relief='raised', bd=4, font=self.Labelfont,
               command=self.search, bg='mistyrose').place(x=375, y=65)
        # 라벨 생성, 위치 지정
        Label(frame, text='학원 및 교습소 명', font=self.Labelfont, bg='light pink').place(x=15, y=160)
        self.academyListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.academyListBox.place(x=15, y=210)
        self.academyListBox.bind('<Double-1>', self.show_details)  # 더블클릭하면 세부정보

        self.academy_details = []

        # book mark init
        notebook = tkinter.ttk.Notebook(frame, width=50, height=20)

        # 북마크 라벨
        graph_label = Label(frame, text='그래프', font=self.Labelfont, bg='light pink')
        graph_label.place(x=450, y=160)
        graph_label.bind('<Double-1>', self.run_graph_script)

        # 북마크 리스트 박스
        self.bookmarkListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.bookmarkListBox.place(x=450, y=210)

    def updateEmdList(self, event):
        selected_city = self.cityCombo.get()
        emds = {
            '고양시': ['덕양구', '일산동구', '일산서구'],
            '과천시': ['과천동', '문원동', '중앙동'],
            '광명시': ['광명동', '철산동', '하안동'],
            '광주시': ['경안동', '곤지암읍', '오포읍'],
            '구리시': ['교문동', '수택동', '인창동'],
            '군포시': ['군포동', '당정동', '산본동'],
            '김포시': ['사우동', '풍무동', '장기동'],
            '남양주시': ['다산동', '별내동', '화도읍'],
            '동두천시': ['생연동', '송내동', '보산동'],
            '부천시': ['원미구', '소사구', '오정구'],
            '성남시': ['수정구', '중원구', '분당구'],
            '수원시': ['장안구', '권선구', '팔달구', '영통구'],
            '시흥시': ['정왕동', '은행동', '매화동'],
            '안산시': ['상록구', '단원구'],
            '안성시': ['공도읍', '대덕면', '일죽면'],
            '안양시': ['만안구', '동안구'],
            '양주시': ['덕정동', '회천동', '양주읍'],
            '여주시': ['세종대왕면', '가남읍', '점동면'],
            '오산시': ['중앙동', '남촌동', '신장동'],
            '용인시': ['처인구', '기흥구', '수지구'],
            '의왕시': ['내손동', '청계동', '오전동'],
            '의정부시': ['호원동', '의정부동', '신곡동'],
            '이천시': ['창전동', '중리동', '관고동'],
            '파주시': ['운정동', '금촌동', '교하동'],
            '평택시': ['평택동', '안중읍', '서정동'],
            '포천시': ['소흘읍', '포천동', '군내면'],
            '하남시': ['덕풍동', '미사동', '감북동'],
            '화성시': ['병점동', '동탄동', '남양읍'],
            '가평군': ['가평읍', '설악면', '청평면'],
            '양평군': ['양평읍', '강상면', '옥천면'],
            '연천군': ['전곡읍', '연천읍', '신서면']
        }
        self.emdCombo['values'] = emds.get(selected_city, [])
        self.emdCombo.set('목록 선택')

    def search(self):
        self.academyListBox.delete(0, self.academyListBox.size())
        SIGUN_NM = urllib.parse.quote(self.cityCombo.get())
        EMD_NM = urllib.parse.quote(self.emdCombo.get())
        open_url = url + '?' + 'KEY=' + open_api_key + '&Type=xml&pIndex=1&pSize=20&SIGUN_NM=' + SIGUN_NM + '&EMD_NM=' + EMD_NM
        req = requests.get(open_url)

        print("req")
        print(req)
        html = req.text
        print("html")
        print(html)
        soup = BeautifulSoup(html, features='xml')  # XML 파서 사용
        print("soup")
        print(soup)
        # academies = soup.find_all('FACLT_NM')
        # print("academies")
        # print(academies)

        # telephones = soup.find_all('TELNO')
        # academyList = [x.text for x in academies]
        # phoneList = [x.text for x in telephones]

        # for x in range(len(academyList)):
        #     academy = academyList[x]
        #     phone = phoneList[x]
        #     self.academyListBox.insert(x, academy + '  ' + phone)

        self.academy_details = []
        for item in soup.find_all('row'):
            academy_name = item.find('FACLT_NM').get_text() if item.find('FACLT_NM') else "N/A"
            phone = item.find('TELNO').get_text() if item.find('TELNO') else "N/A"
            address = item.find('REFINE_ROADNM_ADDR').get_text() if item.find('REFINE_ROADNM_ADDR') else "N/A"
            representative = item.find('REPRSNTV_NM').get_text() if item.find('REPRSNTV_NM') else "없음"
            self.academy_details.append((academy_name, phone, address, representative))
            self.academyListBox.insert(END, f"{academy_name}  {phone}")

    def show_details(self, event):
        selected_index = self.academyListBox.curselection()[0]
        selected_academy = self.academy_details[selected_index]

        details_window = Toplevel()
        details_window.title("학원 세부 정보")

        frame = Frame(details_window)
        frame.pack()

        headers = ["학원명", "전화번호", "주소", "대표자명"]
        for i, col_name in enumerate(headers):
            label = Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
            label.grid(row=0, column=i)

        data = selected_academy
        for i, value in enumerate(data):
            label = Label(frame, text=value, font=("Helvetica", 12))
            label.grid(row=1, column=i)

    def run_graph_script(self, event):
        subprocess.Popen(['python', 'graph.py'])

