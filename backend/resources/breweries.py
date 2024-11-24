import uuid
from schemas import BrewerySchema
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import breweries

blp = Blueprint("breweries", __name__, description="Operations on Breweries")

@blp.route("/breweries/<string:brewery_id>")
class Breweries(MethodView):
    @blp.response(200, BrewerySchema)
    def get(self, brewery_id):
        try:
            return breweries[brewery_id]
        except KeyError:
            return abort(404, message="Brewery not found.")

    # no decorators because only returns msg
    def delete(self, brewery_id):
        try:
            del breweries[brewery_id]
            return {"message": "Brewery deleted."}
        except KeyError:
            return abort(404, message="Brewery not found.")   
        
@blp.route("/breweries")
class BreweryList(MethodView):
    @blp.response(200, BrewerySchema(many=True))
    def get(self):
        return breweries.values()

    @blp.arguments(BrewerySchema)
    @blp.response(201, BrewerySchema)
    def post(self, brewery_data):
        for brewery in breweries.values():
            if brewery_data["name"] == brewery["name"]:
                abort(400, message=f"Brewery already exists.")
        brewery_id = uuid.uuid4().hex
        # unpack the data and put it in dict
        new_brewery = {**brewery_data, "id": brewery_id} 
        breweries[brewery_id] = new_brewery
        return new_brewery