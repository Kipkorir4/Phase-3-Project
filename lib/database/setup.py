# database/setup.py

import sqlite3
# use DB Browser to edit te 
conn = sqlite3.connect('./bootcamp.db') 
cursor = conn.cursor()

def create_tables():
    # Create the Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT CHECK(gender IN ('M', 'F')),
            email_address TEXT NOT NULL UNIQUE,
            course_id INTEGER,
            mentor_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE SET NULL,
            FOREIGN KEY (mentor_id) REFERENCES mentors(id) ON DELETE SET NULL
        )
    ''')

    # Create the Mentors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mentors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT CHECK(gender IN ('M', 'F')),
            email_address TEXT NOT NULL UNIQUE,
            course_ids TEXT  -- Storing a comma-separated list of course IDs
        )
    ''')

    # Create the mentor_course_association table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            duration INTEGER NOT NULL  -- Duration in weeks
        )
    ''')

    # Create the Courses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mentor_course_association (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mentor_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (mentor_id) REFERENCES mentors(id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
            UNIQUE (mentor_id, course_id)
        )
    ''')

    conn.commit()
    print('mentor_course_association done and commited')

def drop_tables():
    # Drop all tables, useful for resetting the database
    cursor.execute('DROP TABLE IF EXISTS students')
    cursor.execute('DROP TABLE IF EXISTS mentors')
    cursor.execute('DROP TABLE IF EXISTS courses')
    cursor.execute('DROP TABLE IF EXISTS mentor_course_association')

    conn.commit()
