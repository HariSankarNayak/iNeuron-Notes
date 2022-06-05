
from flask import Flask,jsonify,render_template,request
from flask_cors import cross_origin,CORS
import logging as logger
from Scaper.webParser import webParser
from bson.json_util import dumps, loads
import threading
import asyncio
import multiprocessing
import time
from apscheduler.schedulers.background import BackgroundScheduler
import tzlocal

logger.basicConfig(filename='./Log/app_logs.log', level=logger.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/view-course',methods=['GET'])  # route to display the home page
@cross_origin()
def view_course():
    """use for render home template"""
    return render_template("course_detail.html")

@app.route('/fetchCoursedetails',methods=['GET'])  # route to display the home page
@cross_origin()
def fetchCoursedetails():
    """use for get fetch Course list page"""

    logger.info("getCourseDetails")
    wp1 = webParser()
    res = list(wp1.getCourse_Details())
    if len(res) > 0:
        res = res[1:]
    return jsonify(res)

@app.route('/fetchCoursedetailsWithCourseName',methods=['POST'])  # route to display the home page
@cross_origin()
def fetchCoursedetailsWithCourseName():
    """use for get fetch Course Detail page"""

    logger.info("fetchCoursedetailsWithCourseName")
    courseName = request.json['courseName']

    wp1 = webParser()
    res =  wp1.getCourse_DetailsWithCourseName(courseName)
    json_data = dumps(res)
    return json_data



#Scraper Function

@app.route('/callParser',methods=['GET'])  # route to display the home page
@cross_origin()
def callParser():
    """ initially to start web_Scrapper """
    #intially call this function.
    web_scraper()

    """ added scheduler to continue web parsing, if in case it's take time"""
    # after one minute BackgroundScheduler will take care scraping task.
    scheduler = BackgroundScheduler(timezone=str(tzlocal.get_localzone()))
    scheduler.add_job(web_scraper, 'interval', minutes=3, id="web_scraper")
    scheduler.start()

    return jsonify({"status":"1","msg":"Ok"})

def web_scraper():
    """This method for course scraping"""
    logger.info("callParser get invoked..")
    """Course Parser"""
    wp = webParser()
    wp.courseScaper()

    """Course Detail Parser"""
    res = list(wp.getCourse_Details())
    wp.courseDetailScaper(res)



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=9091, debug=True)
    app.run(debug=True)
