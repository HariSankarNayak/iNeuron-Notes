from os import getenv
from dotenv import load_dotenv
from scrapper import scrap_all, scrap_one
from model import connection
from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from logger import logger

load_dotenv()
MONGO_URI = getenv("MONGO_URI")
# MONGO_URI = "mongodb://localhost/"
INEURON_URL = "https://courses.ineuron.ai/"

course_collection = connection(MONGO_URI)


app = Flask(__name__)

CORS(app)


@app.get("/")
def home():
    course_count = course_collection.count_documents({})
    course_names = list(course_collection.find({}, {"_id": 0, "Title": 1}))
    return render_template("home.html", count=course_count, course_names=course_names)


@app.post("/")
def delete_course():
    course_collection.delete_many({})
    logger.debug("Collection deleted.")
    course_count = course_collection.count_documents({})
    course_names = list(course_collection.find({}, {"_id": 0, "Title": 1}))
    return render_template("home.html", count=course_count, course_names=course_names)


@app.get("/scrap-all")
def scrapping_all():
    logger.debug("Scrapping all courses.")
    scrap_all(INEURON_URL, course_collection)
    return render_template("notify.html")


@app.post("/scrap-one")
def scrapping_one():
    full_url = request.form.get("site")
    logger.debug(f"Scrapping {full_url}.")
    scrap_one(full_url, course_collection)
    return redirect(f"/course/{full_url.split('/')[-1].replace('-', ' ')}")


@app.post("/course")
def post_course():
    course_name = request.form.get("course")
    return redirect(f"/course/{course_name}")


@app.get("/course/<string:course_name>")
def get_course(course_name):
    course_data = course_collection.find_one({"Title": course_name}, {"_id": 0})
    return render_template("course.html", course_data=course_data)


@app.get("/scrapper")
def scrapper_page():
    return render_template("scrapper.html")


if __name__ == "__main__":
    logger.debug("Started App")
    app.run(debug=True)

