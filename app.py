from flask import Flask
from routes.coin_routes import coin_bp
from routes.user_routes import user_bp
# from models.user import User, db

app = Flask(__name__)



app.register_blueprint(coin_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run()
