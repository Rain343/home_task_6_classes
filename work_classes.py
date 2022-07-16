from statistics import mean 

class MyTools:
    def str_dict_unpack(dict_):
        if isinstance(dict_, dict):
            return ', '.join( ': '.join((k, str(mean(v)))) for (k, v) in dict_.items())
        else:
            return 'Ошибка'

    def mean_dict_unpack(dict_):
        if isinstance(dict_, dict):
            mean_int = mean(mean(v) for v in dict_.values())
            return mean_int
        else:
            return 'Ошибка'

    def mean_dict_course(course, dict_):
        if isinstance(dict_, dict):
            if course in dict_:
                mean_course = mean(dict_[course])
                return mean_course
            else:
                return 'У этого человека нет данного курса'
        else:
            return 'Ошибка'
            

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mean_grades(course, list_students):
        mean_grade = []
        for student in list_students:
            if isinstance(student, Student) and course in student.grades:
                mean_grade.append(MyTools.mean_dict_course(course, student.grades))
            else:
                return 'Ошибка в курсе или в классе Student'
        return f'Средний балл по курсу {course} у студентов: {mean(mean_grade)}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n' 
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {MyTools.str_dict_unpack(self.grades)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
    
    def __eq__(self, object):
        if isinstance(object, Lecturer):
            return MyTools.mean_dict_unpack(self.grades) == MyTools.mean_dict_unpack(object.grades)
        else: 
            return'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean_grades(course, list_lecturers):
        mean_grade = []
        for lecturer in list_lecturers:
            if isinstance(lecturer, Lecturer) and course in lecturer.grades:
                mean_grade.append(MyTools.mean_dict_course(course, lecturer.grades))
            else:
                return 'Ошибка в курсе или в классе Lecturer'
        return f'Средний балл по курсу {course} у лекторов: {mean(mean_grade)}'

    def __str__(self):
        return (f'Имя: {self.name}\n' 
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {MyTools.str_dict_unpack(self.grades)}\n')
    
    def __eq__(self, object):
        if isinstance(object, Student):
            return MyTools.mean_dict_unpack(self.grades) == MyTools.mean_dict_unpack(object.grades)
        else: 
            return'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name}\n' 
                f'Фамилия: {self.surname}\n')
 
best_student = Student('Mr.', 'Bean', 'male')
best_student.courses_in_progress += ['Python', 'css']
best_student_2 = Student('Jim', 'Kerry', 'male')
best_student_2.courses_in_progress += ['Python', 'git']
 
cool_mentor = Mentor('Bruce', 'Willis')
cool_mentor.courses_attached += ['Python']

strong_reviewer = Reviewer('Arnold', 'Schwarzenegger')
strong_reviewer.courses_attached += ['Python', 'css']

beauty_lecturer = Lecturer('Brad', 'Pitt')
beauty_lecturer.courses_attached += ['Python']
smart_lecturer = Lecturer('Robert', 'De Niro')
smart_lecturer.courses_attached += ['Python']
 
strong_reviewer.rate_hw(best_student, 'Python', 10)
strong_reviewer.rate_hw(best_student, 'css', 10)
strong_reviewer.rate_hw(best_student, 'Python', 10)
strong_reviewer.rate_hw(best_student_2, 'Python', 5)
strong_reviewer.rate_hw(best_student_2, 'git', 10)
strong_reviewer.rate_hw(best_student_2, 'Python', 10)

best_student.rate_hw(beauty_lecturer, 'Python', 10)
best_student_2.rate_hw(beauty_lecturer, 'Python', 10)
best_student.rate_hw(beauty_lecturer, 'Python', 10)
best_student_2.rate_hw(smart_lecturer, 'Python', 10)
best_student.rate_hw(smart_lecturer, 'Python', 10)
best_student_2.rate_hw(smart_lecturer, 'Python', 10)

print(best_student)
print(beauty_lecturer)
print(strong_reviewer)
print(beauty_lecturer == best_student_2)
print(best_student == smart_lecturer)
print(Student.mean_grades('Python', [best_student, best_student_2]))
print(Lecturer.mean_grades('Python', [beauty_lecturer, smart_lecturer]))