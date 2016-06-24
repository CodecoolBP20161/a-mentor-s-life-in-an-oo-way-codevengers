from event import Event


class PrivateMentoring(Event):
    def __init__(self, students, mentor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.students = students
        self.mentor = mentor

    @staticmethod
    def do_event(students, mentor):
        for student in students:
            student.happy = True
            student.knowledge_level += 10
            student.motivation_level += 10
            student.energy_level -= 5

        mentor.happy = True
        mentor.motivation_level += 15
        mentor.energy_level -= 5
        return students, mentor
