from student import Student


class Event:
    def __init__(self, name, time, place, length, attendants=None):
        if attendants is None:
            self.attendants = []
        else:
            self.attendants = attendants
        self.name = name
        self.time = time
        self.place = place
        self.length = length
        
