import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.minho


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://datalab.naver.com/keyword/realtimeList.naver',headers=headers)
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
soup = BeautifulSoup(data.text, 'html.parser')

# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
rank_list = soup.select("#content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul.ranking_list")

rank_num = 0
for rank in rank_list:
    keyword_list = rank.select("li > div > span.item_title_wrap > span")

    for keyword in keyword_list:
        rank_num = rank_num+1
        doc = {
            'rank': rank_num,
            'keyword': keyword.text,
            'datetime': '202008262200'
        }
        print(doc)

        db.keyword2.insert_one(doc)

finance = soup.select("#contentarea > div.box_type_l > table > tbody > tr")

for stock in finance:
    stock_list = stock.select("td > a")
    print(stock_list)