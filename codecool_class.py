from mentor import Mentor
from student import Student


class CodecoolClass:

    @classmethod
    def generate_local(cls):
        local_class = cls("Budapest", 2016)
        mentors = Mentor.create_by_csv("./data/mentors.csv")
        students = Student.create_by_csv("./data/students.csv")
        for mentor in mentors:
            local_class.mentors.append(Mentor(mentor[0], mentor[1],
                                              int(mentor[2]), mentor[3],
                                              mentor[4]))
        for student in students:
            local_class.students.append(Student(student[0], student[1],
                                                int(student[2]), student[3]))
        return local_class

    def __init__(self, location, year):
        self.location = location
        self.year = year
        self.mentors = []
        self.students = []

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            student_full_name = "%s %s" % (student.first_name, student.last_name)
            if full_name == student_full_name:
                return student

    def find_mentor_by_full_name(self, full_name):
        for mentor in self.mentors:
            mentor_full_name = "%s %s" % (mentor.first_name, mentor.last_name)
            if full_name == mentor_full_name:
                return mentor

    def feedback(self, students):
        for student in students:
            student.motivation_level += 10
            student.energy_level += 10
            student.happy = True

        for mentor in self.mentors:
            mentor.motivation_level += 10
            mentor.happy = True

        return students
