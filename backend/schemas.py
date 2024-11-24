from marshmallow import Schema, fields

class BeerSchema(Schema):
    # dump_only: cannot be sent through API in payload
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    abv = fields.Float(required=True)
    brewery_id = fields.Str(required=True)

class BeerUpdateSchema(Schema):
    name = fields.Str()
    abv = fields.Float()
    
class BrewerySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
