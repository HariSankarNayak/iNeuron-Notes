import pymongo
class mongodbOperation:
    '''This class shall be used for mongoDB operation
    written By: Sayan Saha
    version: 1.0
    Revision: None
    '''
    def __init__(self, username, password):
        try:
            self.username=username
            self.password=password
            self.url=f"mongodb+srv://{self.username}:{self.password}@ineuron-scrapper-cluste.7i4g6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        except Exception as e:
            raise e

    def getMongoClient(self):
        '''
        Method Name: getMongoClient
        Description: It creates connection with the database
        Output: MongoClient
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            raise e

    def getDatabase(self, dbName):
        '''
        Method Name: getDatabase
        Description: Gives database
        Output: database
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''

        try:
            client = self.getMongoClient()
            database = client[dbName]
            return database
        except Exception as e:
            raise e

    def getCollection(self, dbName, collectionName):
        '''
        Method Name: getCollection
        Description: Gives collection of a database
        Output: collection
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            database = self.getDatabase(dbName)
            collection = database[collectionName]
            return collection
        except Exception as e:
            raise e

    def isDatabasePresent(self, dbName):
        '''
        Method Name: isDatabasePresent
        Description: Checks whether database present or not
        Output: True if present else False
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''

        try:
            client = self.getMongoClient()
            if dbName in client.list_database_names():
                return True
            else:
                return False
        except Exception as e:
            raise e

    def isCollectionPresent(self, dbName, collectionName):
        '''
        Method Name: isCollectionPresent
        Description: Checks whether collection under a given database present or not
        Output: True if present else False
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            if self.isDatabasePresent(dbName):
                database = self.getDatabase(dbName)
                if collectionName in database.list_collection_names():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            raise e

    def createDatabase(self, dbName):
        '''
        Method Name: createDatabase
        Description: creates a database
        Output: None
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''

        try:
            client = self.getMongoClient()
            database = client[dbName]
        except Exception as e:
            raise e

    def createCollection(self, dbName, collectionName):
        '''
        Method Name: createCollection
        Description: Creates collection under a given database
        Output: None
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            database = self.getDatabase(dbName)
            collection = database[collectionName]
        except Exception as e:
            raise e

    def insertManyData(self, dbName, collectionName, data):
        '''
        Method Name: insertManyData
        Description: Inserts bulk data into database
        Output: None
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            collection = self.getCollection(dbName, collectionName)
            collection.insert_many(data)

        except Exception as e:
            raise e


    def getData(self,dbName,collectionName):
        '''
        Method Name: getData
        Description: Returns all data from a collection of the given database
        Output: Returns a cursor
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            if self.isCollectionPresent(dbName, collectionName):
                collection=self.getCollection(dbName,collectionName)
                data= collection.find()
                return data
        except Exception as e:
            raise e

