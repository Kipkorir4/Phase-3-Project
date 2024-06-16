# database/add_data.py

from __init__ import conn, cursor

def add_courses():
    courses = [
        ('UI/UX Design', 8),
        ('Full-Stack Development', 16),
        ('Data Science', 14),
        ('Artificial Intelligence', 18),
        ('Machine Learning', 20),
        ('Deep Learning', 22),
        ('Computer Vision', 17),
        ('Natural Language Processing', 20),
        ('Data Analytics', 16),
        ('Data Visualization', 13)
    ]
    cursor.executemany('INSERT INTO courses (name, duration) VALUES (?, ?)', courses)
    conn.commit()
    print(f"Added {len(courses)} courses.")

def add_mentors():
    mentors = [
        ('Alice Johnson', 'F', 'alice.johnson@example.com', '1,2'),
        ('Bob Smith', 'M', 'bob.smith@example.com', '2,3'),
        ('Charlie Brown', 'M', 'charlie.brown@example.com', '1,3'),
        ('Dave Jones', 'M', 'dave.jones@example.com', '1,4'),
        ('Elizabeth Williams', 'F', 'elizabeth.williams@example.com', '2,5'),
        ('Frank Smith', 'M', 'frank.smith@example.com', '3,6'),
        ('George Williams', 'M', 'george.williams@example.com', '4,7'),
        ('Harry Brown', 'M', 'harry.brown@example.com', '5,8'),
        ('Irene Smith', 'F', 'irene.smith@example.com', '6,9')
    ]
    cursor.executemany('INSERT INTO mentors (name, gender, email_address, course_ids) VALUES (?, ?, ?, ?)', mentors)
    conn.commit()
    print(f"Added {len(mentors)} mentors.")

def add_students():
    students = [
        ('John Doe', '2000-01-15', 'M', 'john.doe@example.com', 1, 1),
        ('Jane Roe', '1999-05-20', 'F', 'jane.roe@example.com', 2, 2),
        ('Sam Smith', '2001-07-22', 'M', 'sam.smith@example.com', 3, 3),
        ('Emily Davis', '1998-11-11', 'F', 'emily.davis@example.com', 1, 1),
        ('Michael Brown', '2002-03-14', 'M', 'michael.brown@example.com', 2, 2),
        ('Jennifer Lawrence', '1997-09-01', 'F', 'jennifer.lawrence@example.com', 3, 3),
        ('Kevin Brown', '2003-05-12', 'M', 'kevin.brown@example.com', 4, 4),
        ('Lisa Bin', '2004-07-15', 'F', 'lisa.bin@example.com', 5, 5),
        ('Mary Prac', '1996-10-18', 'F', 'mary.prac@example.com', 6, 6),
        ('Natalie Jones', '1995-12-21', 'F', 'natalie.jones@example.com', 7, 7),
        ('Olivia Biss', '2005-03-24', 'F', 'olivia.biss@example.com', 8, 8),
        ('Peter Parker', '2006-05-27', 'M', 'peter.parker@example.com', 9, 9),
        ('Quinn Thor', '1994-08-30', 'F', 'quinn.thor@example.com', 1, 1),
        ('Rachel Thanos', '1993-11-02', 'F', 'rachel.thanos@example.com', 2, 2),
        ('Samantha Jay', '2007-01-05', 'F', 'Samantha.jay@example.com', 3, 3)
    ]
    cursor.executemany('INSERT INTO students (name, date_of_birth, gender, email_address, course_id, mentor_id) VALUES (?, ?, ?, ?, ?, ?)', students)
    conn.commit()
    print(f"Added {len(students)} students.")

def add_mentor_course_associations():
    associations = []
    cursor.execute('SELECT id, course_ids FROM mentors')
    mentors_data = cursor.fetchall()

    for mentor_id, course_ids_str in mentors_data:
        if course_ids_str:
            course_ids = map(int, course_ids_str.split(','))
            for course_id in course_ids:
                associations.append((mentor_id, course_id))

    cursor.executemany('INSERT OR IGNORE INTO mentor_course_association (mentor_id, course_id) VALUES (?, ?)', associations)
    conn.commit()
    print(f"Added {len(associations)} mentor-course associations.")

def main():
    create_tables()
    add_courses()
    add_mentors()
    add_students()
    add_mentor_course_associations()
    print("Data has been successfully added to the database.")

if __name__ == "__main__":
    main()

# def main():
#     add_courses()
#     add_mentors()
#     add_students()
#     print("Data has been successfully added to the database.")

# if __name__ == "__main__":
#     main()
