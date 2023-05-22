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
