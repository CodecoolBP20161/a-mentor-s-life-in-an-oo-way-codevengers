import datetime
from event import Event


class Leisure(Event):
    def __init__(self, name, time, place, length, attendants):
        super().__init__(name, time, place, length, attendants)

    def do_event(self):
        for attendant in attendants:
            attendant.energy_level += 5
            attendant.motivation_level += 5
            attendant.happy = True
        return attendants
