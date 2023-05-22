from flask import Flask
from routes.coin_routes import coin_bp
from routes.user_routes import user_bp
from routes.public_routes import public_bp
# from models.coin import Coin
# from models.user import User, db

app = Flask(__name__)

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw" # TODO: 환경변수로 변경

# app.register_blueprint(coin_bp)
app.register_blueprint(user_bp) # 로그인 사용자를 위한 엔드포인트
app.register_blueprint(public_bp)

if __name__ == "__main__":
    # 초기화 코드
    # Coin.initialize_coin(100, 100)
    app.run()
