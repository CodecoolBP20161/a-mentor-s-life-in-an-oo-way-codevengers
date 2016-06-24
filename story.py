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

codecool_bp.students, codecool_bp.mentors = Person.come_to_school(codecool_bp.students, codecool_bp.mentors)

print('\033[92m \n\nA story of an average day at Codecool Budapest.\n\033[0m')

input()

print('\033[92mThe mentors arrive first:\033[0m')
for mentor in codecool_bp.mentors:
    print('\033[93m%s\033[0m (\033[93m%s\033[0m) arrived: \033[93m%s\033[0m'
          % (mentor.first_name, mentor.nickname, mentor.in_school))

print('\033[92m\nMost of the students came to school this morning:\033[0m')
students_in_school = []
for student in codecool_bp.students:
    if student.in_school:
        print('\033[93m%s\033[0m arrived: \033[93m%s\033[0m' % (student.first_name, student.in_school))
        students_in_school.append(student)

input()

print('\033[93m%s\033[0m (\033[93m%s\033[0m) \033[92msenses low energy level \
among the students and initiates some exercises.\033[0m'
      % (codecool_bp.find_mentor_by_full_name('Miklós Beöthy').first_name,
         codecool_bp.find_mentor_by_full_name('Miklós Beöthy').nickname))
default_energy = []
for student in students_in_school:
    default_energy.append(student.energy_level)

students_in_school, codecool_bp.mentors = Mentor.do_morning_gym(students_in_school, codecool_bp.mentors)
for i, student in enumerate(students_in_school):
    print('The energy level of \033[93m%s\033[0m increased by \033[93m%d\033[0m due morning gym exercises.'
          % (student.first_name, student.energy_level - default_energy[i]))

input()

print("\033[92mWhen everybody is well energized, the mentors tell the daily agenda.\n\
If the students learned at home, they feel motivated, \n\
but if they were lazy they don't know what is going on.\033[0m")
default_motivation = []
for student in students_in_school:
    default_motivation.append(student.motivation_level)

students_in_school = Mentor.daily_agenda(students_in_school)
for i, student in enumerate(students_in_school):
    is_studied = "because (s)he didn't learn enough on the SI week"
    if student.studied:
        is_studied = 'because (s)he learned enough on the SI week'
    print('The motivation level of \033[93m%s\033[0m changed by \033[93m%d\033[0m because %s.'
          % (student.first_name, student.motivation_level - default_motivation[i], is_studied))

input()

print('\033[92mThen the students start doing teamwork.\nIf they know what to do, they are \
really involved in the exercise, otherwise not so much.\033[0m')
default_knowledge = []
for student in students_in_school:
    default_knowledge.append(student.knowledge_level)
default_energy = []
for student in students_in_school:
    default_energy.append(student.energy_level)

students_in_school = Student.learn(students_in_school)
for i, student in enumerate(students_in_school):
    if student.studied:
        print('The knowledge of \033[93m%s\033[0m increased by \033[93m%d\033[0m due teamwork exercises.'
              % (student.first_name, student.knowledge_level - default_knowledge[i]))
        print('The energy level of \033[93m%s\033[0m decreased by \033[93m%d\033[0m due the hard work.'
              % (student.first_name, default_energy[i] - student.energy_level))
    else:
        print("\033[93m%s\033[0m didn't learn enough, therefore their knowledge level and energy didn't change."
              % (student.first_name))

input()

print('\033[92mThe mentors help those who have some questions.\033[0m')
mentored_student_index = random.randint(0, len(students_in_school)-1)
mentored_student = students_in_school[mentored_student_index]
default_motivation = mentored_student.motivation_level
mentored_student = codecool_bp.mentors[random.randint(0, 2)].mentoring(mentored_student)
print('The motivation of \033[93m%s\033[0m increased by \033[93m%d\033[0m due the help of\
 \033[93m%s\033[0m and their happiness value is \033[93m%s\033[0m.'
      % (mentored_student.first_name, mentored_student.motivation_level - default_motivation,
         codecool_bp.mentors[random.randint(0, len(codecool_bp.mentors)-1)].first_name,
         mentored_student.happy))
students_in_school[mentored_student_index] = mentored_student

input()

lunch = Leisure('lunch', '12:00', 'Pizzica', 1, [codecool_bp.mentors, students_in_school])
print('\033[92mAt\033[0m \033[93m%s\033[0m \033[92mthe class goes to\033[0m \
\033[93m%s\033[0m \033[92mto have a\033[0m \033[93m%s\033[0m \033[92mand they feel really happy.\033[0m'
      % (lunch.time, lunch.place, lunch.name))
for attendant in lunch.attendants:
    Leisure.do_event(attendant)
