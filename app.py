from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.orders import orders
from routes.orderdetails import orderDetails
from flask_bcrypt import Bcrypt
from utils.loginManagerService import login_manager
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)


app.register_blueprint(auth)
app.register_blueprint(orders)
app.register_blueprint(orderDetails)
