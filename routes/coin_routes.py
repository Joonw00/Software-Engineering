from flask import Blueprint, render_template, redirect, url_for, request, session
from models.coin import Coin
from models.user import User
from models.transactions import Transaction

coin_bp = Blueprint('coin_bp', __name__)

@coin_bp.route('/coin_exchange')
def coin_exchange():
    if request.method == "POST":
        pass
    else:
        if "username" in session:
            username = session["username"]
            name = session["name"]
            user_coin = session["user_coin"]
            user_money = session["user_money"]
            coins = Coin.get_all_coins()
            transactions = Transaction.get_transaction_history()

            coin = None  # 코인 변수 초기화
            for c in coins:
                if c.name == user_coin:
                    coin = c
                    break

            if coin is None:
                return "보유한 코인을 찾을 수 없습니다."

            return render_template(
                "coin_exchange.html",
                username=username,
                name=name,
                user_coin=user_coin,
                user_money=user_money,
                coins=coins,
                coin=coin,
                transactions=transactions
            )
        else:
            return redirect(url_for("login"))
        

@coin_bp.route('/transaction', methods=['POST'])
def transaction():
    transaction_type = request.form.get('transaction-type')
    amount = request.form.get('amount')
    price = request.form.get('price')
    # print(transaction_type, amount, price)

    if transaction_type == 'deposit':
        Coin.deposit(price)
        result = f"입금 완료: {price}원"
    elif transaction_type == 'withdraw':
        Coin.withdraw(price)
        result = f"출금 완료: {price}원"
    elif transaction_type == 'buy':
        Coin.buyCoin('coin', amount, price)
        result = f"코인 구매 완료: 코인 {amount}개, 가격 {price}원"
    elif transaction_type == 'sell':
        sell_amount = int(request.form.get("amount"))
        sell_price = int(request.form.get("price"))
        username = session["username"]
        Transaction.regist_coin(username, sell_amount, sell_price)
        result = f"코인 판매 완료: 코인 {amount}개, 가격 {price}원"
    elif transaction_type == "trans_done":
        seller = request.form.get("seller")
        buyer = session["username"]
        idx = int(request.form.get("idx"))
        #판매자 정보와 구매자 정보 받아오기
        seller_info = User.get_user_by_username(seller)
        buyer_info = User.get_user_by_username(buyer)
        #거래 가능한지 확인
        if(int(seller_info.coin) < int(amount)):
            result = "판매자의 코인이 부족합니다." # 판매자의 코인이 부족한 경우
            # 에러 페이지 렌더링
            return render_template("coin_error.html", error_message=result)          
        elif (int(buyer_info.money) < int(price)):
            result = "구매자의 보유금이 부족합니다" # 구매자의 돈이 부족한 경우
            return render_template("coin_error.html", error_message=result)     
        else:
            # 판매자의 돈을 더해주고 코인을 빼준다.
            seller_info.money += int(price) * int(amount)
            seller_info.coin -= int(amount)
            # 구매자의 돈을 빼주고 코인을 더해준다.
            buyer_info.money -= int(price) * int(amount)
            buyer_info.coin += int(amount)
            # 유저 정보를 업데이트한다.
            User.update_user(seller_info)
            User.update_user(buyer_info)
            # transation에서 idx를 통해 거래내역을 찾아 삭제한다
            transaction = Transaction.del_transaction(idx)
            # 거래 완료 내역을 추가한다.
            Transaction.transaction_done(seller, buyer, amount, price)
            result = f"거래 완료: 코인 {amount}개, 가격 {price}원"
    # user의 /mypage 로 이동
    return redirect(url_for('user.mypage'))
    # return redirect(url_for('user.mypage', result=result))




@coin_bp.route('/buy', methods=['POST'])
def buy():
    coin = Coin.get_coin()
    if coin is None:
        return "코인을 찾을 수 없습니다."

    user = User.get_user_by_id(request.form['user_id'])
    if user is None:
        return "사용자를 찾을 수 없습니다."

    amount = int(request.form['amount'])
    total_price = coin.price * amount

    if user.money < total_price:
        return "잔액이 부족합니다."

    if coin.count < amount:
        return "구매 가능한 코인 수량이 부족합니다."

    user.add_coin(coin.name, amount)
    user.subtract_money(total_price)

    coin.count -= amount

    transaction = Transaction('buy', amount, total_price)
    transaction.save()

    return redirect(url_for("coin_bp.coin_exchange"))

@coin_bp.route('/sell', methods=['POST'])
def sell_coin():
    coin_name = request.form.get('coin_name')
    sell_amount = int(request.form.get('sell_amount'))
    coin = Coin.get_coin_by_name(coin_name)
    if coin is None:
        return "코인을 찾을 수 없습니다."

    user_coin = Coin.get_user_coin()
    if sell_amount > user_coin:
        return "보유한 코인이 부족합니다."

    selling_price = coin.price

    Coin.decrease_user_coin(sell_amount)
    Coin.increase_seller_coin(sell_amount)
    Coin.increase_user_money(sell_amount * selling_price)

    transaction = Transaction('sell', sell_amount, selling_price)
    transaction.save()

    return redirect(url_for("coin_bp.coin_exchange"))
