from flask import Blueprint, request, jsonify
from . import db
from .models import BeerStyle
from .schemas import BeerStyleSchema

api_bp = Blueprint('api', __name__)
beer_schema = BeerStyleSchema()
beer_list_schema = BeerStyleSchema(many=True)

@api_bp.route('/beerstyle', methods=['GET'])
def get_beerstyles_by_name():
    """
    Get all beer styles or search by name.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        description: Name of the beer style to search for
    responses:
      200:
        description: List of beer styles
    """
    query = request.args.get('name')
    if query:
        beerstyles = BeerStyle.query.filter(BeerStyle.name.ilike(f'%{query}%')).all()
    else:
        beerstyles = BeerStyle.query.all()
    return jsonify(beer_list_schema.dump(beerstyles))

@api_bp.route('/beerstyles', methods=['POST'])
def add_beerstyle():
    data = request.get_json()
    errors = beer_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_beer = BeerStyle(**data)
    db.session.add(new_beer)
    db.session.commit()
    return beer_schema.jsonify(new_beer), 201
