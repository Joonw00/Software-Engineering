from models.db import DB
from datetime import datetime

class Transaction:
    collection = DB["transactions"]

    @classmethod
    def get_all_transactions(cls):
        return list(cls.collection.find())

    @classmethod
    def get_transactions_by_username(cls, username):
        return list(cls.collection.find({"username": username}))
    
    @staticmethod
    def get_transaction_history(username):
        transactions = DB.transactions.find({'username': username})
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
