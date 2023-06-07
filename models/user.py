from models.db import DB

class User:
    def __init__(self, username, name, password, coin=0, money=0):
        self.username = username
        self.name = name
        self.password = password
        self.coin = coin
        self.money = money
        self.coins = {}

    def save(self):
        DB.users.insert_one(self.__dict__)
        
    def deposit_money(self, amount):
        self.money += amount

    def withdraw_money(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            raise ValueError("Insufficient balance.")
        
    def update_user(self):
        DB.users.update_one({"username": self.username}, {"$set": self.__dict__})

    def buy_coin(self, coin, amount):
        if amount * coin.price <= self.money:
            if coin.name in self.coins:
                self.coins[coin.name] += amount
            else:
                self.coins[coin.name] = amount
            self.money -= amount * coin.price
        else:
            raise ValueError("Insufficient balance.")

    def sell_coin(self, coin, amount):
        if coin.name in self.coins:
            self.coins[coin.name] -= amount
            self.money += amount * coin.price
        else:
            raise ValueError("Insufficient balance.")
        
    

    @staticmethod
    def get_user_by_username(username):
        user_data = DB.users.find_one({"username": username})
        if user_data:
            return User(
                username=user_data["username"],
                name=user_data["name"],
                password=user_data["password"],
                coin=user_data.get("coin"),
                money=user_data.get("money")
            )
        return None

    @staticmethod
    def get_user_by_name(username):
        user_data = DB.users.find_one({"username": username})
        if user_data:
            return User(
                username=user_data["username"],
                name=user_data["name"],
                password=user_data["password"],
                coin=user_data.get("coin"),
                money=user_data.get("money")
            )
        return None

    def save(self):
        DB.users.insert_one(self.__dict__)

    @classmethod
    def find_by_username(cls, username):
        user_data = DB.users.find_one({"username": username})
        return user_data

    @staticmethod
    def authenticate(username, password):
        user_data = User.find_by_username(username)
        if user_data and user_data["password"] == password:
            return User(
                username=user_data["username"],
                name=user_data["name"],
                password=user_data["password"],
                coin=user_data.get("coin"),
                money=user_data.get("money")
            )
        return None
