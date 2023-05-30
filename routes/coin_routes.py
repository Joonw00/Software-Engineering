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
        Coin.sellCoin('coin', amount, price)
        result = f"코인 판매 완료: 코인 {amount}개, 가격 {price}원"
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
