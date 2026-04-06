# importing required packages
from apps import db
from datetime import datetime


class ScrappedDataCourses(db.Model):

    record_id = db.Column(db.Integer, primary_key=True)
    course_categories = db.Column(db.String(30), nullable=False)
    course_sub_categories = db.Column(db.String(200), nullable=False)
    tech_neuron_course_count = db.Column(db.Integer, nullable=False)
    kids_neuron_course_count = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class ScrappedDataCourse(db.Model):

    record_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(30), nullable=False)
    course_features = db.Column(db.String(200), nullable=False)
    course_fee = db.Column(db.Integer, nullable=False)
    similar_content = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)