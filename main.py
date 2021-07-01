class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_gr = 0

    def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Ошибка!!')

    def __str__(self):
        res = 'Статус: Student\n'\
              f'Имя:{self.name}\n'\
              f'Фамилия:{self.surname}\n'\
              f'Средняя оценка за домашние задания:{self.mean_gr}\n'\
              f'Курсы в процессе изучения:{str(self.courses_in_progress).strip("[]")} \n'\
              f'Завершенные курсы:{str(self.finished_courses).strip("[]")} \n'
        return res

    def mean_grade(self):
        sum_grade = 0
        sum_len = 0
        for course in self.grades.keys():
            sum_grade += sum(self.grades[course])
            sum_len += len(self.grades[course])
        self.mean_gr += sum_grade/sum_len
        return self.mean_gr

    def __le__(self, other):
        if isinstance(self, Student) and isinstance(other, Lecturer):
            return self.mean_gr <= other.mean_gr
        else:
            print('Ошибка!')

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Lecturer):
            return self.mean_gr < other.mean_gr
        else:
            print('Ошибка!')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
               student.grades[course] += [grade]
            else:
               student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        res = 'Статус: Rewiewer\n'\
              f'Имя:{self.name}\n'\
              f'Фамилия:{self.surname}\n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.mean_gr = 0

    def __str__(self):
        res = 'Статус: Lecturer\n'\
              f'Имя:{self.name}\n'\
              f'Фамилия:{self.surname}\n'\
              f'Средняя оценка за лекции:{self.mean_gr}\n'
        return res

    def mean_grade(self):
        Student.mean_grade(self)

    def __le__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Student):
            return self.mean_gr <= other.mean_gr
        else:
            print('Ошибка!')

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Student):
            return self.mean_gr < other.mean_gr
        else:
            print('Ошибка!')

    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Student):
            return self.mean_gr == other.mean_gr
        else:
            print('Ошибка!')


def stud_mid_grade_course(list_stud, course):
    middle_grade_course = 0
    middle_grade_all = 0
    new_list_stud = []
    for student in list_stud:
        if course in student.grades:
            new_list_stud += [student]
            middle_grade_course += sum(student.grades[course])/len(student.grades[course])
        else:
            continue
    middle_grade_all = middle_grade_course / len(new_list_stud)
    return f'Средняя оценка всех студентов по курсу {course}', middle_grade_all


def lec_mid_grade_course(list_lec, course):
    middle_grade_course = 0
    middle_grade_all = 0
    new_list_lec = []
    for lec in list_lec:
        if course in lec.grades:
            new_list_lec += [lec]
            middle_grade_course += sum(lec.grades[course])/len(lec.grades[course])
        else:
            continue
    middle_grade_all = middle_grade_course / len(new_list_lec)
    return f'Средняя оценка всех лекторов по курсу {course}', middle_grade_all



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

student = Student('Kseny', 'Pypirkina', 'women')
student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ['JavaScript']

lecturer = Lecturer('Tema', 'Surnov')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['Java']

best_lecture = Lecturer('Artem', 'Wenysh')
best_lecture.courses_attached += ['Java']

rewiewer = Reviewer('Uriy', 'Egoshin')
rewiewer.courses_attached += ['Python', 'Git', 'Java']
rewiewer.rate_student(best_student, 'Python', 9)
rewiewer.rate_student(best_student, 'Python', 9)
rewiewer.rate_student(best_student, 'Git', 10)
rewiewer.rate_student(best_student, 'Git', 9)
rewiewer.rate_student(student, 'Java', 9)
rewiewer.rate_student(student, 'Java', 9)
rewiewer.rate_student(student, 'Python', 9)
rewiewer.rate_student(student, 'Python', 9)



best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)

student.rate_lecturer(lecturer, 'Java', 9)
student.rate_lecturer(lecturer, 'Java', 9)

bad_student = Student('Katy', 'Pushkova', 'women')
bad_student.courses_in_progress += ['Python', 'Java']
bad_student.rate_lecturer(best_lecture, 'Java', 8)
bad_student.rate_lecturer(best_lecture, 'Java', 8)
bad_student.rate_lecturer(best_lecture, 'Java', 8)

rewiewer.rate_student(bad_student, 'Python', 9)
rewiewer.rate_student(bad_student, 'Python', 9)

lecturer.mean_grade()
student.mean_grade()
best_student.mean_grade()
best_lecture.mean_grade()
bad_student.mean_grade()

print(student)
print(lecturer)
print(best_student)
print(rewiewer)
print(best_lecture)

print(stud_mid_grade_course([best_student, student, bad_student], 'Python'))
print(stud_mid_grade_course([lecturer], 'Java'))
print(lec_mid_grade_course([lecturer, best_lecture], 'Java'))

