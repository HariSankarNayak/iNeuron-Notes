import pymongo


client = pymongo.MongoClient("mongodb+srv://gl0427:wasiq123@cluster0.afuprqr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

#client = pymongo.MongoClient("mongodb+srv://gl0427:wasiq123@cluster0.afuprqr.mongodb.net/?retryWrites=true&w=majority")
#db = client.test

print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db = client['mongotest']
coll = db['test']
coll.insert_one(d)


