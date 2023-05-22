from flask import Blueprint, render_template
from models.public import Public
from models.transactions import Transaction

public_bp = Blueprint('public', __name__)

@public_bp.route('/public')
def public_page():
    coins = Public.query_all_coins()
    transactions = Transaction.get_all_transactions()
    return render_template('public.html', coins=coins, transactions=transactions)
