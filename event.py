from mentor import Mentor
from student import Student

class Event:
    def __init__(self, name, time, place, length, attendants=[]):
        self.name = name
        self.time = time
        self.place = place
        self.length = length
        self.attendants = attendants
