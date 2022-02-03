import requests
#res=requests.get("http://.com")
#res=requests.get("http://nowgyung.tistory.com")
#print("응답코드 :", res.status_code) # 200이면 정상, 파일상태 체크

#if res.status_code == requests.codes.ok: #requests.codes.ok는 200과 같은말
#    print("정상입니다")
#else:
#    print("문제가 생겼습니다. [에러코드 " , res.status_code, "]")

#res.raise_for_status() #올바른 html을 가져왔다면 문제없이, 않은경우 에러발생
#print("웹 스크래핑을 진행합니다")


res=requests.get("http://google.com") #두 줄로 처리 가능, 습관적으로 사용하기
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)