from models.db import DB

class User:
    def __init__(self, username, name, password, coin=0, money=0):
        self.username = username
        self.name = name
        self.password = password
        self.coin = coin
        self.money = money

    def save(self):
        DB.users.insert_one(self.__dict__)

    @classmethod
    def find_by_username(cls, username):
        user_data = DB.users.find_one({"username": username})
        return user_data

    @staticmethod
    # 로그인 성공 여부를 반환하는 메소드
    def authenticate(username, password):
        user_data = User.find_by_username(username)
        if user_data and user_data["password"] == password:
            return True
        return False
