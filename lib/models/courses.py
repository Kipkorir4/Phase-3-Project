# models/courses.py

import sqlite3

conn = sqlite3.connect('./lib/database/bootcamp.db')
cursor = conn.cursor()

class Course:
    @staticmethod
    def get_all_courses():
        cursor.execute('SELECT * FROM courses')
        return cursor.fetchall()
    
    courses_db = []
    id_counter = 1

    def __init__(self, course_id, name, duration):
        self.course_id = course_id
        self.name = name
        self.duration = duration

    @classmethod
    def create(cls, name, duration):
        course_id = cls.id_counter
        cls.id_counter += 1
        course = cls(course_id, name, duration)
        cls.courses_db.append(course)
        return course

    @classmethod
    def find_by_id(cls, course_id):
        for course in cls.courses_db:
            if course.course_id == course_id:
                return course
        return None

    @classmethod
    def get_all_courses(cls):
        return cls.courses_db

    def update(self, field, value):
        setattr(self, field, value)

    def delete(self):
        Course.courses_db = [course for course in Course.courses_db if course.course_id != self.course_id]

    def get_students(self):
        from models.students import Student
        return [student for student in Student.students_db if student.course_id == self.course_id]

    def __str__(self):
        return f"Course(id={self.course_id}, name={self.name}, duration={self.duration} weeks)"
