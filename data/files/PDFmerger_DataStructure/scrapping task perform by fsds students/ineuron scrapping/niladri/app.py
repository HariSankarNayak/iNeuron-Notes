from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup as bs
import time
import mysql.connector as conn
import logging

from models import *

app = Flask(__name__)

logging.basicConfig(filename='appLog.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    logging.info("Starting home page")
    setupSQLConn()
    return render_template("index.html")


@app.route('/maincourses', methods=['POST'])  # route to display the home page
@cross_origin()
def getCourses():
    if request.method == 'POST':
        try:
            iNeuronHome = "https://ineuron.ai"

            # Scrape Main Course Items
            chrome_options = Options()
            chrome_options.add_argument("--window-size=1400,800")
            driver = Chrome(executable_path='chromedriver',
                            chrome_options=chrome_options)
            driver.get(iNeuronHome)
            driver.find_element_by_xpath("//li[contains(@id, 'course-dropdown')]//img").click()
            driver.find_element_by_xpath("//li[contains(@id, 'course-dropdown')]//img").click()
            iNeuronHome_html = bs(driver.page_source)
            driver.quit()

            main_courses = []
            for i in range(
                    len(iNeuronHome_html.findAll("div", {"class": "courses-card-list card flex"})[0].findAll("a"))):
                courseName = iNeuronHome_html.findAll("div", {"class": "courses-card-list card flex"})[0].findAll("li")[
                    i].text
                # courseLink = iNeuronHome_html.findAll("div", {"class": "courses-card-list card flex"})[0].findAll("a")[i].get('href')
                mc1 = MainCourse(courseName.strip())
                main_courses.append(mc1)

            # Get all MainCourse details
            logging.info("Retrieved Main Course list from ", iNeuronHome)
            for i in main_courses:
                i.printMainCourse()

            # Scrape Main Course SubTopic Name and URLs
            driver = Chrome(executable_path='chromedriver',
                            chrome_options=chrome_options)
            driver.get(iNeuronHome)
            time.sleep(5)
            try:
                driver.find_element_by_xpath("//div[contains(@id, 'enquiry-modal')]//div//div//i").click()
            except NoSuchElementException:
                pass
            driver.find_element_by_xpath("//li[contains(@id, 'course-dropdown')]//img").click()
            driver.find_element_by_xpath("//li[contains(@id, 'course-dropdown')]//img").click()

            for mc in main_courses:
                sub_topic_element = driver.find_element_by_link_text(mc.courseName)
                actions = ActionChains(driver)
                actions.move_to_element(sub_topic_element).perform()
                iNeuronHome_html = bs(driver.page_source)
                sub_topic_no = len(
                    iNeuronHome_html.findAll('div', {'class': 'courses-card-list card flex'})[0].findAll('div', {
                        'id': 'subcategories-list'})[0].findAll('a'))
                for i in range(sub_topic_no):
                    stname = iNeuronHome_html.findAll('div', {'class': 'courses-card-list card flex'})[0].findAll('div',
                                                                                                                  {
                                                                                                                      'id': 'subcategories-list'})[
                        0].findAll('li')[i].text
                    stURL = iNeuronHome_html.findAll('div', {'class': 'courses-card-list card flex'})[0].findAll('div',
                                                                                                                 {
                                                                                                                     'id': 'subcategories-list'})[
                        0].findAll('a')[i].get('href')
                    s1 = SubTopic(stname, stURL)
                    mc.add_subTopic(s1)
            driver.quit()

            # Load data into Database
            logging.info("Going to insert courses into Database")
            loadMainCourseTable(main_courses)

            return render_template("maincourses.html", mainCourses=main_courses)
        except Exception as e:
            logging.error('The Exception message is: ', e)
            return 'Exception occured'


@app.route('/subtopics', methods=['POST'])  # route to display the home page
@cross_origin()
def getSubtopics():
    if request.method == 'POST':
        try:
            stName = request.form.get("subTopicName")
            stURL = request.form.get("subTopicURL")
            st = SubTopic(stName, stURL)
            logging.info("Going to get the details of SubTopic:", st.printSubTopic())

            # Scrape Sub Topic Items
            chrome_options = Options()
            chrome_options.add_argument("--window-size=1400,800")
            driver = Chrome(executable_path='chromedriver',
                            chrome_options=chrome_options)
            driver.get(stURL)
            time.sleep(3)
            previous_height = driver.execute_script('return document.body.scrollHeight')
            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height == previous_height:
                    break
                previous_height = new_height
            sub_topic_html = bs(driver.page_source)
            driver.quit()

            course_num = int(len(sub_topic_html.findAll("h5", {"class": "Course_course-title__2rA2S"})) / 2)
            logging.info("Total number of courses available for this SubTopic is:", course_num)

            for i in range(course_num):
                course_name = sub_topic_html.findAll("h5", {"class": "Course_course-title__2rA2S"})[i].text
                course_url = (
                        st.subTopicURL[0:26] + sub_topic_html.findAll("div", {"class": "Course_right-area__1XUfi"})[
                    i].a.get('href'))
                logging.info('Course Name:', course_name)
                logging.info('Course URL:', course_url)
                c1 = Course(course_name, course_url)
                st.add_subTopicCourse(c1)

            # Load data into Database
            logging.info("Going to insert sub topics into Database")
            loadSubtopicTable(st)

            return render_template("subtopics.html", subtopic=st)
        except Exception as e:
            logging.error('The Exception message is: ', e)
            return 'Exception occured'


@app.route('/courses', methods=['POST'])
def getCourseDetails():
    if request.method == 'POST':
        try:
            course_name = request.form.get("courseName")
            course_url = request.form.get("courseURL")
            course = Course(course_name, course_url)
            logging.info("Going to get the details of Course:", course.printCourse())

            # Scrape Course Page details
            chrome_options = Options()
            chrome_options.add_argument("--window-size=1400,800")
            driver = Chrome(executable_path='chromedriver',
                            chrome_options=chrome_options)
            driver.get(course_url)
            time.sleep(5)
            try:
                driver.find_element_by_xpath("//div[contains(@id, 'enquiry-modal')]//div//div//i").click()
                driver.find_element_by_xpath(
                    "//span[contains(@class, 'CurriculumAndProjects_view-more-btn__3ggZL')]").click()
            except NoSuchElementException:
                pass
            course_html = bs(driver.page_source)
            driver.quit()

            # Set Course Description
            course.set_courseDesc(course_html.findAll("div", {"class": "Hero_course-desc__26_LL"})[0].text)

            # Set Course Learnings
            try:
                course.courseLearnings = []
                learning_num = len(
                    course_html.findAll("div", {"class": "CourseLearning_card__WxYAo card"})[0].findAll("li"))
                if learning_num > 0:
                    for ln in range(learning_num):
                        course.add_courseLearnings(
                            course_html.findAll("div", {"class": "CourseLearning_card__WxYAo card"})[0].findAll("li")[
                                ln].text)
            except IndexError:
                logging.error("IndexError in course Learnings")
                pass

            # Set Course Requirements
            try:
                course.courseRequirements = []
                requirement_num = len(
                    course_html.findAll("div", {"class": "CourseRequirement_card__3g7zR requirements card"})[
                        0].findAll("li"))
                if requirement_num > 0:
                    for rn in range(requirement_num):
                        course.add_courseRequirements(course_html.findAll("div", {
                            "class": "CourseRequirement_card__3g7zR requirements card"})[0].findAll("li")[rn].text)
            except IndexError:
                logging.error("IndexError in course Requirements")
                pass

            # Set Course Features
            try:
                course.courseFeatures = []
                feature_num = len(
                    course_html.findAll("div", {"class": "CoursePrice_course-features__2qcJp"})[0].findAll("li"))
                if feature_num > 0:
                    for ft in range(feature_num):
                        course.add_courseFeatures(
                            course_html.findAll("div", {"class": "CoursePrice_course-features__2qcJp"})[0].findAll(
                                "li")[ft].text)
            except IndexError:
                logging.error("IndexError in course Features")
                pass

            # Set Course Curriculums
            course.courseCurriculums = []
            curriculums = course_html.findAll("div", {
                "class": "CurriculumAndProjects_curriculum-accordion__2pppc CurriculumAndProjects_card__7HqQx card"})
            logging.info("Total number of curriculums found:", len(curriculums))
            for curriculum in curriculums:
                cname = curriculum.findAll("div", {
                    "class": "CurriculumAndProjects_accordion-header__3ALRY CurriculumAndProjects_flex__1-ljx flex"})[
                    0].span.text
                itemDetails = []
                curriculum_details = curriculum.findAll("div", {
                    "class": "CurriculumAndProjects_course-curriculum-list__3rUJt"})
                for details in curriculum_details:
                    itemDetails.append(details.text)
                c1 = Curriculum(cname, itemDetails)
                course.add_courseCurriculums(c1)
                logging.info("Course Curriculums:", c1.printCurriculum())

            # Set Course Faculty details
            course.courseFaculties = []
            faculties = course_html.findAll("div", {
                "class": "InstructorDetails_mentor__2hmG8 InstructorDetails_card__14MoH InstructorDetails_flex__2ePsQ card flex"})
            for faculty in faculties:
                f1 = Faculty(faculty.find('h5').text, faculty.find('p').text)
                logging.info("Faculty details:",f1.printFaculty())
                logging.info("Going to insert faculty details into Database")
                loadFacultyTable(f1)
                course.add_courseFaculties(f1)

            logging.info("Going to insert Curriculum details into Database:", course.printCourse())
            loadCurriculumTable(course)

            logging.info("Going to insert Course details into Database:", course.printCourse())
            loadCourseTable(course)

            return render_template("course.html", course=course)
        except Exception as e:
            logging.error('The Exception message is: ', e)
            return 'Exception occured'


def setupSQLConn():
    logging.info("Setting up SQL Connection")
    mydb = getConn()
    cursor = mydb.cursor()
    cursor.execute("show databases")
    dblist = cursor.fetchall()
    logging.info("Available Databases:", dblist)
    if (any('ineurondata' in i for i in dblist)):
        logging.info("ineurondata is present")
        pass
    else:
        logging.info("Creating ineurondata database")
        cursor.execute("create database iNeuronData")

    cursor.execute('use iNeuronData')
    cursor.execute('show tables')
    tableList = cursor.fetchall()
    logging.info("Available Tables in ineurondata Database:", tableList)

    # mastercourse table
    if (any('mastercourse' in i for i in tableList)):
        logging.info("mastercourse table is present")
        pass
    else:
        logging.info("Creating mastercourse table in iNeuronData database")
        query = "create table iNeuronData.mastercourse(mastercoursename varchar(100), subtopicname VARCHAR(100), subtopicurl VARCHAR(150))"
        cursor.execute(query)

    # subtopic table
    if (any('subtopic' in i for i in tableList)):
        logging.info("subtopic table is present")
        pass
    else:
        logging.info("Creating subtopic table in iNeuronData database")
        query = "create table iNeuronData.subtopic(subtopicname VARCHAR(100), coursename VARCHAR(100), courseurl VARCHAR(150))"
        cursor.execute(query)

    # course table
    if (any('course' in i for i in tableList)):
        logging.info("course table is present")
        pass
    else:
        logging.info("Creating course table in iNeuronData database")
        query = "create table iNeuronData.course(coursename VARCHAR(100), coursedesc VARCHAR(1000), courselearnings VARCHAR(1000), courserequirements VARCHAR(1000), courseFeatures TEXT, coursecurriculumname TEXT, coursefacultyname VARCHAR(500))"
        cursor.execute(query)

    # curriculum table
    if (any('curriculum' in i for i in tableList)):
        logging.info("curriculum table is present")
        pass
    else:
        logging.info("Creating curriculum table in iNeuronData database")
        query = "create table iNeuronData.curriculum(coursename VARCHAR(100), coursecurriculumname VARCHAR(100), coursecurriculumdetails TEXT)"
        cursor.execute(query)

    # faculty table
    if (any('faculty' in i for i in tableList)):
        logging.info("faculty table is present")
        pass
    else:
        logging.info("Creating faculty table in iNeuronData database")
        query = "create table iNeuronData.faculty(coursefacultyname VARCHAR(100), coursefacultyprofile VARCHAR(1000))"
        cursor.execute(query)

    mydb.commit()


def getConn():
    # Local
    mydb = conn.connect(host='localhost', user='root', passwd='MySql@123')

    # AWS
    # mydb = conn.connect(host='ineurondatabase.caxhx34dldru.us-east-1.rds.amazonaws.com', user='admin',
    #                    passwd='mysql1234')
    return mydb


def loadMainCourseTable(main_courses):
    logging.info('getConn loadMainCourseTable called')
    try:
        if isinstance(main_courses, list):
            for mc in main_courses:
                if isinstance(mc, MainCourse):
                    if isinstance(mc.subTopics, list):
                        for st in mc.subTopics:
                            if isinstance(st, SubTopic):
                                mydb = getConn()
                                cursor = mydb.cursor()

                                # Check before inserting whethere Entry is present in the table or not
                                squery = "select * from iNeuronData.mastercourse where mastercoursename = %s and subtopicname = %s and subtopicurl = %s"
                                args = (mc.courseName, st.subTopicName, st.subTopicURL)
                                cursor.execute(squery, args)
                                # logging.info('Cursor fetchall', cursor.fetchall())

                                # Only insert into database if the entry is not there
                                if len(cursor.fetchall()) == 0:
                                    iquery = "insert into iNeuronData.mastercourse values(%s, %s, %s)"
                                    args = (mc.courseName, st.subTopicName, st.subTopicURL)
                                    logging.info("Row inserted into mastercourse table", args)
                                    cursor.execute(iquery, args)
                                    mydb.commit()
    except Exception as e:
        logging.info('The Exception message is: ', e)
        return 'Exception occured'


def loadSubtopicTable(subTopic):
    logging.info('loadSubtopicTable method called')
    try:
        if isinstance(subTopic, SubTopic):
            if isinstance(subTopic.subTopicCourses, list):
                for stc in subTopic.subTopicCourses:
                    if isinstance(stc, Course):
                        mydb = getConn()
                        cursor = mydb.cursor()

                        # Check before inserting whethere Entry is present in the table or not
                        squery = "select * from iNeuronData.subtopic where subtopicname = %s and coursename = %s and courseurl = %s"
                        args = (subTopic.subTopicName, stc.courseName, stc.courseURL)
                        cursor.execute(squery, args)

                        # Only insert into database if the entry is not there
                        if len(cursor.fetchall()) == 0:
                            iquery = "insert into iNeuronData.subtopic values(%s, %s, %s)"
                            cursor.execute(iquery, args)
                            logging.info("Row inserted into subtopic table", args)
                            mydb.commit()
    except Exception as e:
        logging.info('The Exception message is: ', e)
        return 'Exception occured'


def loadCourseTable(course):
    logging.info('loadCourseTable method called')
    try:
        if isinstance(course, Course):
            mydb = getConn()
            cursor = mydb.cursor()
            # Check before inserting whethere Entry is present in the table or not
            squery = "select * from iNeuronData.course where coursename = %s"
            sargs = (course.courseName,)
            cursor.execute(squery, sargs)

            # Only insert into database if the entry is not there
            if len(cursor.fetchall()) == 0:
                iquery = "insert into iNeuronData.course values(%s, %s, %s, %s, %s, %s, %s)"
                iargs = (
                    course.courseName, course.courseDesc, str(course.courseLearnings), str(course.courseRequirements),
                    str(course.courseFeatures), str(course.get_courseCurriculumNames()),
                    str(course.get_courseFaculty()))
                cursor.execute(iquery, iargs)
                logging.info("Row inserted into course table", iargs)
                mydb.commit()
    except Exception as e:
        logging.info('The Exception message is: ', e)
        return 'Exception occured'


def loadCurriculumTable(course):
    logging.info('loadCurriculumTable method called')
    try:
        if isinstance(course, Course):
            if isinstance(course.courseCurriculums, list):
                for curr in course.courseCurriculums:
                    if isinstance(curr, Curriculum):
                        mydb = getConn()
                        cursor = mydb.cursor()

                        # Check before inserting whethere Faculty is present in the table or not
                        squery = "select * from iNeuronData.curriculum where coursename = %s and coursecurriculumname = %s"
                        sargs = (course.courseName, curr.name)
                        cursor.execute(squery, sargs)

                        # Only insert into database if the entry is not there
                        if len(cursor.fetchall()) == 0:
                            iquery = "insert into iNeuronData.curriculum values(%s, %s, %s)"
                            iargs = (course.courseName, curr.name, str(curr.curriculumListDetails))
                            cursor.execute(iquery, iargs)
                            logging.info("Row inserted into curriculum table", iargs)
                            mydb.commit()
    except Exception as e:
        logging.info('The Exception message is: ', e)
        return 'Exception occured'


def loadFacultyTable(faculty):
    logging.info('loadFacultyTable method called')
    try:
        if isinstance(faculty, Faculty):
            mydb = getConn()
            cursor = mydb.cursor()

            # Check before inserting whethere Faculty is present in the table or not
            logging.info("Searching for faculty name:", faculty.name)
            squery = "select * from iNeuronData.faculty where coursefacultyname = %s "
            sargs = (faculty.name,)
            cursor.execute(squery, sargs)

            # Only insert into database if the entry is not there
            if len(cursor.fetchall()) == 0:
                logging.info("Going to insert Faculty object: {", faculty.name, ", ", faculty.profile, "}")
                iquery = "insert into iNeuronData.faculty values(%s, %s)"
                iargs = (faculty.name, faculty.profile)
                cursor.execute(iquery, iargs)
                logging.info("Row inserted into faculty table", iargs)
                mydb.commit()
        else:
            logging.info("Error in parsing Faculty object in loadFacultyTable()")
    except Exception as e:
        logging.info('The Exception message is: ', e)
        return 'Exception occured'


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
