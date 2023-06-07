from models.db import DB
from datetime import datetime

class Transaction:
    collection = DB["transactions"]

    @classmethod
    def get_all_transactions(cls):
        return list(cls.collection.find())
    
    @classmethod
    def get_buy_transactions(cls):
        return list(cls.collection.find({"transaction_type": "buy"}))

    @classmethod
    def get_transactions_by_username(cls, username):
        return list(cls.collection.find({"username": username}))
    
    @staticmethod
    def get_transaction_history(username):
        transactions = DB.transactions.find({'username': username})
        return transactions
    
    @staticmethod
    def get_transactions_by_type(transaction_type):
        transactions = DB.transactions.find({'transaction_type': transaction_type})
        # for transaction in transactions:
        #     print(transaction)
        return transactions
    
    @staticmethod
    def add_transaction(username, transaction_type, amount, price):
        transaction = {
            'username': username,
            'transaction_type': transaction_type,
            'amount': amount,
            'price': price,
            'timestamp': datetime.now()
        }
        DB.transactions.insert_one(transaction)

    @staticmethod
    def del_transaction(idx):
        DB.transactions.delete_one({'idx': idx})

    @staticmethod
    def transaction_done(seller, buyer, amount, price):
        transaction = {
            'seller': seller,
            'buyer': buyer,
            'transaction_type' : 'trans_done',
            'amount': amount,
            'price': price,
            'idx': DB.transactions.count_documents({}) + 1,
            'timestamp': datetime.now()
        }
        DB.transactions.insert_one(transaction)

    @staticmethod
    def regist_coin(username, amount, price):
        # transaction_type은 register로 설정한다
        transaction = {
            'username': username,
            'transaction_type': 'register',
            'amount': amount,
            'price': price,
            'idx': DB.transactions.count_documents({}) + 1,
            'timestamp': datetime.now()
        }
        DB.transactions.insert_one(transaction)
