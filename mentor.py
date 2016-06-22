import random
from person import Person

class Mentor(Person):
    @classmethod
    def create_by_csv(cls, file_name):
        import csv
        with open(file_name) as csvfile:
            mentors = csv.reader(csvfile,  delimiter=';')
            mentors_list = []
            for row in mentors:
                mentors_list.append(row)
        return mentors_list

    def __init__(self, first_name,  last_name, year_of_birth, gender,  nickname):
        super().__init__(first_name,
                         last_name,
                         year_of_birth,
                         gender)

        self.nickname = nickname
        self.energy_level = None

    @staticmethod
    def do_morning_gym(students, mentors):
        for student in students:
            if student.energy_level < 10:
                student.energy_level += 20
            else:
                student.energy_level += 10
        for mentor in mentors:
            if mentor.energy_level < 10:
                mentor.energy_level += 20
            else:
                mentor.energy_level += 10
        return students, mentors

    @staticmethod
    def daily_agenda(students):
        for student in students:
            if studied_level:
                students.motivation_level += 10
            else:
                students.motivation_level -= 10
        return students

    def mentoring(self, student):
        student.happy = True
        student.knowledge_level += 10
        student.motivation_level += 10
        student.energy_level -= 10
        self.motivation_level += 5
        return student

    @staticmethod
    def interview(candidate, mentors):
        candidate_in_school = True
        choice = 0
        for mentor in mentors:
            choice += random.randrange(0, 2)
        if choice == 3:
            accepted = True
            candidate.motivation_level += 10
        return candidate
