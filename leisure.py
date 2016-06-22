import datetime
from event import Event


class Leisure(Event):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_event(self):
        for attendant in attendants:
            attendant.energy_level += 5
            attendant.motivation_level += 5
            attendant.happy = True
        return attendants
