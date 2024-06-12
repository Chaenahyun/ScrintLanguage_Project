import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.font import Font
import tkinter.ttk
import matplotlib.font_manager as fm

# 하드코딩된 데이터 (예시 데이터)
data = [
    {'SIGUN_NM': '고양시', 'STDNT_CNT': 30000},
    {'SIGUN_NM': '과천시', 'STDNT_CNT': 15000},
    {'SIGUN_NM': '광명시', 'STDNT_CNT': 20000},
    {'SIGUN_NM': '광주시', 'STDNT_CNT': 18000},
    {'SIGUN_NM': '구리시', 'STDNT_CNT': 17000},
    {'SIGUN_NM': '군포시', 'STDNT_CNT': 21000},
    {'SIGUN_NM': '김포시', 'STDNT_CNT': 25000},
    {'SIGUN_NM': '남양주시', 'STDNT_CNT': 27000},
    {'SIGUN_NM': '동두천시', 'STDNT_CNT': 14000},
    {'SIGUN_NM': '부천시', 'STDNT_CNT': 35000},
    {'SIGUN_NM': '성남시', 'STDNT_CNT': 40000},
    {'SIGUN_NM': '수원시', 'STDNT_CNT': 42000},
    {'SIGUN_NM': '시흥시', 'STDNT_CNT': 19000},
    {'SIGUN_NM': '안산시', 'STDNT_CNT': 31000},
    {'SIGUN_NM': '안성시', 'STDNT_CNT': 16000},
    {'SIGUN_NM': '안양시', 'STDNT_CNT': 33000},
    {'SIGUN_NM': '양주시', 'STDNT_CNT': 17000},
    {'SIGUN_NM': '여주시', 'STDNT_CNT': 12000},
    {'SIGUN_NM': '오산시', 'STDNT_CNT': 13000},
    {'SIGUN_NM': '용인시', 'STDNT_CNT': 41000},
    {'SIGUN_NM': '의왕시', 'STDNT_CNT': 11000},
    {'SIGUN_NM': '의정부시', 'STDNT_CNT': 29000},
    {'SIGUN_NM': '이천시', 'STDNT_CNT': 15000},
    {'SIGUN_NM': '파주시', 'STDNT_CNT': 24000},
    {'SIGUN_NM': '평택시', 'STDNT_CNT': 23000},
    {'SIGUN_NM': '포천시', 'STDNT_CNT': 14000},
    {'SIGUN_NM': '하남시', 'STDNT_CNT': 16000},
    {'SIGUN_NM': '화성시', 'STDNT_CNT': 38000},
    {'SIGUN_NM': '가평군', 'STDNT_CNT': 9000},
    {'SIGUN_NM': '양평군', 'STDNT_CNT': 10000},
    {'SIGUN_NM': '연천군', 'STDNT_CNT': 8000}
]

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 윈도우의 경우
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 시각화 함수
def visualize_data(canvas_frame):
    sigun_names = [item['SIGUN_NM'] for item in data]
    student_counts = [item['STDNT_CNT'] for item in data]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(sigun_names, student_counts, color='skyblue')
    ax.set_xlabel('시군명')
    ax.set_ylabel('학생 수')
    ax.set_title('경기도 시군별 학생 수')
    ax.set_xticklabels(sigun_names, rotation=45, ha='right')

    # Clear the previous plot
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    # Embed the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tkinter GUI 설정
class VisualizationApp:
    def __init__(self, frame):
        self.Labelfont = Font(family='210 나무고딕 EB', weight='bold', slant='roman', size=18)

        Label(frame, text='경기도 시군별 학생수', font=self.Labelfont).pack()

        self.canvas_frame = Frame(frame)
        self.canvas_frame.pack(pady=20, fill=BOTH, expand=True)

        visualize_data(self.canvas_frame)

# Tkinter 앱 실행
root = Tk()
root.title("경기도 시군별 학생수 시각화")
root.geometry("1200x800")
app = VisualizationApp(root)
root.mainloop()
