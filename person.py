import random


class Person:
    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.motivation_level = random.randint(0, 100)
        self.in_school = False
        self.happy = False

    @staticmethod
    def come_to_school(students, mentors):
        for mentor in mentors:
            mentor.in_school = True
            mentor.happy = True
            mentor.motivation_level = random.randint(1, 100)
            mentor.energy_level = random.randint(1, 100)
        count = 0
        for student in students:
            i = random.randint(0, 1)
            if i == 0 and count < 2:
                student.in_school = False
                count += 1
            else:
                student.in_school = True
                student.happy = True
                student.motivation_level = random.randint(1, 100)
                student.knowledge_level = random.randint(1, 100)
                student.studied = bool(random.randint(0, 1))
                student.energy_level = random.randint(1, 100)
        return students, mentors
