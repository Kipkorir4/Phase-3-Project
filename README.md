# Code Boot Camp CLI Management System


## Introduction

The Code Boot Camp Management System is a command-line interface (CLI) application designed to manage students, mentors, and courses efficiently. This application provides a user-friendly interface for administrators to add, update, delete, and list information in a well-organized format.

## Features

- Add, update, and delete students, mentors, and courses.
- List all students, mentors, and courses with enhanced formatting.
- Find specific students, mentors, or courses by their IDs.
- Display relationships between students, mentors, and courses.
- Clear, organized, and visually appealing CLI menus and outputs.

## Prerequisites

- Packages listed in the Pipfile.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kipkorir4/Phase-3-Project.git
    cd code-Phase-3-Project
    ```

2. Install the required dependencies:
    ```bash
    pipenv install
    ```

  ```

## Usage

1. Run the CLI application:
    ```bash
    python lib/cli.py
    ```

2. Follow the on-screen instructions to navigate through the menus and perform operations.

## Functionality
## Main Menu
    Upon starting the application, you will be greeted with the main menu:


========================================
 Welcome to the Code Boot Camp Management System 
========================================
 Kindly select an option:
 [0] Exit the program
 [1] Student Management
 [2] Mentor Management
 [3] Course Management
========================================
    Choose an option by typing the corresponding number and pressing Enter.

### Student Management
    Access the student management menu by selecting 1 from the main menu. You will see:


----------------------------------------
 Student Management 
----------------------------------------
 [P] Previous menu
 [0] Exit program
 [1] Add new student
 [2] Update student details
 [3] Find student by id
 [4] List all students
 [5] Find course for specific student
 [6] Find mentor for specific student
 [7] Delete a student
----------------------------------------
### Options:
    Add new student: Prompts for student details and adds them to the database.
    Update student details: Prompts for student ID and new details to update.
    Find student by id: Prompts for student ID and displays the student’s details.
    List all students: Displays all students in a formatted table.
    Find course for specific student: Prompts for student ID and shows the related course.
    Find mentor for specific student: Prompts for student ID and shows the related mentor.
    Delete a student: Prompts for student ID and deletes the student.
    Mentor Management
    Access the mentor management menu by selecting 2 from the main menu. You will see:


----------------------------------------
 ## Mentor Management 
----------------------------------------
    [P] Previous menu
    [0] Exit program
    [1] Add new mentor
    [2] Update mentor details
    [3] Find mentor by id
    [4] List all mentors
    [5] List students for specific mentor
    [6] List courses for specific mentor
    [7] Delete a mentor
----------------------------------------
### Options:
    Add new mentor: Prompts for mentor details and adds them to the database.
    Update mentor details: Prompts for mentor ID and new details to update.
    Find mentor by id: Prompts for mentor ID and displays the mentor’s details.
    List all mentors: Displays all mentors in a formatted table.
    List students for specific mentor: Prompts for mentor ID and lists their students.
    List courses for specific mentor: Prompts for mentor ID and lists their courses.
    Delete a mentor: Prompts for mentor ID and deletes the mentor.
    Course Management
    Access the course management menu by selecting 3 from the main menu. You will see:


----------------------------------------
##  Course Management 
----------------------------------------
    [P] Previous menu
    [0] Exit program
    [1] Add new course
    [2] Update course details
    [3] Find course by id
    [4] List all courses
    [5] List students for specific course
    [6] Delete a course
----------------------------------------
### Options:
    Add new course: Prompts for course details and adds them to the database.
    Update course details: Prompts for course ID and new details to update.
    Find course by id: Prompts for course ID and displays the course’s details.
    List all courses: Displays all courses in a formatted table.
    List students for specific course: Prompts for course ID and lists its students.
    Delete a course: Prompts for course ID and deletes the course.
    Formatting and Display
    The application utilizes the tabulate library to format and display the fetched results in a table format, ensuring that each row is spaced and clearly separated from the next one. This improves readability and user experience.

#### Example output for listing all students:

    
    ------------------------------------------------------------
    All Students 
    ------------------------------------------------------------
    +----+-----------------+-----------------------+-------------+-----------+
    | ID | Name            | Email                 | Course      | Mentor    |
    +----+-----------------+-----------------------+-------------+-----------+
    | 1  | Alice Johnson   | alice.j@example.com   | Python Boot | John Doe  |
    | 2  | Bob Smith       | bob.smith@example.com | JavaScript  | Jane Roe  |
    +----+-----------------+-----------------------+-------------+-----------+
    ------------------------------------------------------------
    Each row is clearly separated, and columns are aligned to provide a clear view of each student's details.

## Contributing
    If you would like to contribute to the project, please follow these steps:

### Fork the repository.
    Create a new branch for your feature or bugfix:
        git checkout -b feature/your-feature-name
    Commit your changes:
        git commit -m "Add some feature"
    Push to the branch:
        git push origin feature/your-feature-name
    Open a pull request and describe your changes.
## License
This project is licensed under the Moringa License.




