from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import tkinter.ttk

class SearchFrame:
    def __init__(self, frame):
        self.font = Font(family='italic', slant='italic') #폰트

        # '시/군' 레이블 추가
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel.place(x=30, y=30)

        # '시/군' 콤보박스 추가
        values = [str(i) for i in range(10)]  # 콤보박스 항목으로 사용할 값 생성
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)  # 콤보박스 생성
        cityCombo.configure(state='readonly')  # 콤보박스를 읽기 전용으로 설정
        cityCombo.place(x=100, y=30)
        cityCombo.set('목록')  # 초기 선택값 설정

# 테스트를 위한 기본 윈도우 설정
if __name__ == "__main__":
    root = Tk()
    root.geometry("300x200")
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)
    SearchFrame(frame)
    root.mainloop()
