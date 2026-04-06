import pymongo

client = pymongo.MongoClient("mongodb+srv://gl0427:wasiq123@cluster0.afuprqr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


db = client.test
database = client['inventory']
collection = database["table"]
#collection.insert_many(data)

# d = collection.find()

# d = collection.find({'status':'A'})                     # Status only A

# d = collection.find({'status':{'$in': ['A', 'P']}})     # Status A or P

# d = collection.find({'status':{'$gt': 'C'}})            # Status greater than C

# d = collection.find({'qty':{'$gte': 75}})               # qty greater than equal to 75

# d = collection.find({'item': 'sketch pad','qty': 95})   # item is sketch and qty is 95

# d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}}) # item is sketch and qty gretater than 75

# d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]}) # item is sketch or qty gretater than 75

# collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })  # Update canvas to sudhanshu

collection.delete_one({'item': 'sudhanshu'})  # Delete the record where item is sudhanshu

# d = collection.find({'item': 'sudhanshu'})

d = collection.find()
for i in d:
    print(i)