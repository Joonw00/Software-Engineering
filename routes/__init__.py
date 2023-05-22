from flask import Blueprint

# 각각의 블루프린트 모듈을 import
from .coin_routes import coin_bp
from .user_routes import user_bp

# 각각의 블루프린트 모듈을 리스트에 추가
blueprints = [coin_bp, user_bp]

# 모든 블루프린트 모듈을 등록할 함수
def register_blueprints(app):
    for bp in blueprints:
        app.register_blueprint(bp)
