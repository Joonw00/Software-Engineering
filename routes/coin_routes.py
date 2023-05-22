from flask import Blueprint, render_template, request, redirect, url_for, session

coin_bp = Blueprint("coin", __name__)

@coin_bp.route("/coin_exchange", methods=["GET", "POST"])
def coin_exchange():
    if request.method == "POST":
        # 코인 거래 정보를 가져오는 코드
        pass
    else:
        # GET 요청에 대한 처리 코드
        if "username" in session: # 세션에 사용자 이름이 있는지 확인
            username = session["username"]
            name = session["name"]
            coin = session["user_coin"]
            money = session["user_money"]
            # 로그인한 사용자에 대한 처리
            return render_template("coin_exchange.html", username=username, name=name, user_coin=coin, user_money=money)
        else:
            # 로그인되지 않은 사용자에 대한 처리
            return redirect(url_for("login"))