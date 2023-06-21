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

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
        if selection == 1:
            student_number = input('Enter Student Number: ')
            exists = False
            for student in student_list:
                if student.student_number == student_number:
                    exists = True
                    break
            if exists:
                print('the student number exists')
            else:
                student_name = input('Enter Student Name')
                while True:
                    try:
                        student_age = int(input("Enter Student Age"))
                        break
                    except:
                        print('Invalid Value')

                new_student = Student(student_name,student_age,student_number)
                student_list.append(new_student)
                print("Student Added Successfully")


















