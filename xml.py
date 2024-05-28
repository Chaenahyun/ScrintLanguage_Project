# import requests
# # url = 'https://openapi.gg.go.kr/TninsttInstutM'
# from bs4 import BeautifulSoup
# import urllib
#
# open_api_key = 'ff47d1d708e3432cb12c14f70bdffb56'
# SIGUN_NM = urllib.parse.quote(input())
# params = '&SIGUN_NM='+SIGUN_NM
# url = 'https://openapi.gg.go.kr/TninsttInstutM?KEY='
# open_url = url + open_api_key + params
#
# req = requests.get(open_url)
# html = req.text
#
# soup = BeautifulSoup(html, 'html.parser')
# values = soup.find_all('faclt_nm')
# print([x.text for x in values][:5])