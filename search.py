from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import tkinter.ttk


class SearchFrame:
    def __init__(self, frame):
        # 폰트 설정
        self.font = Font(family='italic', weight='bold', slant='roman')

        # '시/군' 레이블 추가
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel.place(x=30, y=25)  # 레이블 위치 설정

        # '시/군' 콤보박스 추가
        values = [str(i) for i in range(10)]  # 콤보박스 항목으로 사용할 값 생성
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)  # 콤보박스 생성
        cityCombo.configure(state='readonly')  # 콤보박스를 읽기 전용으로 설정
        cityCombo.place(x=100, y=30)  # 콤보박스 위치 설정
        cityCombo.set('목록')  # 초기 선택값 설정

        # '업종' 레이블 추가
        jobLabel = Label(frame, text='업종', font=self.font)
        jobLabel.place(x=30, y=80)  # 레이블 위치 설정

        # '업종' 콤보박스 추가
        values = [str(i) for i in range(10)]  # 콤보박스 항목으로 사용할 값 생성
        jobCombo = tkinter.ttk.Combobox(frame, values=values, height=5)  # 콤보박스 생성
        jobCombo.configure(state='readonly')  # 콤보박스를 읽기 전용으로 설정
        jobCombo.place(x=100, y=85)  # 콤보박스 위치 설정
        jobCombo.set('목록')  # 초기 선택값 설정

    # 검색 기능을 위한 메서드 (현재는 비어 있음)
    def search(self):
        pass


# 테스트를 위한 기본 윈도우 설정
if __name__ == "__main__":
    root = Tk()
    root.geometry("300x200")
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)
    SearchFrame(frame)
    root.mainloop()
