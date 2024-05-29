import tkinter as tk
from PIL import Image, ImageTk
import requests
import io

# NCP 콘솔에서 복사한 클라이언트ID와 클라이언트Secret 값
client_id = "yubnuki0kx"
client_secret = "UI2Z81P20kkJD08qmYRaClqtHW6gfZ3QnxikUpA4"

# 좌표 (경도, 위도)
endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
}
# 중심 좌표
lon, lat = "127.020326886309", "37.5164324582415"
_center = f"{lon},{lat}"
# 줌 레벨 - 0 ~ 20
_level = 16
# 가로 세로 크기 (픽셀)
_w, _h = 500, 300
# 지도 유형 - basic, traffic, satellite, satellite_base, terrain
_maptype = "satellite"
# 반환 이미지 형식 - jpg, jpeg, png8, png
_format = "png"
# 고해상도 디스플레이 지원을 위한 옵션 - 1, 2
_scale = 1
# 마커
_markers = f"""type:d|size:mid|pos:{lon} {lat}|color:red"""
# 라벨 언어 설정 - ko, en, ja, zh
_lang = "ko"
# 대중교통 정보 노출 - Boolean
_public_transit = True
# 서비스에서 사용할 데이터 버전 파라미터 전달 CDN 캐시 무효화
_dataversion = ""

# URL
url = f"{endpoint}?center={_center}&level={_level}&w={_w}&h={_h}&maptype={_maptype}&format={_format}&scale={_scale}&markers={_markers}&lang={_lang}&public_transit={_public_transit}&dataversion={_dataversion}"
res = requests.get(url, headers=headers)

if res.status_code == 200:
    image_data = io.BytesIO(res.content)
    image = Image.open(image_data)

    # Tkinter 설정
    root = tk.Tk()
    root.title("Naver Map")

    # Canvas 설정
    canvas = tk.Canvas(root, width=_w, height=_h)
    canvas.pack()

    # PIL 이미지를 Tkinter 이미지로 변환
    tk_image = ImageTk.PhotoImage(image)

    # Canvas에 이미지 추가
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # Tkinter 이벤트 루프 실행
    root.mainloop()
else:
    print("이미지를 가져오는데 실패했습니다. 상태 코드:", res.status_code)

