from urllib.request import urlopen
from loggerMainClass import scrapLogger
from bs4 import BeautifulSoup
import requests
import json
import os
from selenium import webdriver
from helium import *

DRIVER_PATH = r'chromedriver.exe'
DEV_BUILD = False

class ineuronScrapper:
    def __init__(self, course_name, refactor_object, db_object):
        """
        Constructor initialization
        """
        self.url_path = refactor_object.getIneuronUrl()
        self.course_name = course_name
        self.db_object = db_object
        self.refactor_object = refactor_object
        self.logger = scrapLogger.ineuron_scrap_logger()

    def getCourseCategory(self):
        try:
            """
            This function scraps all the course in selected category. 
            """
            category_url = self.refactor_object.getIneuronUrl() + 'category/' + self.course_name
            uClient = urlopen(category_url)
            ineuron_page = uClient.read()
            uClient.close()
            self.logger.info("uClient hitted")
            category_page_html = BeautifulSoup(ineuron_page, "html.parser")
            self.logger.info("Page parsed")
            script_tag_data = json.loads(category_page_html.find('script', {"id": "__NEXT_DATA__"}, type="application/json").text)
            scrapped_courses = script_tag_data['props']['pageProps']['initialState']['filter']['initCourses']
            self.logger.info("scrapped_courses fetched")
            self.logger.info('All courses scrapped')
            course_names = []
            for course in scrapped_courses:
                course_names.append(course['title'])
            self.logger.info("course_names fetched")
            return course_names
        except Exception as e:
            self.logger.info("[getCourseCategory]: Error occurred while extracting category")
            print("[getCourseCategory]: Error occurred while extracting category", str(e))

    def getCourseTitle(self, soup_obj):
        """
        This function scraps Course Title of particular course.
        :param : beautifulSoup object
        :return: Course Tile
        """
        try:
            self.logger.info('Scrapped course tile')
            return soup_obj.find("h3", self.refactor_object.getCourseTitle()).text
        except Exception as e:
            print("[getCourseTitle]: Error occurred while extracting CourseTitle", str(e))

    def getCourseDescription(self, soup_obj):
        """
        This function scraps Course Description of particular course.
        :param : beautifulSoup object
        :return: Course Description
        """
        try:
            self.logger.info('Scrapped course Description')
            return soup_obj.find("div", self.refactor_object.getCourseDescription()).text
        except Exception as e:
            print("[getCourseDescription]: Error occurred while extracting CourseDescription", str(e))

    def getCourseFees(self, soup_obj):
        """
        This function scraps Course Fees of particular course.
        :param : beautifulSoup object
        :return: Course Fees
        """
        try:
            price_div = soup_obj.find("div", self.refactor_object.getCourseFees())
            if price_div.text:
                course_price = soup_obj.find("div", self.refactor_object.getCourseFees()).text
            else:
                course_price = soup_obj.find("div", self.refactor_object.getCourseFees()).find("span").text
            self.logger.info('Scrapped course Fees')
            return course_price
        except Exception as e:
            print("[getCourseDescription]: Error occurred while extracting CourseFees", str(e))

    def getClassTimings(self, soup_obj):
        """
        This function scraps Class Timings of particular course.
        :param : beautifulSoup object
        :return: Class Timings
        """
        try:
            if len(soup_obj.find_all("div", self.refactor_object.getClassTimings())) > 0:
                class_timing = soup_obj.find_all("div", self.refactor_object.getClassTimings())[0].text
                doubt_timing = soup_obj.find_all("div", self.refactor_object.getClassTimings())[1].text
            else:
                class_timing = "NA"
                doubt_timing = "NA"
            self.logger.info('Scrapped course class_timing')
            return class_timing, doubt_timing
        except Exception as e:
            print("[getClassTimings]: Error occurred while extracting class_timing", str(e))

    def getMentorsName(self, soup_obj):
        """
        This function scraps Mentors Name of particular course.
        :param : beautifulSoup object
        :return: Mentors Name List
        """
        try:
            instructors_name = []
            for instructor in soup_obj.find_all("div", self.refactor_object.getMentorsName()):
                instructors_name.append({"name": instructor.h5.text})
            if len(instructors_name) == 0:
                instructors_name.append({"name": "NA"})
            self.logger.info('Scrapped course instructors_name')
            return instructors_name
        except Exception as e:
            print("[getMentorsName]: Error occurred while extracting instructors_name", str(e))

    def scrapListElements(self, soup_obj, flag_value):
        """
        This function scraps all unordered HTML Lists of particular course.
        :param : beautifulSoup object
        :return: List
        """
        try:
            scrapped_list = []
            if flag_value == "what_learn":
                ul_class_element = soup_obj.find("div", self.refactor_object.getWhatYouWillLearn()).find("ul")
            elif flag_value == "requirements":
                ul_class_element = soup_obj.find("div", self.refactor_object.getRequirements()).find("ul")
            elif flag_value == "features":
                ul_class_element = soup_obj.find("div", self.refactor_object.getCourseFeatures()).find("ul")
            if ul_class_element:
                for li in ul_class_element.find_all("li"):
                    scrapped_list.append(li.text)
                if len(scrapped_list) == 0:
                    scrapped_list.append("NA")
            self.logger.info("Scrapped scrapped_list")
            return scrapped_list
        except Exception as e:
            print(f"[{flag_value}]: Error occurred while extracting {flag_value}", str(e)).format(flag_value)

    def getCurriculumList(self, soup_obj):
        """
        This function scraps all course curriculum Lists of particular course.
        :param : beautifulSoup object
        :return: List
        """
        try:
            course_curriculum_list = []
            if len(soup_obj.find_all("div", self.refactor_object.getCurriculumList())) > 0:
                for single_card in soup_obj.find_all("div", self.refactor_object.getCurriculumList()):
                    course_topics = []
                    course_heading = single_card.find("div", self.refactor_object.getCurriculumCard()).find("span").text
                    if len(single_card.find("ul")) > 0:
                        for li in single_card.find("ul"):
                            course_topics.append(li.text)
                        course_curriculum_list.append({"heading": course_heading, "topics": course_topics})
            else:
                course_curriculum_list.append({"heading": "NA", "topics": "NA"})
            self.logger.info("Scrapped course_curriculum_list")
            return course_curriculum_list
        except Exception as e:
            print("[getCurriculumList]: Error occurred while extracting curriculum", str(e))

    def getCourseDetails(self):
        """
        This function prepares and collects data of particular course to render on HTML Page.
        :param : beautifulSoup object
        :return: List
        """
        try:
            course_details = []
            self.db_object.createCollection(self.course_name)

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--disable-gpu')

            if DEV_BUILD:
                print("Chrome Driver version: ", os.system('chromedriver --version'))
                driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
            else:
                chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                                          chrome_options=chrome_options)
            length = len(self.getCourseCategory())
            if length >= 15:
                length = 15
            for course_title in self.getCourseCategory()[:length]:
                course_link = self.refactor_object.getIneuronUrl() + course_title
                self.logger.info("course_link fetched")
                
                driver.get(course_link)
                response = requests.get(course_link)
                response.raise_for_status()
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                self.logger.info("Fetched HTML parsed page")
                course_dictionary = {
                    "Course_Name": self.getCourseTitle(soup),
                    "Course Description": self.getCourseDescription(soup),
                    "Mentors": self.getMentorsName(soup),
                    "Fees": self.getCourseFees(soup),
                    "Requirements": self.scrapListElements(soup, "requirements"),
                    "What_you_learn": self.scrapListElements(soup, "what_learn"),
                    "Course Features": self.scrapListElements(soup, "features"),
                    "Class Timing": self.getClassTimings(soup)[0],
                    "Doubt Timing": self.getClassTimings(soup)[1],
                    "Curriculum": self.getCurriculumList(soup),
                    "accordionExampleID": self.refactor_object.generateUniqueIdsForUI(8),
                    "collapse_id": self.refactor_object.generateUniqueIdsForUI(4),
                    "modal_id": self.refactor_object.generateUniqueIdsForUI(4),
                    "features_id": self.refactor_object.generateUniqueIdsForUI(4),
                }
                course_details.append(course_dictionary)
                self.logger.info("course details")

            driver.close()

            self.db_object.insertDocument(course_details)
            self.logger.info("collected all course details")
            return course_details
        except Exception as e:
            print("[getCourseDetails]: Error occurred while extracting CourseDetails", str(e))
