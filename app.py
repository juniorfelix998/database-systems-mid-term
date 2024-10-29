from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
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


# Add routes for adding students, courses, sections, grade reports, and prerequisites
# Example for adding a student
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
        return redirect(url_for("index"))
    return render_template("add_student.html")


# Other routes for courses, sections, grade reports, and prerequisites

if __name__ == "__main__":
    app.run(debug=True)
