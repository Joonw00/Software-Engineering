from flask import Blueprint, render_template

coin_bp = Blueprint("coin", __name__)

@coin_bp.route("/coin_exchange")
def coin_exchange():
    return render_template("coin_exchange.html")
