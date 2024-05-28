from tkinter import Label, PhotoImage
from PIL import Image

class LoadGIFImage:
    def __init__(self, parent):
        self.label = Label(parent, bg="white")
        self.label.pack()

        self.my_image_number = 0

        # GIF 파일의 실제 프레임 수를 자동으로 감지
        self.image_path = 'gif.gif'
        self.image = Image.open(self.image_path)
        self.frames = [PhotoImage(file=self.image_path, format='gif -index %i' % i) for i in range(self.image.n_frames)]

        # 이미지를 label에 설정
        self.label.config(image=self.frames[0])

        # 애니메이션 속도 설정 (밀리초 단위)
        self.animation_speed = 100  # 예: 100 밀리초 = 0.1초

        self.animate()  # 애니메이션 시작

    def animate(self):
        # label에서 이미지를 읽어오고 gif의 다음 이미지로 교체함
        self.label.config(image=self.frames[self.my_image_number % len(self.frames)])
        self.my_image_number += 1
        self.label.after(self.animation_speed, self.animate)  # 애니메이션 프레임 갱신
