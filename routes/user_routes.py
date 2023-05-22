from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User
from models.db import DB

user_bp = Blueprint("user", __name__)

@user_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # 사용자 정보를 가져오는 코드
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")
        user = User(username, name, password, coin=0, money=0)
        user.save()

        # 응답 처리하는 코드
        return redirect(url_for("user.login"))
    else:
        # GET 요청에 대한 처리 코드
        return render_template("signup.html")

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # 로그인 정보를 가져오는 코드
        username = request.form.get("username")
        password = request.form.get("password")
    
        if User.authenticate(username, password):
            # 로그인 성공 처리
            user_data = User.find_by_username(username)
            session["username"] = user_data["username"]
            session["name"] = user_data["name"]
            session["user_coin"] = user_data.get("coin")
            session["user_money"] = user_data.get("money")
            return redirect(url_for("coin.coin_exchange"))
        else:
            # 로그인 실패 처리
            return render_template("login.html", error="Invalid username or password")

    # GET 요청에 대한 처리 코드
    return render_template("login.html")
