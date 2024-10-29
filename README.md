# **School Management System**

This project is a simple web-based school management system developed as a Flask application. It allows users to view
and manage information about students, courses, instructors, and grades, following a relational database schema. 
The application follows RESTful design practices and is styled with Bootstrap for a clean, responsive UI.

This project is designed for a somple class mid-term assignment for Database Systems.


**Table of Contents**

* [Project Structure](#project-structure)
* [Setup and Installation](#setup-and-installation)
* [Database Schema](#database-schema)
* [API Endpoints](#api-endpoints)
* [Usage](#usage)
* [Technologies Used](#technologies-used)


### **Project Structure**

```bash
project/
│
├── app.py               # Main application with routes and views
├── config.py            # Configuration settings (database URI, etc.)
├── models.py            # SQLAlchemy models
├── migrations/          # Flask-Migrate migrations folder
│   └── versions/        # Migration scripts
└── templates/           # HTML templates with Bootstrap styling
    ├── base.html        # Base template with Bootstrap
    ├── student_grades.html # Template for showing a student's grades
    ├── instructor.html  # Template for the instructor page
    ├── course.html      # Template for showing course and prerequisites
    ├── students_all.html# Template for listing all students
    ├── student_info.html # Template for individual student info
    ├── courses_all.html # Template for listing all courses
    └── index.html       # Home page
```

### **Setup and Installation**

Prerequisites

* Python 3.x
* MySQL (or any other relational database if configured)
* virtualenv (recommended for dependency management)

Install Dependencies

1. Clone the repository:


`git clone https://github.com/juniorfelix998/database-systems-mid-term.git`

`cd school-management-system`

2. Set up a virtual environment:

`python3 -m venv venv`

`source venv/bin/activate `

3. Install required packages:

`pip install -r requirements.txt`

4. Set up the database. Configure MySQL as the backend in config.py:

`SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/school_db'`

5. Initialize the database and run migrations:

```bash
flask db init
flask db migrate
flask db upgrade
```

#### **Run the Application**

1. Start the Flask server:

`flask run`

2. Open your browser and navigate to http://127.0.0.1:5000/ to access the application.



### Database Schema

The database includes the following tables:

1. Student - Stores information about students, such as their name, student number, class, and major.
2. Course - Contains details of courses, including course name, number, credit hours, and department.
3. Section - Holds information about specific sections of each course, along with the instructor and semester.
4. Grade Report - Records grades for students in different course sections.
5. Prerequisite - Lists course prerequisites for each course.


### API Endpoints

1. Student Grades View

Description: Displays a student’s grades, including course details.

    URL: /students/<student_number>
    Method: GET

2. Instructor View

Description: Displays all sections taught by a specific instructor.

    URL: /instructors/<instructor>
    Method: GET

3. Course Information

Description: Shows course details, including prerequisites.

    URL: /courses/<course_number>
    Method: GET

4. All Students

Description: Lists all students.

    URL: /students/all
    Method: GET

5. Individual Student Information

Description: Displays information for a single student.

    URL: /students/<student_number>/info
    Method: GET

6. All Courses

Description: Lists all courses with prerequisites.

    URL: /courses/all
    Method: GET

### Usage

1. Viewing All Students: Go to /students/all to view a list of all students. Click on a student’s name to see their individual information.
2. Viewing Grades: Access /students/<student_number> to view a specific student's grades in each course.
3. Instructor Details: From the All sections view, click on an instructor’s name to see all sections taught by that instructor.
4. Course Information: In the student grades view, click on a course number to view course information, including prerequisites.
5. Viewing All Courses: Go to /courses/all to view all courses and their prerequisites.

### Technologies Used

* Flask - Web framework
* SQLAlchemy - ORM for managing the database
* Flask-Migrate - Handles database migrations
* MySQL - Database backend
* Bootstrap - Front-end framework for styling

### License

This project is licensed under the MIT License.

### Notes

* Debugging: To enable debug mode, set app.config['DEBUG'] = True in app.py.
* Database Configuration: You can switch to another database (e.g., SQLite) by modifying the SQLALCHEMY_DATABASE_URI in config.py.
* Adding Sample Data: To test with sample data, you can populate the database manually or write a seeder script.