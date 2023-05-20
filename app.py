# Mongo DB사용
from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# from datetime import datetime
import os

app = Flask(__name__)

# static_dir = os.path.abspath('./src/static')
# template_dir = os.path.abspath('./src/templates')

# templates 실행
@app.route('/')
def layout():
    # routes폴더로 상세경로 지정
    return render_template('login.html')

# /login 경로로 접속시 실행
@app.route('/login', methods=['GET', 'POST'])
def login():
    # POST방식으로 접근시
    if request.method == 'POST':
        # login.html에서 입력한 id와 pw를 받아옴
        id = request.form['userid']
        pw = request.form['userpw']
        #routes를 통해 mongoDB에 접근해 id와 pw를 받아옴
        # id와 pw가 일치할 경우
        if id == 'admin' and pw == '1234':
            return render_template('market.html')
        # id와 pw가 일치하지 않을 경우
        else:
            return render_template('login.html')
    # GET방식으로 접근시
    else:
        # login.html로 이동
        return redirect(url_for('/'))


if __name__ == '__main__':
    # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
    app.run(debug=True) # debug=True는 수정하면 바로바로 반영됨
