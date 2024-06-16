# models/students.py
import sqlite3

conn = sqlite3.connect('./lib/database/bootcamp.db')
cursor = conn.cursor()

class Student:
    @staticmethod
    def get_all_students():
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()
    
    students_db = []
    id_counter = 1

    def __init__(self, student_id, name, date_of_birth, gender, email_address, course_id, mentor_id):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email_address = email_address
        self.course_id = course_id
        self.mentor_id = mentor_id

    @classmethod
    def create(cls, name, date_of_birth, gender, email_address, course_id, mentor_id):
        student_id = cls.id_counter
        cls.id_counter += 1
        student = cls(student_id, name, date_of_birth, gender, email_address, course_id, mentor_id)
        cls.students_db.append(student)
        return student

    @classmethod
    def find_by_id(cls, student_id):
        for student in cls.students_db:
            if student.student_id == student_id:
                return student
        return None

    @classmethod
    def get_all_students(cls):
        return cls.students_db

    def update(self, field, value):
        setattr(self, field, value)

    def delete(self):
        Student.students_db = [student for student in Student.students_db if student.student_id != self.student_id]

    def get_course(self):
        from models.courses import Course
        return Course.find_by_id(self.course_id)

    def get_mentor(self):
        from models.mentors import Mentor
        return Mentor.find_by_id(self.mentor_id)

    def __str__(self):
        return f"Student(id={self.student_id}, name={self.name}, date_of_birth={self.date_of_birth}, " \
               f"gender={self.gender}, email_address={self.email_address}, course_id={self.course_id}, " \
               f"mentor_id={self.mentor_id})"
