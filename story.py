# import copy
from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from event import Event
from leisure import Leisure
from person import Person
from private_mentoring import PrivateMentoring
from candidate import Candidate

codecool_bp = CodecoolClass.generate_local()
# print(codecool_bp)
# print(codecool_bp.students[0].__dict__)

codecool_bp.students, codecool_bp.mentors = Person.come_to_school(codecool_bp.students, codecool_bp.mentors)

print('Every mentor and the following students arrived to CodeCool BP this morning:')
students_in_school = []
for student in codecool_bp.students:
    if student.in_school:
        print(student.first_name)
        students_in_school.append(student)
# codecool_bp.students = copy.deepcopy(students_in_school)
input()

default_energy = []
for student in students_in_school:
    default_energy.append(student.energy_level)

students_in_school, codecool_bp.mentors = Mentor.do_morning_gym(students_in_school, codecool_bp.mentors)
for i, student in enumerate(students_in_school):
    print('The energy level of %s increased by %d due morning gym exercises.'
          % (student.first_name, student.energy_level - default_energy[i]))

input()

default_motivation = []
for student in students_in_school:
    default_motivation.append(student.motivation_level)

students_in_school = Mentor.daily_agenda(students_in_school)
for i, student in enumerate(students_in_school):
    is_studied = "because (s)he didn't learn enough on the SI week"
    if student.studied:
        is_studied = 'because (s)he learned enough on the SI week'
    print('The motivation level of %s changed by %d because %s.'
          % (student.first_name, student.motivation_level - default_motivation[i], is_studied))

input()

default_knowledge = []
for student in students_in_school:
    default_knowledge.append(student.knowledge_level)

students_in_school = Student.learn(students_in_school)
for i, student in enumerate(students_in_school):
    print('The knowledge of %s increased by %d due teamwork exercises.'
          % (student.first_name, student.knowledge_level - default_knowledge[i]))

input()
