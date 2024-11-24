from flask import Flask
from flask_smorest import Api

from resources.beers import blp as BeersBlueprint
from resources.breweries import blp as BreweriesBlueprint

app = Flask(__name__) 
# create Flask app, run with flask run, which looks for app.py

# automated tests:  how do we want to introduce them?

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "BeerDB REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" #jsdelivr w/o an 'e'!

api = Api(app)
api.register_blueprint(BeersBlueprint)
api.register_blueprint(BreweriesBlueprint)