from flask import Blueprint, render_template, request, redirect, url_for, session
from models.coin import Coin
from models.user import User
from models.transactions import Transaction
from models.public import Public

user_bp = Blueprint("user", __name__)

@user_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # 사용자 정보를 가져오는 코드
        username = request.form.get("username")
        if User.find_by_username(username):
            return render_template("error.html", error_message="이미 존재하는 사용자입니다.")
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
@user_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("user.login"))

@user_bp.route('/mypage', methods=["GET", "POST"])
def mypage():
    if request.method == "POST":
        # 이쪽 코드들 사용 안됨
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
            # 마켓에 코인을 판매 등록한다
            sell_amount = float(request.form.get("amount"))
            sell_price = float(request.form.get("price"))
            username = session["username"]
            Transaction.regist_coin(username, sell_amount, sell_price)


        return redirect(url_for("user.mypage"))
    else:
        if "username" in session:
            username = session["username"]
            user = User.get_user_by_username(username)
            coins = Coin.get_all_coins()
            market_coin = Public.get_coin_count()
            # register된 코인의 거래 내역을 가져온다
            register_transactions = Transaction.get_transactions_by_type("register") #register된 코인의 거래 내역
            transactions = Transaction.get_transaction_history(username) #유저의 거래 내역
            
            recent_transactions = Transaction.get_recent_transactions()
            recent_prices = []
            for transaction in recent_transactions:
                recent_prices.append(int(transaction["price"]))
            return render_template("mypage.html", user=user, coins=coins, transactions=transactions, market_coin=market_coin, register_transactions=register_transactions, recent_prices=recent_prices)
        else:
            return redirect(url_for("login"))