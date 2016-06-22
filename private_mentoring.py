from event import Event


class PrivateMentoring(Event):
    def __init__(self, students, mentor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.students = students
        self.mentor = mentor

    def do_event(self):
        for student in self.students:
            student.happy = True
            student.knowledge_level += 10
            student.motivation_level += 10
            student.energy_level -= 5

        self.mentor.happy = True
        self.mentor.motivation_level += 150
        self.mentor.energy_level -= 5
