from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_restless import APIManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/storage.db'
db = SQLAlchemy(app)

ma = Marshmallow(app)

# manager = APIManager(app, flask_sqlalchemy_db=db)

