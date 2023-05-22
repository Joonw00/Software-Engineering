from flask import Blueprint, render_template, request, redirect, url_for, session
from models.coin import Coin
from models.user import User
from models.transactions import Transaction

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
            return redirect(url_for("user.mypage"))
        else:
            # 로그인 실패 처리
            return render_template("login.html", error="Invalid username or password")

    # GET 요청에 대한 처리 코드
    return render_template("login.html")
@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user_bp.login"))

@user_bp.route('/mypage', methods=["GET", "POST"])
def mypage():
    if request.method == "POST":
        action = request.form.get("action")
        amount = float(request.form.get("amount"))
        user = User.get_user_by_username(session["username"])

        if action == "deposit":
            user.deposit_money(amount)
        elif action == "withdraw":
            user.withdraw_money(amount)
        elif action == "buy":
            coin_name = request.form.get("coin")
            coin = Coin.get_coin_by_name(coin_name)
            if coin is None:
                return "Invalid coin name."
            user.buy_coin(coin, amount)
        elif action == "sell":
            coin_name = request.form.get("coin")
            coin = Coin.get_coin_by_name(coin_name)
            if coin is None:
                return "Invalid coin name."
            user.sell_coin(coin, amount)

        return redirect(url_for("user.mypage"))
    else:
        if "username" in session:
            username = session["username"]
            user = User.get_user_by_username(username)
            coins = Coin.get_all_coins()
            transactions = Transaction.get_transaction_history(username)
            return render_template("mypage.html", user=user, coins=coins, transactions=transactions)
        else:
            return redirect(url_for("login"))