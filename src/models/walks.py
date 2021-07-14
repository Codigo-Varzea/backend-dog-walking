import uuid
from enum import Enum

class WalkStatus(Enum):
    WAITING = 1
    WALKING = 2
    DONE = 3


class Walk(object):
    def __init__(self, status, schedule_date, price, duration, latitude, longitude, pets, start_time, end_time):
        self.id = uuid.uuid4()
        self.status = status
        self.schedule_date = schedule_date
        self.price = price
        self.duration = duration
        self.latitude = latitude
        self.longitude = longitude
        self.pets = pets
        self.start_time = start_time
        self.end_time = end_time
    
    def __eq__(self, other):
        return self.id == other.id


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
    
    def fetch_all(self):
        return self.walks

