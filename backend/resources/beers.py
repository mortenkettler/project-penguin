
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import beers, breweries
from schemas import BeerSchema, BeerUpdateSchema

blp = Blueprint("Beers", __name__, description="Operations on Beers")


@blp.route("/beers/<string:beer_id>")
class Beers(MethodView):
    @blp.response(200, BeerSchema)
    def get(self, beer_id):
        try:
            return beers[beer_id]
        except KeyError:
            abort (404, "Beer not found.")

    def delete(self, beer_id):
        try:
            del beers[beer_id]
            return {"message": "Beer deleted."}
        except KeyError:
            return abort(404, message="Beer not found.")    

    @blp.arguments(BeerUpdateSchema)
    @blp.response(200, BeerSchema)
    def put(self, beer_data, beer_id): #_data has to go before _id (route arg)
        try:
            beer = beers[beer_id]
            beer |= beer_data
            return beer
        except KeyError:
            abort(404, message="Beer not found.")

@blp.route("/beers")
class BeerList(MethodView):
    @blp.response(200, BeerSchema(many=True))
    def get(self):
        return beers.values()
    
    @blp.arguments(BeerSchema)
    @blp.response(201, BeerSchema)
    def post(self, beer_data):
        # using the decorator and the input, we can delete the request()
        #beer_data = request.get_json()
        # validation should include: is data sent in and is it the right kind of data?
        # use marshmallow in schemas.py
        # check for already existing is still manual
        for beer in beers.values():
            if (
                beer_data["name"] == beer["name"]
                and beer_data["brewery_id"] == beer["brewery_id"]
            ):
                abort(400, message=f"Beer already added.")
        if beer_data["brewery_id"] not in breweries:
            return abort(404, message="Brewery not found.")
        beer_id = uuid.uuid4().hex
        # unpack the data and put it in dict
        new_beer = {**beer_data, "id": beer_id} 
        beers[beer_id] = new_beer
        return new_beer