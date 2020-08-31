import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.minho
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/sise/sise_rise.nhn',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
finance = soup.select("table.type_2 > tr")
for stock in finance:
    finance_rank = stock.select_one("td.no")
    finance_info_td = stock.select('td')

    if finance_rank:
        if int(finance_info_td[0].text.strip()) > 50 :
            break

        doc = {
            'ranking': finance_info_td[0].text.strip(),
            'stock_name': finance_info_td[1].select_one('a').text.strip(),
            'increase': finance_info_td[2].text.strip(),
            'datetime': '202008242200'
        }
        print(doc)

        db.stock.insert_one(doc)

# print(finance_info_td[0].text.strip(),
#     finance_info_td[1].select_one('a').text.strip(),


#from bs4 import BeautifulSoup
#import requests

#from pymongo import MongoClient

#from flask import Flask, render_template, jsonify, request

#app = Flask(__name__)

#client = MongoClient('localhost', 27017)
#db = client.minho


# 타겟 URL을 읽어서 HTML를 받아오고,
#headers = {
#        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#data = requests.get('https://finance.naver.com/sise/sise_rise.nhn',headers=headers)
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
#soup = BeautifulSoup(data.text, 'html.parser')


#finance = soup.select("#contentarea > div.box_type_l > table > tbody > tr")

#for stock in finance:
 #   stock_list = stock.select("td > a.title ")
 #   print(stock_list)





        #print(finance_info_td[0].text.strip(),
         #     finance_info_td[1].select_one('a').text.strip(),
              #finance_info_td[2].text.strip(),
              #finance_info_td[3].text.strip(),
          #    finance_info_td[4].text.strip(),
           #   finance_info_td[5].text.strip(),
            #  finance_info_td[6].text.strip())
              #finance_info_td[7].text.strip(),
              #finance_info_td[8].text.strip(),
              #finance_info_td[9].text.strip(),
              #finance_info_td[10].text.strip(),
              #finance_info_td[11].text.strip())
