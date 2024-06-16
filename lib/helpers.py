# lib/helpers.py
from database.connection import get_db_connection

def exit_program():
    print("Done! Exited the program.")
    exit()

def add_student():
    student_name = input("Enter student's name: ")
    date_of_birth = input("Enter date of birth: ")
    gender = input("Enter gender, M or F: ")
    email_address = input("Enter email address: ")
    course_id = int(input("Enter course ID: "))
    mentor_id = int(input("Enter mentor ID: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (name, date_of_birth, gender, email_address, course_id, mentor_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_name, date_of_birth, gender, email_address, course_id, mentor_id))
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def update_student():
    student_id = int(input("Enter student id: "))
    field = input("Enter field to update (name, date_of_birth, gender, email_address, course_id, mentor_id): ")
    value = input(f"Enter new value for {field}: ")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE students SET {field} = ? WHERE id = ?", (value, student_id))
        conn.commit()
        print(f"Student with id {student_id} updated successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def find_student_by_id():
    student_id = int(input("Enter student id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    
    if student:
        print(dict(student))
    else:
        print(f"Student with id {student_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if students:
        print("Listing all students:")
        for student in students:
            print(dict(student))
    else:
        print("No students found.")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_student_course():
    student_id = int(input("Enter student id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT courses.* FROM students
        JOIN courses ON students.course_id = courses.id
        WHERE students.id = ?
    """, (student_id,))
    course = cursor.fetchone()
    
    if course:
        print(dict(course))
    else:
        print(f"Student with id {student_id} does not exist or is not enrolled in a course")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_student_mentor():
    student_id = int(input("Enter student id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT mentors.* FROM students
        JOIN mentors ON students.mentor_id = mentors.id
        WHERE students.id = ?
    """, (student_id,))
    mentor = cursor.fetchone()
    
    if mentor:
        print(dict(mentor))
    else:
        print(f"Student with id {student_id} does not exist or does not have a mentor")
    conn.close()
    
    input("\nPress Enter to continue...")

def delete_student():
    student_id = int(input("Enter student id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Student with id {student_id} deleted successfully.")
    else:
        print(f"Student with id {student_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

    

# Mentor functions

def add_mentor():
    mentor_name = input("Enter mentor's name: ")
    gender = input("Enter gender, M or F: ")
    email_address = input("Enter email address: ")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO mentors (name, gender, email_address)
            VALUES (?, ?, ?)
        """, (mentor_name, gender, email_address))
        conn.commit()
        print("Mentor added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def update_mentor():
    mentor_id = int(input("Enter mentor id: "))
    field = input("Enter field to update (name, gender, email_address): ")
    value = input(f"Enter new value for {field}: ")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE mentors SET {field} = ? WHERE id = ?", (value, mentor_id))
        conn.commit()
        print(f"Mentor with id {mentor_id} updated successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def find_mentor_by_id():
    mentor_id = int(input("Enter mentor id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mentors WHERE id = ?", (mentor_id,))
    mentor = cursor.fetchone()
    
    if mentor:
        print(dict(mentor))
    else:
        print(f"Mentor with id {mentor_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_all_mentors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mentors")
    mentors = cursor.fetchall()
    
    if mentors:
        print("Listing all mentors:")
        for mentor in mentors:
            print(dict(mentor))
    else:
        print("No mentors found.")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_mentor_students():
    mentor_id = int(input("Enter mentor id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.* FROM mentors
        JOIN students ON mentors.id = students.mentor_id
        WHERE mentors.id = ?
    """, (mentor_id,))
    students = cursor.fetchall()
    
    if students:
        print(f"Students mentored by mentor id {mentor_id}:")
        for student in students:
            print(dict(student))
    else:
        print(f"Mentor with id {mentor_id} does not have any students or does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_mentor_courses():
    mentor_id = int(input("Enter mentor id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT courses.* FROM mentors
        JOIN mentor_course_association ON mentors.id = mentor_course_association.mentor_id
        JOIN courses ON mentor_course_association.course_id = courses.id
        WHERE mentors.id = ?
    """, (mentor_id,))
    courses = cursor.fetchall()
    
    if courses:
        print(f"Courses taught by mentor id {mentor_id}:")
        for course in courses:
            print(dict(course))
    else:
        print(f"Mentor with id {mentor_id} does not teach any courses or does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def delete_mentor():
    mentor_id = int(input("Enter mentor id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mentors WHERE id = ?", (mentor_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Mentor with id {mentor_id} deleted successfully.")
    else:
        print(f"Mentor with id {mentor_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

# Course functions

def add_course():
    course_name = input("Enter course's name: ")
    duration = int(input("Enter duration in weeks: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO courses (name, duration)
            VALUES (?, ?)
        """, (course_name, duration))
        conn.commit()
        print("Course added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def update_course():
    course_id = int(input("Enter course id: "))
    field = input("Enter field to update (name, duration): ")
    value = input(f"Enter new value for {field}: ")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE courses SET {field} = ? WHERE id = ?", (value, course_id))
        conn.commit()
        print(f"Course with id {course_id} updated successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    
    input("\nPress Enter to continue...")

def find_course_by_id():
    course_id = int(input("Enter course id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
    course = cursor.fetchone()
    
    if course:
        print(dict(course))
    else:
        print(f"Course with id {course_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_all_courses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    
    if courses:
        print("Listing all courses:")
        for course in courses:
            print(dict(course))
    else:
        print("No courses found.")
    conn.close()
    
    input("\nPress Enter to continue...")

def get_course_students():
    course_id = int(input("Enter course id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.* FROM courses
        JOIN students ON courses.id = students.course_id
        WHERE courses.id = ?
    """, (course_id,))
    students = cursor.fetchall()
    
    if students:
        print(f"Students enrolled in course id {course_id}:")
        for student in students:
            print(dict(student))
    else:
        print(f"Course with id {course_id} does not have any students or does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")

def delete_course():
    course_id = int(input("Enter course id: "))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Course with id {course_id} deleted successfully.")
    else:
        print(f"Course with id {course_id} does not exist")
    conn.close()
    
    input("\nPress Enter to continue...")
