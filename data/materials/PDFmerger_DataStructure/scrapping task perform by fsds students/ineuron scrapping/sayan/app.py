from flask import Flask, render_template, url_for, redirect, flash
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler
from ScheduledScrapper.ScheduledScrapping import autoScrapper
from dbOperation.mongodb import  mongodbOperation
from application_logging.logger import app_log

dbName='iNeuron_scrapper'
collectionName='iNeuron_courses'
dbOps = mongodbOperation(username='ineuron_scrapper', password='iNeuron') #DB operation initialization
lg=app_log(username='ineuron_scrapper', password='iNeuron') #logging initialization

autoScrap=autoScrapper() #initialization of auto scrapping
scheduler=BackgroundScheduler()
scheduler.add_job(func=autoScrap.autoScrapping, trigger='date') #Runs the scheduler one time
scheduler.start()

app=Flask(__name__)
app.secret_key = "any random string"
CORS(app)



@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
@cross_origin()
def result():
    try:
        if dbOps.isCollectionPresent(dbName=dbName, collectionName=collectionName):
            all_course_info=dbOps.getData(dbName=dbName, collectionName=collectionName)
            lg.log(tag='INFO', message='Received all course info from database  successfully!! and returned result page')
            return render_template('result.html', results=all_course_info)
        else:
            flash(message='Getting Results....Please check after few minutes', category='primary')
            return redirect(url_for('index'))
    except Exception as e:
        lg.log(tag='ERROR', message=f"Something went wrong to get result page: {e}")
        flash(message='Something went wrong', category='danger')
        return redirect(url_for('index'))


if __name__=="__main__":
    app.run()