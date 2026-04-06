from loggerMainClass import scrapLogger
import pymongo

class MongoDbUtils:
    def __init__(self, username, password):
        """
        Constructor initializes monogdb url link
        """
        try:
            self.username = username
            self.password = password
            self.url = "mongodb+srv://mongodb:mongodb@cluster0.oxgpt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(self.username, self.password)
            self.client = pymongo.MongoClient(self.url)
            self.logger = scrapLogger.ineuron_scrap_logger()

        except Exception as e:
            print(f"[__init__]: Something went wrong on initiation process\n" + str(e))

    def createDatabase(self, db_name):
        """
        This function checks whether the database is present or not.
        :param db_name:
        :return:
        """
        try:
            self.database = self.client[str(db_name)]
        except Exception as e:
            self.logger.error("[createDatabase]:Database Creation issue" + str(e))
            print("[createDatabase]:Database Creation issue", e)
        else:
            print("Connection Established")
            self.logger.info('Connection Established!' + str(self.client))

    def isCollectionPresent(self, collection_name):
        """
        This checks if collection is present or not.
        :param collection_name:
        :return:
        """
        try:
            database_status = self.database.name in self.client.list_database_names()
            self.logger.info(f"Database {self.database} present")
            if database_status:
                if collection_name in self.database.list_collection_names():
                    self.logger.info(f"Collection {collection_name} present")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            self.logger.info(f"[isCollectionPresent]: Failed to check collection\n" + str(e))
            print(f"[isCollectionPresent]: Failed to check collection\n" + str(e))

    def getRecords(self, collection_name):
        """
        This fetches collection data from database.
        :param collection_name:
        :return:
        """
        try:
            collection = self.database[collection_name]
            data = collection.find()
            self.logger.info(f"Fetching records from collection")
            return data
        except Exception as e:
            self.logger.info("[getRecords]:Problem occured while fetching data" + str(e))
            print("[getRecords]:Problem occured while fetching data")

    def createCollection(self, collection_name):

        try:
            collection_status_check = self.isCollectionPresent(collection_name)
            if not collection_status_check:
                self.collection = self.database[str(collection_name)]
        except Exception as e:
            self.logger.info(f"[getRecords]: Failed to create collection {collection_name}\n" + str(e))
            print(f"[getRecords]: Failed to create collection {collection_name}\n" + str(e))

    def insertDocument(self,record):
        """
       Insert one  or list of document at a time
       :param:
       arg1(collection_name): record.
       :return:
       """
        try:
            collection = self.database[self.collection.name]
            if type(record) == list:
                collection.insert_many(record)
                self.logger.info(f"Inserted record in list")
            else:
                self.collection.insert_one(record)
                self.logger.info(f"Inserted one record at a time")
        except Exception as e:
            self.logger.info("Something went wrong in inserting one document" + str(e))
            raise Exception("Something went wrong in inserting one document", str(e))







