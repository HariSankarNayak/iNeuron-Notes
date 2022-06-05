import pymongo
from logger import logger


def connection(uri: str):
    """Connects to course collection

    Args:
        uri (str): MongoDB URI connection string

    Returns:
        object: course collection object
    """
    client = pymongo.MongoClient(uri)
    database = client["fsds-scrapper"]
    course_collection = database["course"]
    logger.debug("Database Connected")
    return course_collection

