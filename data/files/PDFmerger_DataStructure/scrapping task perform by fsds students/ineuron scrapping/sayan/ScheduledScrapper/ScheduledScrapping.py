import os
from selenium import webdriver
from iNeuronScrapping.pageScrapping import CourseScrapper
from dbOperation.mongodb import  mongodbOperation
from application_logging.logger import app_log

class autoScrapper:
    '''
    This class shall be used for auto scrapping

    Written By: Sayan Saha
    Version: 1
    Revision: None
    '''
    def __init__(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            self.chrome_options.add_argument("--no-sandbox")
            self.driver_path=os.environ.get("CHROMEDRIVER_PATH")

            # self.driver_path = './chromedriver'
            self.dbName = 'iNeuron_scrapper'
            self.collectionName = 'iNeuron_courses'
            self.dbOps = mongodbOperation(username='ineuron_scrapper', password='iNeuron')
            self.lg = app_log(username='ineuron_scrapper', password='iNeuron')
        except Exception as e:
            self.lg.log(tag='ERROR', message=f'Something went wrong to initialize autoscrapping: {e}')

    def autoScrapping(self):
        '''
        Method Name: autoScrapping
        Description : If collection present then it pass, else
                      receive all links from website, then receive all course information
                      and insert them into database
        Output: None
        On Failure: Exception

        Written by: Sayan Saha
        Version: 1
        Revision: None

        '''
        try:
            if self.dbOps.isCollectionPresent(dbName=self.dbName, collectionName=self.collectionName):
                pass
            else:
                scrapper = CourseScrapper(driver_path=self.driver_path, chrome_options=self.chrome_options)  # initialization of scrapping
                ineuron_url = "https://courses.ineuron.ai/"
                all_course_links = scrapper.get_all_course_links(url=ineuron_url, load_time=60)
                self.lg.log(tag='INFO', message='Received all course links from website successfully!!')

                all_course_info = scrapper.get_all_course_info(all_course_links=all_course_links)
                self.lg.log(tag='INFO', message='Scrapped all course informations successfully!!')

                self.dbOps.createDatabase(dbName=self.dbName)
                self.lg.log(tag='INFO', message=f'Database:{self.dbName} created successfully!!')
                self.dbOps.createCollection(dbName=self.dbName, collectionName=self.collectionName)
                self.lg.log(tag='INFO', message=f'Collection:{self.collectionName} in Database:{self.dbName} created successfully!!')
                self.dbOps.insertManyData(dbName=self.dbName, collectionName=self.collectionName, data=all_course_info)
                self.lg.log(tag='INFO', message='All course informations inserted into database successfully!!')
        except Exception as e:
            self.lg.log(tag='ERROR', message=f'Something went wrong during auto scrapping: {e}')

