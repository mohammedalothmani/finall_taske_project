# Name : mohammed alothmani
# Delivery Date : 21/06/2023

import uuid

class Course:

    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0
    student_list = []

    def __init__(self,student_name,student_age,student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1
        Student.student_list.append(self)


    def enroll_new_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f'cours name : {course.course_name}')
            print(f'cours name : {course.course_mark}')
            print()
            print()

    def get_student_average(self):
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        if len(self.courses_list) > 0:
            average = total_marks / len(self.courses_list)
            return average
        else:
            return 0
student_list = []








