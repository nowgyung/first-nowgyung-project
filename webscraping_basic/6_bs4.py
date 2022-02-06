#beautifulsoup은 웹 스크래핑을 위한 패키지, lxml은 구문을 분석하기 위한 파써

import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #가져온 html 문서를 lxml 파써를 통해 BeautifulSoup 객체로 만든것
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup 객체에서 처음 발견되는 a element를 출력
# soup은 가져온 html문서를 가지고 있는데 그 중에서 첫번째로 발견되는 a태그에 대한 정보를 뿌려줘
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# attributes a href? onclick? 속성에 대한 설명
#print(soup.a["href"]) # a element 의 href 속석 '값' 정보를 출력
# 원하는 속성 가져오고싶을때

# 웹 스크래핑 하려는 페이지에 대해서 잘 모름. 그럴때 사용하는
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element를 찾아줘, 처음으로 발견되는 
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element를 찾아줘
#print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)