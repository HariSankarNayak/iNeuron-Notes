# doing necessary imports

from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo
import json
import scrap_data
import logging

logging.basicConfig(filename='logs/app1.log',level=logging.INFO,format = '%(name)s - %(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('alllogs.log')
# file_handler.setFormatter(formatter)

console_log = logging.StreamHandler()
console_log.setLevel(logging.INFO)
format = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
console_log.setFormatter(format)

logging.getLogger('').addHandler(console_log)



app = Flask(__name__)  # initialising the flask app with the name 'app'
CORS(app)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")




@app.route('/scrap',methods=['POST','GET']) # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        random_input = request.form['content'].replace(" ","") # obtaining the search string entered in the form

        try:
            try:
                logging.info('Connecting to DB')
                dbConn = pymongo.MongoClient("mongodb+srv://akarsh:akarsh@cluster0.9as2r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  # opening a connection to Mongo
                logging.info('DB connection is successful')
            except:
                logging.info('Failed to connect to Database')

            db = dbConn['ineuronDB'] # connecting to the database called crawlerDB
            db_data = db['ineuron_data_coll'].find({}) # searching the collection with the name same as the keyword
            if db['ineuron_data_coll'].count_documents({}) > 0: # if there is a collection with INEURON keyword and it has records in it
                logging.info('Data is already present in the database. So pulling data from DB')
                return render_template('results.html',ineuron_data=db_data) # show the results to user
            else:
                search_url1 = "https://courses.ineuron.ai/"

                table = db['ineuron_data_coll']

                try:
                    course_list1 = scrap_data.get_course_list(search_url1)
                    course_url_list = scrap_data.get_course_urls(course_list1)
                    course_data_list = scrap_data.get_course_details(course_url_list)
                    course_data_final_list = scrap_data.scrap_course_data(course_data_list)
                except Exception as e:
                    logging.info('Failed in parsing operation')
                    logging.error(e)




                table.insert_many(course_data_final_list)
                logging.info('Succesfully inserted the data into DB')
                return render_template('results.html', ineuron_data=course_data_final_list)
        except:
            return 'something is wrong'
            #return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000,debug=True) # running the app on the local machine on port 8000