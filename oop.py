class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        marks = [0,1,2,3,4,5,6,7,8,9,10]
        if isinstance(lecturer, Lecturer) and grade in marks:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'        
        
    def __str__(self,student):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_stud(student)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
    def __lt__(self, other):
        if aver_stud(self) >= aver_stud(other):
            return
        return aver_stud(self) < aver_stud(other)
    
def aver_lect(lecturer):
    count = 0
    countlen = 0
    for value in lecturer.grades.values():
        countlen +=len(value)
        for item in value:
            count += item
    return round(count/countlen, 2)
    
def aver_stud(student):
    count = 0
    countlen = 0
    for value in student.grades.values():
        countlen +=len(value)
        for item in value:
            count += item
    return round(count/countlen, 2)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {} 
    def __str__(self,lecturer):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_lect(lecturer)}")
    def __lt__(self, other):
        if aver_lect(self) >= aver_lect(other):
            return
        return aver_lect(self) < aver_lect(other)
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return print(f"Имя:{self.name}\nФамилия:{self.surname}")    
        
