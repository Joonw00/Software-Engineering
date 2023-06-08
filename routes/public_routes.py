from flask import Blueprint, render_template
from models.public import Public
from models.transactions import Transaction

public_bp = Blueprint('public', __name__)

@public_bp.route('/public')
def public_page():
    coins = Public.query_all_coins()
    coin_count = Public.get_coin_count()
    trans_done = Transaction.get_transactions_by_type("trans_done")
    trans_regist = Transaction.get_transactions_by_type("register")

    # 그래프에 들어갈 데이터
    # 최근 10개의 거래내역을 가져온다.
    recent_transactions = Transaction.get_recent_transactions()
    recent_prices = []
    for transaction in recent_transactions:
        recent_prices.append(int(transaction["price"]))
    return render_template('public.html', coins=coins, trans_regist=trans_regist, coin_count=coin_count, trans_done=trans_done, recent_prices=recent_prices)
