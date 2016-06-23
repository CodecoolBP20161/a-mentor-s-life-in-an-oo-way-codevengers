import random
from person import Person


class Student(Person):

    @classmethod
    def create_by_csv(cls, file_name):
        import csv
        with open(file_name) as csvfile:
            students = csv.reader(csvfile, delimiter=';')
            students_list = []
            for row in students:
                students_list.append(row)
            return students_list

    def __init__(self, first_name,  last_name, year_of_birth, gender):
        super().__init__(first_name,
                         last_name,
                         year_of_birth,
                         gender)

        self.knowledge_level = None
        self.energy_level = None
        self.studied = None

    @staticmethod
    def learn(students):
        for student in students:
            study = random.randrange(2)
            if study == 0:
                student.studied = False
            else:
                student.studied = True
            if student.studied:
                student.knowledge_level += 10
                student.energy_level -= 10
                student.motivation_level += 10
        return students
