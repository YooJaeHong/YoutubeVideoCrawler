import urllib.request
from bs4  import BeautifulSoup
from flask import Flask, render_template
from flask import request

'''
플라스크는 html/db 으로 넘겨주고 받는역할
예외처리는 일단 해당부분에 주석으로 표기

검색 키워드 입력 (html)
입력된 값을 파이썬에서 받음(flask)
검색주소 : https://www.youtube.com/results?search_query= + 입력된 값
beautifulsoup(검색주소) 파싱
맨 처음 영상 링크로 넘어가서
모든 다음 동영상에 대해 반복
영상의 링크 타고 넘어감
모든 다음 동영상에 대해 비디오 키값 파싱
자료구조(db)에 저장(flask)
반복 종료
모든 비디오 키값이 저장된 테이블에 대해 키값 / 빈도수 뷰 생성
뷰에서 빈도수 상위 n개를 html으로 보냄(flask) (비디오 키값/ 빈도수)
html에서 받은 데이터로 연관 동영상 테이블생성
html에서 ui보여줌
'''

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)