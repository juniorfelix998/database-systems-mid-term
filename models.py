from operator import index

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.Integer, unique=True, nullable=False, index=True)
    name = db.Column(db.String(50), nullable=False)
    student_class = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(50), nullable=False)
    grades = db.relationship("GradeReport", backref="student", lazy=True)


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_number = db.Column(db.String(10), unique=True, nullable=False,index=True)
    credit_hours = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    sections = db.relationship("Section", backref="course", lazy=True)
    prerequisites = db.relationship("Prerequisite", backref="course", lazy=True)


class Section(db.Model):
    __tablename__ = "sections"
    id = db.Column(db.Integer, primary_key=True)
    section_identifier = db.Column(db.Integer, unique=True, nullable=False,index=True)
    course_number = db.Column(
        db.String(10), db.ForeignKey("courses.course_number"), nullable=False
    )
    semester = db.Column(db.String(10), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    instructor = db.Column(db.String(50), nullable=False)
    grades = db.relationship("GradeReport", backref="section", lazy=True)


class GradeReport(db.Model):
    __tablename__ = "grade_reports"
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(
        db.Integer, db.ForeignKey("students.student_number"), nullable=False, index=True
    )
    section_identifier = db.Column(
        db.Integer, db.ForeignKey("sections.section_identifier"), nullable=False
    )
    grade = db.Column(db.String(2), nullable=False)


class Prerequisite(db.Model):
    __tablename__ = "prerequisites"
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(
        db.String(10), db.ForeignKey("courses.course_number"), nullable=False
    )
    prerequisite_number = db.Column(db.String(10), nullable=False)
