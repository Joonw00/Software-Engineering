from models.db import DB
# from models.transactions import Transaction

class Public:
    collection = DB["coins"]

    @classmethod
    def query_all_coins(cls):
        return list(cls.collection.find())

    @classmethod
    def get_coin_by_id(cls, coin_id):
        return cls.collection.find_one({"_id": coin_id})

    @staticmethod
    def get_coin_count():
        coins_collection = DB["coins"]
        #name이 Bitcoin인 코인의 count를 가져온다.
        coin_count = coins_collection.find_one({"name": "Bitcoin"})["count"]
        return coin_count