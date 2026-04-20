from setting.setting import Setting
from db_connection.mongodboperation import DbOperation
from scrapping.scrapping import Scrapping
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json
from flask_classful import FlaskView, route
from bson.json_util import dumps

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    db_operation = DbOperation(db_name="ineuron_data")
    db_operation.connect_current_collection("ineuron_collection")

    li = []
    for i in db_operation.get_all_data():

        li.append(i)

    return dumps(li)


class MyApp(Setting):

    def __init__(self):
        super(MyApp, self).__init__("main.log")
        self.db_operation = DbOperation(db_name="ineuron_data")
        self.db_operation.create_collection("ineuron_collection")
        self.db_operation.connect_current_collection("ineuron_collection")
        # only windows support with chrome install
        # Scrapping(self.db_operation)






if __name__ == "__main__":
    #a = MyApp()
    #db_operation = a.db_operation
    app.run(host='127.0.0.1', port=8000, debug=True)