for attendant in lunch.attendants:
    for person in attendant:
        print('During lunch, the motivation level of \033[93m%s\033[0m changed to\
 \033[93m%d\033[0m and their energy level changed to \033[93m%d\033[0m.'
              % (person.first_name, person.motivation_level, person.energy_level))

input()

print('\033[92mAfter lunch the students continue the teamwork with the help of \033[93m%s\033[0m.'
      % (codecool_bp.mentors[0].first_name))

input()

print('\033[93m%s\033[0m \033[92mdoes private mentoring and\033[0m \
\033[93m%s\033[0m \033[92minterviews the new applicants.\033[0m'
      % (codecool_bp.mentors[1].first_name, codecool_bp.mentors[2].first_name))

input()

private_mentoring = PrivateMentoring(students_in_school[3], codecool_bp.mentors[1],
                                     'private mentoring', '13:00', 'Codecool Office', 0.5)
mentored_student = None
awesome_mentor = None
mentored_student, awesome_mentor = PrivateMentoring.do_event([students_in_school[3]], codecool_bp.mentors[1])
print("\033[93m%s\033[0m helps \033[93m%s\033[0m in a private mentoring session.\
\n\033[93m%s\033[0m's motivation increases to \033[93m%s\033[0m, \
their knowledge increases to \033[93m%s\033[0m and their energy slightly decreases\
 to \033[93m%s\033[0m." % (private_mentoring.mentor.first_name, private_mentoring.students.first_name,
      private_mentoring.students.first_name, private_mentoring.students.motivation_level,
      private_mentoring.students.knowledge_level, private_mentoring.students.energy_level))
print("\033[93m%s\033[0m's energy level slightly decreases to \033[93m%s\033[0m but he feels the success, so \
his motivation increases to \033[93m%d\033[0m and his happiness is \033[93m%s\033[0m."
      % (private_mentoring.mentor.first_name, private_mentoring.mentor.energy_level,
         private_mentoring.mentor.motivation_level, private_mentoring.mentor.happy))

input()


candidate = Candidate('4ildu', 'Bela', 'Toth', 1991, 'Male')
candidate = Mentor.interview(candidate, codecool_bp.mentors)
if candidate.accepted:
    print("\033[93m%s\033[0m's (\033[93m%s\033[0m) interview was successful! \
His motivation level increased to \033[93m%s\033[0m."
          % (candidate.first_name, candidate.application_code, candidate.motivation_level))
else:
    print("\033[93m%s\033[0m's (\033[93m%s\033[0m) interview was unsuccessful! :("
          % (candidate.first_name, candidate.application_code))
input()

print('\033[92mFeedback session time!\033[0m')
students_in_school = codecool_bp.feedback(students_in_school)
for i, student in enumerate(students_in_school):
    print("The feedback changed \033[93m%s\033[0m's motivation level to\
 \033[93m%d\033[0m and happiness to \033[93m%s\033[0m"
          % (student.first_name, student.motivation_level, student.happy))
for i, mentor in enumerate(codecool_bp.mentors):
    print("The feedback changed \033[93m%s\033[0m (\033[93m%s\033[0m)'s motivation level to \
\033[93m%d\033[0m and happiness to \033[93m%s\033[0m"
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
yoga = Leisure('yoga', '15:30', 'Codecool Office', 1,
               [[codecool_bp.find_mentor_by_full_name('Tamás Tompa')], yoga_students])
print('\033[92mAt\033[0m \033[93m%s\033[0m \033[92msome people of the class have\033[0m \
\033[93m%s\033[0m at the\033[0m \033[93m%s\033[0m.' % (yoga.time, yoga.name, yoga.place))
for attendant in yoga.attendants:
    attendants = Leisure.do_event(attendant)
for attendant in yoga.attendants:
    for person in attendant:
        print('During yoga, the motivation level of \033[93m%s\033[0m changed to \
\033[93m%d\033[0m and his energy level changed to \033[93m%d\033[0m.'
              % (person.first_name, person.motivation_level, person.energy_level))
print('And everybody is happy now :)')

input()

print('\033[92mAnd at the end of the day everybody goes home.\033[0m')
for student in students_in_school:
    student.in_school = False
    print("\033[93m%s\033[0m in school: \033[93m%s\033[0m" % (student.first_name, student.in_school))
for mentor in codecool_bp.mentors:
    mentor.in_school = False
    print("\033[93m%s\033[0m in school: \033[93m%s\033[0m" % (mentor.first_name, mentor.in_school))

print('\033[92m\nThis was the story of an average day at Codecool Budapest. \n\
We hope you enjoyed our little presentation and we could \
\nset your motivation value sky high and your happiness to True! :)\033[0m')
