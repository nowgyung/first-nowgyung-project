import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a" , attrs={"class" : "title"}) #조건에 해당하는 모든 element를 찾는다 / 태그명이 a 이고, class명이 title인 값 모두 가져옴
for cartoon in cartoons:
    print(cartoon.get_text())