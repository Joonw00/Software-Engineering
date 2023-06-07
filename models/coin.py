from models.db import DB
from flask import session
from models.transactions import Transaction

users_collection = DB["users"]
coins_collection = DB["coins"]

class Coin:
    def __init__(self, name, price, count=0, price_change=0):
        self.name = name
        self.price = price
        self.count = count
        self.price_change = price_change
    
    def save(self):
        DB.coins.update_one({"name": self.name}, {"$set": self.__dict__}, upsert=True)

    @staticmethod
    def initialize_coin(coin_count, coin_price):
        coin = Coin.get_coin()
        if coin is None:
            coin = Coin("Bitcoin", coin_price, coin_count)
            coin.save()

    @staticmethod
    def get_coin():
        coin_data = DB.coins.find_one()
        if coin_data:
            return Coin(coin_data["name"], coin_data["price"], coin_data.get("count", 0), coin_data.get("price_change", 0))
        return None

    @staticmethod
    def get_all_coins():
        coin_data = DB.coins.find()
        coins = []
        for coin in coin_data:
            coins.append(Coin(coin["name"], coin["price"], coin.get("count", 0), coin.get("price_change", 0)))
        return coins

    @staticmethod
    def get_coin_by_name(name):
        coin_data = DB.coins.find_one({"name": name})
        if coin_data:
            return Coin(coin_data["name"], coin_data["price"], coin_data.get("count", 0), coin_data.get("price_change", 0))
        return None

    @staticmethod
    def get_user_money():
        user_money = 10000  # 가정: 사용자의 돈을 10000으로 설정
        return user_money

    @staticmethod
    def decrease_user_money(amount):
        user_money = Coin.get_user_money()
        user_money -= amount
        # 사용자의 돈을 업데이트하는 로직 구현

    @staticmethod
    def increase_user_coin(amount):
        user_coin = Coin.get_user_coin()
        user_coin += amount
        # 사용자의 코인을 업데이트하는 로직 구현

    @staticmethod
    def get_seller_money():
        seller_money = 10000  # 가정: 판매자의 돈을 10000으로 설정
        return seller_money

    @staticmethod
    def decrease_seller_money(amount):
        seller_money = Coin.get_seller_money()
        seller_money -= amount
        # 판매자의 돈을 업데이트하는 로직 구현

    @staticmethod
    def increase_seller_coin(amount):
        seller_coin = Coin.get_seller_coin()
        seller_coin += amount
        # 판매자의 코인을 업데이트하는 로직 구현

    @staticmethod
    def get_user_coin():
        user_coin = 0  # 가정: 사용자의 코인을 0으로 설정
        return user_coin

    @staticmethod
    def decrease_user_coin(amount):
        user_coin = Coin.get_user_coin()
        user_coin -= amount
        # 사용자의 코인을 업데이트하는 로직 구현

    @staticmethod
    def update_coin_price(new_price):
        # name이 Bitcoin인 항목 업데이트
        DB.coins.update_one({"name": "Bitcoin"}, {"$set": {"price": new_price}})
    
    @staticmethod
    def update_coin_count(new_count):
        DB.coins.update_one({"name": "Bitcoin"}, {"$set": {"count": new_count}})

    @staticmethod
    def update_price_change(name, price_change):
        DB.coins.update_one({"name": name}, {"$set": {"price_change": price_change}})

    # coin_routes.py에서 사용, transaction으로 접근 시 사용되는 코드
    @staticmethod
    def deposit(price):
        # 세션을 통해 사용자 정보를 받아오기
        username =  session["username"]
        user = get_user(username)
        user["money"] += int(price)
        update_user(user)
        Transaction.add_transaction(username, "deposit", None, price)

    @staticmethod
    def withdraw(price):
        username =  session["username"]
        user = get_user(username)
        user["money"] -= int(price)
        update_user(user)
        Transaction.add_transaction(username, "withdraw", None, price)


    # 마켓 플레이스에서 코인 구매
    @staticmethod
    def buyCoin(coin, amount, price):
        username =  session["username"]
        user = get_user(username)
        user["coin"] += int(amount)
        user["money"] -= int(amount) * 100
        remain_coin = Coin.get_coin_by_name("Bitcoin").count - int(amount)
        # 업데이트
        Coin.update_coin_count(remain_coin)
        update_user(user)
        Transaction.add_transaction(username, "buy", amount, price)

    @staticmethod
    def sellCoin(coin, amount, price):
        username =  session["username"]
        user = get_user(username)
        user["coin"] -= int(amount)
        # user["money"] += int(price)
        update_user(user)
        Transaction.add_transaction(username, "sell", coin, price)


def get_user(username):
    # 사용자 정보 조회
    user = users_collection.find_one({"username": username})
    return user

def update_user(user):
    # 사용자 정보 업데이트
    username = user["username"]
    users_collection.update_one({"username": username}, {"$set": user})