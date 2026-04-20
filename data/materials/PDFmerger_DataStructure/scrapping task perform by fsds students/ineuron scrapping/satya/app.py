from flask import Flask, render_template, request
from flask_cors import cross_origin
from MongoDbManagement import MongoDbUtils
from ineuron_scrapper import ineuronScrapper
from loggerMainClass import scrapLogger
import utils

app = Flask(__name__)


@cross_origin()
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@cross_origin()
@app.route('/scrap', methods=['GET', 'POST'])
def scrap():
    if request.method == 'POST':
        inputString = request.form['submit_button'].replace(" ", "")
        try:
            log = scrapLogger.ineuron_scrap_logger()
            refactor_obj = utils.utilityFunctions()
            db_obj = MongoDbUtils(refactor_obj.getUsernameforMongoDB(), refactor_obj.getPasswordforMongoDB())
            db_obj.createDatabase("Ineuron_Scrapper")
            log.info("Database created")
            if db_obj.isCollectionPresent(inputString):
                log.info("Checks if collection present in database")
                response = db_obj.getRecords(inputString)
                if response is not None:
                    course_details = [i for i in response]
                    if bool(course_details):
                        log.info("Fetching data from database")
                        return render_template("output.html", course_details=course_details, course_title=inputString)
            else:
                scrapper_obj = ineuronScrapper(inputString, refactor_obj, db_obj)
                return render_template("output.html", course_details=scrapper_obj.getCourseDetails(), course_title = inputString)
        except Exception as e:
            print("(app.py) - Something went wrong while rendering all the details of product.\n" + str(e))


if __name__ == '__main__':
    app.run(debug=True)
