from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.minho  # 'minho'라는 이름의 db를 만듭니다.

## HTML을 주는 부분

@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/keyword', methods=['GET'])
def sort_keyword():
    stocks = list(db.stock.find({'datetime':'202008242200' },{'_id':0}))

    return jsonify({'result': 'success', 'msg': '검색결과입니다!', 'stock': stocks})

@app.route('/stock', methods=['GET'])
def sort_stcok():
    keywords = list(db.keyword.find({'datetime':'202008242200' },{'_id':0}))

    return jsonify({'result': 'success', 'msg': '검색결과입니다', 'keyword': keywords})

#엑셀 다운로드 구현 필요
#@app.route('/down', methods=[''])
#def excel():
#   exceldoc = ()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)