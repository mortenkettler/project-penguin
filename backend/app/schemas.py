from marshmallow import fields, Schema

class BeerStyleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
