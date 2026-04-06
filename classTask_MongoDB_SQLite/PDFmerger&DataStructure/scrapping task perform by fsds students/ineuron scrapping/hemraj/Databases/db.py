import pymongo
import logging as logger

logger.basicConfig(filename='./Log/app_logs.log', level=logger.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


class DatabaseOpr:

    client = pymongo.MongoClient(
        "mongodb+srv://root:Welcome123@cluster0.rf9ij.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db_connection = client.ineuronCourseScaperNew

    def __init__(self):
        pass


    def insertCourseInfo(self,course_details):
            """Insert Course list"""
            try:
                #logger.info(course_details)

                #batch insertion
                batchSize = 10
                recordBatch = int(len(course_details)/batchSize)
                logger.info(recordBatch)
                for item in range(recordBatch):
                    selectedPage = item+1
                    start = int((selectedPage - 1) * batchSize);
                    end = int(selectedPage * batchSize);
                    insertData =  course_details[start:end]

                    try:
                        courseDetailsColl = DatabaseOpr.db_connection["courseDetailsInueron"]
                        result =  courseDetailsColl.insert_many(insertData)
                        return result.inserted_ids
                    except Exception as e:
                        logger.exception("Error occurred while inserting a data into collection :====>  " + str(e))

            except Exception as e:
                logger.exception(str(e))

    def insertCourseIndividuals(self,course_details):
            """Insert Course Detail data based on course name"""
            #logger.info(course_details)

            try:
                courseDetailsColl = DatabaseOpr.db_connection["individuals_inueron_course"]
                insertedid = courseDetailsColl.insert_one(course_details).inserted_id
                return insertedid
            except Exception as e:
                logger.exception("Error occurred while inserting a fetching into collection :====>  " + str(e))


    def getCourseDetails(self):
        """Get All Course Detail"""
        try:
            logger.info("======getCourseDetails=======")
            courseColl = DatabaseOpr.db_connection["courseDetailsInueron"]
            res =  courseColl.find()
            return res

        except Exception as e:
            logger.exception("Error occurred while fetch a fetching fom collection :====>  " + str(e))


    def findIndivisualCourse(self,slug):
        """check course exist or not in DB"""
        try:
            courseColl = DatabaseOpr.db_connection["individuals_inueron_course"]
            return courseColl.count_documents({"query.slug": slug})
        except Exception as e:
            logger.exception("Error occurred while fetching a data fom collection :====>  " + str(e))

    def findCourseName(self,course_name):
        """check course content exist or not in DB"""
        try:
            courseColl = DatabaseOpr.db_connection["courseDetailsInueron"]
            return courseColl.count_documents({"course_name": course_name})
        except Exception as e:
            logger.exception("Error occurred while fetching a data fom collection :====>  " + str(e))


    def courseNameDetails(self,course_name):
        """get course content based on it's name"""
        try:
            c_name = f"{course_name}"
            query = {"query.slug": c_name}
            courseColl = DatabaseOpr.db_connection["individuals_inueron_course"]
            return courseColl.find_one(query)
        except Exception as e:
            logger.exception("Error occurred while fetching a data fom collection :====>  " + str(e))