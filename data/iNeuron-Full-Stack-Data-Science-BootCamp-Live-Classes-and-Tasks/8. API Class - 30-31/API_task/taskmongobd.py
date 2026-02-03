
from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://gl0427:wasiq123@cluster0.afuprqr.mongodb.net/?retryWrites=true&w=majority")
print(client)

database = client['taskdb']
collection = database["MyMongoTable"]

@app.route('/insert/mongo',methods = ['POST','GET'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str('Successfully Inserted'))

if __name__ == '__main__':
    app.run(port = 5001)