from flask import Flask, render_template, redirect, url_for, request, flash
from flask_migrate import Migrate
from config import Config
from models import db, Student, Course, Section, GradeReport, Prerequisite

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/students/<int:student_number>")
def student_grades(student_number):
    student = Student.query.filter_by(student_number=student_number).first_or_404()
    grades = (
        db.session.query(
            Course.course_name,
            Course.course_number,
            Section.section_identifier,
            Section.instructor,
            Course.credit_hours,
            Section.semester,
            Section.year,
            GradeReport.grade,
        )
        .join(Section, GradeReport.section_identifier == Section.section_identifier)
        .join(Course, Section.course_number == Course.course_number)
        .filter(GradeReport.student_number == student_number)
        .all()
    )

    return render_template("student_grades.html", student=student, grades=grades)


@app.route("/students/all")
def students_all():
    students = Student.query.all()
    return render_template("students_all.html", students=students)


@app.route("/students/<int:student_number>/info")
def student_info(student_number):
    student = Student.query.filter_by(student_number=student_number).first_or_404()
    grades = (
        db.session.query(GradeReport, Section, Course)
        .join(Section, GradeReport.section_identifier == Section.section_identifier)
        .join(Course, Section.course_number == Course.course_number)
        .filter(GradeReport.student_number == student.student_number)
        .all()
    )
    return render_template("student_info.html", student=student, grades=grades)


@app.route("/instructors/<string:instructor>")
def instructor(instructor):
    sections = Section.query.filter_by(instructor=instructor).all()
    return render_template("instructor.html", instructor=instructor, sections=sections)


@app.route("/sections")
def all_sections():
    sections = Section.query.all()  # Get all sections
    return render_template("all_sections.html", sections=sections)


@app.route("/courses/<string:course_number>")
def course_info(course_number):
    course = Course.query.filter_by(course_number=course_number).first_or_404()
    prerequisites = Prerequisite.query.filter_by(course_number=course_number).all()
    return render_template("course.html", course=course, prerequisites=prerequisites)


@app.route("/courses/all")
def courses_all():
    courses = Course.query.all()
    return render_template("courses_all.html", courses=courses)


@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        student_number = request.form["student_number"]
        student_class = request.form["class"]
        major = request.form["major"]
        student = Student(
            name=name,
            student_number=student_number,
            student_class=student_class,
            major=major,
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully!")
        return redirect(url_for("students_all"))
    return render_template("add_student.html")


@app.route("/courses/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course_name = request.form["course_name"]
        course_number = request.form["course_number"]
        credit_hours = request.form["credit_hours"]
        department = request.form["department"]
        course = Course(
            course_name=course_name,
            course_number=course_number,
            credit_hours=credit_hours,
            department=department,
        )
        db.session.add(course)
        db.session.commit()
        flash("Course added successfully!")
        return redirect(url_for("courses_all"))
    return render_template("add_course.html")


@app.route("/prerequisites/add", methods=["GET", "POST"])
def add_prerequisite():
    # Fetch all existing courses to populate the dropdown
    courses = Course.query.all()

    if request.method == "POST":
        course_number = request.form["course_number"]
        prerequisite_number = request.form["prerequisite_number"]

        prerequisite = Prerequisite(
            course_number=course_number,
            prerequisite_number=prerequisite_number,
        )
        db.session.add(prerequisite)
        db.session.commit()

        flash("Prerequisite added successfully!")
        return redirect(url_for("courses_all"))  # Redirect to a relevant page

    return render_template(
        "add_prerequisite.html", courses=courses
    )  # Pass courses to the template


if __name__ == "__main__":
    app.run(debug=True)
