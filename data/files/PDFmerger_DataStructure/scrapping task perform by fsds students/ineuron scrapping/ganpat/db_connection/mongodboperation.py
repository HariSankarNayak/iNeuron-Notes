from db_connection.mongocore import MyBaseDB
import logging


class DbOperation(MyBaseDB):

    def __init__(self, db_name):
        # self.current_coll = None
        self.db_name = db_name
        connect_url = "mongodb+srv://root:root@cluster0.krwwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        super().__init__(connect_url, db_name=db_name)

    def create_collection(self, collection_name):
        """Create collection using name on current database"""
        logging.info("try to create collection " + collection_name)
        try:
            if not self.check_collection_exist(collection_name):
                self.current_coll = self.connect_db()[collection_name]
                logging.info("Successfully created collection " + collection_name)
            else:
                logging.info("Already exist collection " + collection_name)
        except Exception as e:
            logging.error(e, exc_info=True)

    def connect_current_collection(self, collection_name):
        """Connect to current collection """
        logging.info("try to connect collection " + collection_name)
        try:
            if self.check_collection_exist(collection_name):
                self.current_coll = self.connect_db().get_collection(name=collection_name)
                return self.current_coll
            else:
                logging.error("No collection exist with this name " + collection_name)
        except Exception as e:
            logging.error(e, exc_info=True)

    def insert_bulk_data(self, data):
        """inserting bulk data on collection"""
        logging.info("try to insert bulk data ")
        try:
            self.current_coll.insert_many(data)
        except Exception as e:
            logging.error(e, exc_info=True)
        else:
            logging.info("Successfully inserted bulk data")

    def insert_only_one(self, data):
        """insert single data"""
        logging.info("insert only one data " + str(data))
        try:
            self.current_coll.insert_one(data)
        except Exception as e:
            logging.error(e, exc_info=True)
        else:
            logging.info("Successfully inserted single data " + str(data))

    def get_all_data(self):
        """return all data of collection """
        try:
            data = self.current_coll.find()
            logging.info("data sample showing: " + str(data[5]))
            return data
        except Exception as e:
            logging.error(e, exc_info=True)

    def filter_documents(self, match: dict):
        """filtering data on documents"""
        try:
            logging.info("try to filtering documents with " + str(match))
            data = self.current_coll.find(match)

            logging.info("data sample showing: " + str(data.next()))
            return data
        except Exception as e:
            logging.error(e, exc_info=True)

    def update(self, match: dict, set_data: dict, is_many: bool):
        """update data @param match is used for matching data first
                        @param set_data is used for modify data on matching document
                        @param is_many is check for update on many documents or modify single document"""
        try:
            logging.info("try to update data")
            if is_many:
                data = self.current_coll.update_many(match, {"$set": set_data})
            else:
                data = self.current_coll.update_one(match, {"$set": set_data})
            logging.info("data is updated " + str(data))
        except Exception as e:
            logging.error(e, exc_info=True)

    def delete_all_document(self, match={}):
        """delete many data with or without match key value pair in document """
        try:
            logging.info("try to delete documents")
            data = self.current_coll.delete_many(match)
            logging.info("deleted documents " + str(data))
        except Exception as e:
            logging.error(e, exc_info=True)

    def delete_specific_document(self, match: dict):
        """delete specific data with match """
        try:
            logging.info("try to delete document with specific " + str(match))
            data = self.current_coll.delete_one(match)
            logging.info("deleted document " + str(data))
        except Exception as e:
            logging.error(e, exc_info=True)

    def check_collection_exist(self, col_name):
        """check collection exist or not """

        try:
            logging.info("list of collection " + str(self.connect_db().list_collection_names()))
            if col_name in self.connect_db().list_collection_names():
                logging.info("avail this collection " + col_name)
                return True
            else:
                logging.info("not avail this collection " + col_name)

                return False

        except Exception as e:
            logging.info(e)

    def drop_current_coll(self):
        """drop current collection"""
        try:
            logging.info("try to delete complete collection")
            data = self.connect_db().drop_collection(self.current_coll.name)
            logging.info("Successfully deleted collection " + str(data))
        except Exception as e:
            logging.error(e, exc_info=True)



