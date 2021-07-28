import uuid
from datetime import datetime, timedelta
from enum import Enum
from marshmallow import Schema, fields
from .pets import PetSchema

class WalkStatus(Enum):
    WAITING = 1
    WALKING = 2
    DONE = 3


class Walk(object):
    def __init__(self, schedule_date, duration, latitude, longitude, pets, status = WalkStatus.WAITING):
        self.id = uuid.uuid4()
        self.status = status
        self.schedule_date = schedule_date
        self.duration = duration
        self.latitude = latitude
        self.longitude = longitude
        self.pets = pets

        self.__set_price()
        self.__set_end_date()
    
    def __set_price(self):
        num_pets = len(self.pets)

        base_price = self.get_base_price()
        if self.duration >= timedelta(minutes=60):
            base_price += 10
        
        self.price = base_price + ((num_pets - 1) * 15)

    def __set_end_date(self):
        self.end_date = self.schedule_date + self.duration
    
    def __eq__(self, other):
        return self.id == other.id

    @staticmethod
    def get_base_price():
        return 25

    @staticmethod
    def from_json(json_post):
        schedule_date = datetime.strptime(json_post.get('schedule_date'), '%Y-%m-%d %H:%M')
        duration = timedelta(minutes=json_post.get('duration'))
        latitude = json_post.get('latitude')
        longitude = json_post.get('longitude')
        pets = json_post.get('pets')
        return Walk(schedule_date, duration, latitude, longitude, pets)

class WalkSchema(Schema):
    id = fields.Str()
    schedule_date = fields.DateTime()
    duration = fields.TimeDelta(precision=fields.TimeDelta.MINUTES)
    latitude = fields.Float()
    longitude = fields.Float()
    pets = fields.Nested(PetSchema, many=True)
    price = fields.Float()
    end_date = fields.DateTime()
    status = fields.Str()

class Walks(object):
    def __init__(self):
        self.walks = []

    def create(self, walk):
        self.walks.append(walk)

    def delete(self, walk):
        self.walks.remove(walk)
    
    def update(self, walk):
        index = self.walks.index(walk)

        self.walks.pop(index)

        self.walks.insert(index, walk)

    def fetch_by_page_index(self, total_per_page, index):
        walks_count = len(self.walks)
        start_index = index * total_per_page
        end_index = start_index + total_per_page
        if end_index >= walks_count:
            end_index = walks_count
        return self.walks[start_index:end_index]
    
    def fetch_all(self):
        return self.walks
    
    def fetch_from_start_date(self, start_date):
        filtered_walks = []

        for walk in self.walks:
            if walk.schedule_date >= start_date:
                filtered_walks.append(walk)

        return filtered_walks
        #return filter(lambda walk: walk.schedule_date > start_date, self.walks)

    def get_by_id(self, id):
        for walk in self.walks:
            if str(walk.id) == id:
                return walk

