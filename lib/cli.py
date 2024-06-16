from helpers import (
    exit_program,
    add_student,
    update_student,
    find_student_by_id,
    get_all_students,
    get_student_course,
    get_student_mentor,
    delete_student,
    add_mentor,
    update_mentor,
    find_mentor_by_id,
    get_all_mentors,
    get_mentor_students,
    get_mentor_courses,
    delete_mentor,
    add_course,
    update_course,
    find_course_by_id,
    get_all_courses,
    get_course_students,
    delete_course
)
from tabulate import tabulate

def main():
    # create_tables() # Uncomment if you need to set up the database
    while True:
        main_menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            students()
        elif choice == "2":
            mentors()
        elif choice == "3":
            courses()
        else:
            print("Invalid choice. Please enter a valid option.")

def main_menu():
    print("\n" + "="*40)
    print(" Welcome to the Code Boot Camp Management System ")
    print("="*40)
    print(" Kindly select an option:")
    print(" [0] Exit the program")
    print(" [1] Student Management")
    print(" [2] Mentor Management")
    print(" [3] Course Management")
    print("="*40)
    print()

def students():
    while True:
        students_menu()
        choice = input("> ").strip()
        if choice.lower() == "p":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_student()
            print("Student added successfully!")
        elif choice == "2":
            update_student()
            print("Student updated successfully!")
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            get_student_course()
        elif choice == "6":
            get_student_mentor()
        elif choice == "7":
            delete_student()
            print("Student deleted successfully!")
        else:
            print("Invalid entry. Please choose a valid option.")

def students_menu():
    print("\n" + "-"*40)
    print(" Student Management ")
    print("-"*40)
    print(" [P] Previous menu")
    print(" [0] Exit program")
    print(" [1] Add new student")
    print(" [2] Update student details")
    print(" [3] Find student by id")
    print(" [4] List all students")
    print(" [5] Find course for specific student")
    print(" [6] Find mentor for specific student")
    print(" [7] Delete a student")
    print("-"*40)
    print()

def display_all_students():
    students = get_all_students()  # Assuming this returns a list of dictionaries
    if not students:
        print("No students found.")
    else:
        headers = ["ID", "Name", "Email", "Course", "Mentor"]
        table_data = [[student["id"], student["name"], student["email"], student["course"], student["mentor"]] for student in students]
        print("\n" + "-"*60)
        print(" All Students ")
        print("-"*60)
        print(tabulate(table_data, headers, tablefmt="grid"))
        print("-"*60)
        print()

def mentors():
    while True:
        mentors_menu()
        choice = input("> ").strip()
        if choice.lower() == "p":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_mentor()
            print("Mentor added successfully!")
        elif choice == "2":
            update_mentor()
            print("Mentor updated successfully!")
        elif choice == "3":
            find_mentor_by_id()
        elif choice == "4":
            display_all_mentors()
        elif choice == "5":
            get_mentor_students()
        elif choice == "6":
            get_mentor_courses()
        elif choice == "7":
            delete_mentor()
            print("Mentor deleted successfully!")
        else:
            print("Invalid entry. Please choose a valid option.")

def mentors_menu():
    print("\n" + "-"*40)
    print(" Mentor Management ")
    print("-"*40)
    print(" [P] Previous menu")
    print(" [0] Exit program")
    print(" [1] Add new mentor")
    print(" [2] Update mentor details")
    print(" [3] Find mentor by id")
    print(" [4] List all mentors")
    print(" [5] List students for specific mentor")
    print(" [6] List courses for specific mentor")
    print(" [7] Delete a mentor")
    print("-"*40)
    print()

def display_all_mentors():
    mentors = get_all_mentors()  # Assuming this returns a list of dictionaries
    if not mentors:
        print("No mentors found.")
    else:
        headers = ["ID", "Name", "Email", "Course"]
        table_data = [[mentor["id"], mentor["name"], mentor["email"], mentor["course"]] for mentor in mentors]
        print("\n" + "-"*60)
        print(" All Mentors ")
        print("-"*60)
        print(tabulate(table_data, headers, tablefmt="grid"))
        print("-"*60)
        print()

def courses():
    while True:
        courses_menu()
        choice = input("> ").strip()
        if choice.lower() == "p":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_course()
            print("Course added successfully!")
        elif choice == "2":
            update_course()
            print("Course updated successfully!")
        elif choice == "3":
            find_course_by_id()
        elif choice == "4":
            display_all_courses()
        elif choice == "5":
            get_course_students()
        elif choice == "6":
            delete_course()
            print("Course deleted successfully!")
        else:
            print("Invalid entry. Please choose a valid option.")

def courses_menu():
    print("\n" + "-"*40)
    print(" Course Management ")
    print("-"*40)
    print(" [P] Previous menu")
    print(" [0] Exit program")
    print(" [1] Add new course")
    print(" [2] Update course details")
    print(" [3] Find course by id")
    print(" [4] List all courses")
    print(" [5] List students for specific course")
    print(" [6] Delete a course")
    print("-"*40)
    print()

def display_all_courses():
    courses = get_all_courses()  # Assuming this returns a list of dictionaries
    if not courses:
        print("No courses found.")
    else:
        headers = ["ID", "Name", "Description", "Mentor"]
        table_data = [[course["id"], course["name"], course["description"], course["mentor"]] for course in courses]
        print("\n" + "-"*60)
        print(" All Courses ")
        print("-"*60)
        print(tabulate(table_data, headers, tablefmt="grid"))
        print("-"*60)
        print()

if __name__ == "__main__":
    main()
