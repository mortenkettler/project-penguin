from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
import urllib.parse


db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\MSSQLLocalDB;DATABASE=BeerDB;Trusted_Connection=yes"
    )
    encoded_string = urllib.parse.quote_plus(connection_string)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={encoded_string}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    Swagger(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
