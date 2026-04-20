import logging
import pymongo


class MyBaseDB:

    def __init__(self, mongodb_connect_url, db_name):
        self.__connect__(mongodb_connect_url, False)
        self.__create_db__(db_name)

    def __connect__(self, connect_url, low_security):
        """connection with mongo db """
        try:
            # rechange format exception not happen here
            if low_security:
                logging.info("connection with std mangodb")
                self.__client = pymongo.MongoClient(connect_url)
            else:
                logging.info("connect mongodb with some insecurity")
                self.__client = pymongo.MongoClient(connect_url, tls=True, tlsAllowInvalidCertificates=True)
        except Exception as e:
            logging.error(e, exc_info=True)
            logging.info("retry mongodb connection")
            self.__connect__(connect_url, True)
        else:
            logging.info("Successfully connected with mongodb")

    def __create_db__(self, db_name):
        """create database"""
        logging.info("try to create db " + db_name)

        try:
            if not self.check_db_exist(db_name):
                self.__db = self.__client[db_name]
                logging.info("Successfully created db " + db_name)
            else:
                logging.info("Already exist db " + db_name)
                self.connect_db_by_name(db_name)


        except Exception as e:
            logging.error(e, exc_info=True)

    def connect_db(self):
        """connect to database"""
        return self.__db

    def close_connection(self):
        """close connection of mongo db """
        try:
            self.__client.close()
            logging.info("Successfully closed connection of mongodb")
        except Exception as e:
            logging.error(e, exc_info=True)

    def drop_current_db(self):
        """drop current working database with attach instance"""
        try:
            if self.check_db_exist(self.__db.name):
                logging.info("try to delete complete db")
                data = self.__client.drop_database(self.__db)
                logging.info("Successfully deleted db " + str(data))
            else:
                logging.info("No db exist with this name")

        except Exception as e:
            logging.error(e, exc_info=True)

    def connect_db_by_name(self, db_name):
        """Connect database using name"""

        logging.info("try to connecting db " + db_name)
        try:
            if self.check_db_exist(db_name):
                self.__db = self.__client[db_name]
                logging.info("Successfully connected with db " + db_name)
                return self.__db
            else:
                logging.error("No db available with this name " + db_name)
                return None
        except Exception as e:
            logging.error(e, exc_info=True)

    def check_db_exist(self, db_name):
        """this is checking database exist or not """
        logging.info("check db exist " + db_name)
        try:
            if db_name in self.__client.list_database_names():
                return True
            else:
                return False
        except Exception as e:
            logging.error(e, exc_info=True)
