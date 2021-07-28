import uuid
from marshmallow import Schema, fields

class Pet(object):
    def __init__(self, name, breed):
        self.id = uuid.uuid4()
        self.name = name
        self.breed = breed
    
    def __eq__(self, other):
        return self.id == other.id

class PetSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    breed = fields.Str()