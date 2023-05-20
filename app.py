from flask import Flask
from flask_pymongo import PyMongo
from routes.coin_routes import coin_bp
from routes.user_routes import user_bp

app = Flask(__name__)

# MongoDB 연결 정보 설정
#Mongo_uri에는 MongoDB의 연결 URI를 설정
app.config["MONGO_URI"] = "mongodb://localhost:27017/coin_trading" 
#mongodb://localhost:27017/coin_trading는 로컬 MongoDB 서버의 coin_trading 데이터베이스에 연결하는 예시,실제 uri로 수정 필요
mongo = PyMongo(app)

app = Flask(__name__)
app.register_blueprint(coin_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run()
