from models.db import DB
from models.transactions import Transaction

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
    def update_coin_price(name, new_price):
        DB.coins.update_one({"name": name}, {"$set": {"price": new_price}})

    @staticmethod
    def update_price_change(name, price_change):
        DB.coins.update_one({"name": name}, {"$set": {"price_change": price_change}})

