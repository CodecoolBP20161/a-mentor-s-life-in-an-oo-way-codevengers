# import copy
import random
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

print('Every mentor arrived to CodeCool BP this morning:')
for mentor in codecool_bp.mentors:
    print(mentor.first_name, '(%s)' % mentor.nickname)

print('The following students arrived to CodeCool BP this morning:')
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
default_energy = []
for student in students_in_school:
    default_energy.append(student.energy_level)

students_in_school = Student.learn(students_in_school)
for i, student in enumerate(students_in_school):
    if student.studied:
        print('The knowledge of %s increased by %d due teamwork exercises.'
              % (student.first_name, student.knowledge_level - default_knowledge[i]))
        print('The energy level of %s decreased by %d due the hard work.\n'
              % (student.first_name, default_energy[i] - student.energy_level))
    else:
        print("%s didn't learn enough, therefore their knowledge level and energy didn't change.\n"
              % (student.first_name))

input()

mentored_student_index = random.randint(0, len(students_in_school)-1)
mentored_student = students_in_school[mentored_student_index]
default_motivation = mentored_student.motivation_level
mentored_student = codecool_bp.mentors[random.randint(0, 2)].mentoring(mentored_student)
print('The motivation of %s increased by %d due the help of a mentor and (s)he is happy now.'
      % (mentored_student.first_name, mentored_student.motivation_level - default_motivation))
students_in_school[mentored_student_index] = mentored_student

input()

lunch = Leisure('lunch', '12:00', 'Pizzica', 1, [codecool_bp.mentors, students_in_school])
print('At %s the class goes to %s to have a %s.' % (lunch.time, lunch.place, lunch.name))
for attendant in lunch.attendants:
    Leisure.do_event(attendant)
for attendant in lunch.attendants:
    for person in attendant:
        print('During lunch, the motivation level of %s changed to %d and their energy level changed to %d.'
              % (person.first_name, person.motivation_level, person.energy_level))
print('And everybody is happy now :)')

input()

print('After lunch the students continue the teamwork with the help of %s.'
      % (codecool_bp.mentors[0].first_name))

input()

print('%s does private mentoring and %s interviews the new applicants.'
      % (codecool_bp.mentors[1].first_name, codecool_bp.mentors[2].first_name))

input()


private_mentoring = PrivateMentoring(students_in_school[3], codecool_bp.mentors[1], 'private mentoring', '13:00', 'Codecool Office', 0.5)
print("%s helps %s in a private mentoring session.\n%s's motivation increases\
 to %s, their knowledge increases to %s and their energy slightly decreases\
 to %s." % (private_mentoring.mentor.first_name, private_mentoring.students.first_name,
      private_mentoring.students.first_name, private_mentoring.students.motivation_level,
      private_mentoring.students.knowledge_level, private_mentoring.students.energy_level))
print("%s's energy level slightly decreases to %s but he feels the success, so \
his motivation increases to %d and his happiness is %s."
      % (private_mentoring.mentor.first_name, private_mentoring.mentor.energy_level,
      private_mentoring.mentor.motivation_level, private_mentoring.mentor.happy))

input()

candidate = Candidate('4ildu', 'Bela', 'Toth', 1991, 'Male')
candidate = Mentor.interview(candidate, codecool_bp.mentors)
if candidate.accepted:
    print("%s's (%s) interview was successful! Their motivation level increased, what is %s now."
          % (candidate.first_name, candidate.application_code, candidate.motivation_level))
else:
    print("%s's (%s) interview was unsuccessful! :(" % (candidate.first_name, candidate.application_code))
input()

print('Feedback session time!')
students_in_school = codecool_bp.feedback(students_in_school)
for i, student in enumerate(students_in_school):
    print("The feedback changed %s's motivation level to %d and happiness to %s"
          % (student.first_name, student.motivation_level, student.happy))
for i, mentor in enumerate(codecool_bp.mentors):
    print("The feedback changed %s (%s)'s motivation level to %d and happiness to %s"
          % (mentor.first_name, mentor.nickname, mentor.motivation_level, mentor.happy))

input()
yoga_students = [codecool_bp.find_student_by_full_name('Dávid Fehér'),
                 codecool_bp.find_student_by_full_name('Péter Pomsár')]
for student in yoga_students:
    if not student.in_school:
        student.in_school = True
        student.happy = True
        student.motivation_level = random.randint(1, 100)
        student.knowledge_level = random.randint(1, 100)
        student.studied = bool(random.randint(0, 1))
        student.energy_level = random.randint(1, 100)
yoga = Leisure('yoga', '15:30', 'Codecool Office', 1, [[codecool_bp.find_mentor_by_full_name('Tamás Tompa')], yoga_students])
print('At %s some people of the class have %s at the %s.' % (yoga.time, yoga.name, yoga.place))
for attendant in yoga.attendants:
    attendants = Leisure.do_event(attendant)
for attendant in yoga.attendants:
    for person in attendant:
        print('During yoga, the motivation level of %s changed to %d and his energy level changed to %d.'
              % (person.first_name, person.motivation_level, person.energy_level))
print('And everybody is happy now :)')

input()

print('At the end of the day everybody goes home.')
for student in students_in_school:
    student.in_school = False
    print("%s in school: %s" % (student.first_name, student.in_school))
for mentor in codecool_bp.mentors:
    mentor.in_school = False
    print("%s in school: %s" % (mentor.first_name, mentor.in_school))
