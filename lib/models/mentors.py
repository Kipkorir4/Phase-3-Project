# models/mentors.py
import sqlite3

conn = sqlite3.connect('./lib/database/bootcamp.db')
cursor = conn.cursor()

class Mentor:
    mentors_db = []
    id_counter = 1

    def __init__(self, mentor_id, name, gender, email_address, course_ids):
        self.mentor_id = mentor_id
        self.name = name
        self.gender = gender
        self.email_address = email_address
        self.course_ids = course_ids

    @classmethod
    def create(cls, name, gender, email_address, course_ids):
        mentor_id = cls.id_counter
        cls.id_counter += 1
        mentor = cls(mentor_id, name, gender, email_address, course_ids)
        cls.mentors_db.append(mentor)
        return mentor

    @classmethod
    def find_by_id(cls, mentor_id):
        for mentor in cls.mentors_db:
            if mentor.mentor_id == mentor_id:
                return mentor
        return None

    @classmethod
    def get_all_mentors(cls):
        return cls.mentors_db

    def update(self, field, value):
        setattr(self, field, value)

    def delete(self):
        Mentor.mentors_db = [mentor for mentor in Mentor.mentors_db if mentor.mentor_id != self.mentor_id]

    def get_students(self):
        from models.students import Student
        return [student for student in Student.students_db if student.mentor_id == self.mentor_id]

    def get_courses(self):
        from models.courses import Course
        return [Course.find_by_id(course_id) for course_id in self.course_ids]

    def __str__(self):
        return f"Mentor(id={self.mentor_id}, name={self.name}, gender={self.gender}, " \
               f"email_address={self.email_address}, course_ids={self.course_ids})"
