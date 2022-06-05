from setting.setting import Setting
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging
from db_connection.mongodboperation import DbOperation


class Scrapping(Setting):

    def __init__(self, db_operation: DbOperation):
        super(Scrapping, self).__init__("scrapping.log")
        self.base_url = "https://ineuron.ai/"
        self.db_operation = db_operation
        try:
            self.connect_chrome()
        except Exception as e:
            logging.error(e, exc_info=True)

    def scroll_to_end(self, wd):
        """selenium scrolling to end"""
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def collect_course_detail_links(self, driver):
        """collect all course links"""
        course_links = []
        while True:
            course_main_html = bs(driver.page_source, "html.parser")
            # main_pg_left_boxes = course_main_html.findAll("div", {"class": "Course_left-area__QeYpw"})
            main_pg_right_boxes = course_main_html.findAll("div", {"class": "Course_right-area__1XUfi"})

            if len(course_links) > 0 and \
                    len(main_pg_right_boxes) > 0 and \
                    course_links[-1] == main_pg_right_boxes[-1].a["href"]:
                break

            for i in main_pg_right_boxes:
                course_links.append(i.a["href"])
               # logging.info(i.a["href"])

            self.scroll_to_end(driver)

        return course_links

    def collect_detail(self, courses_links, driver, course_main_url):
        """collect per course detail"""
        count = 0
        final_details = []
        finalized_links = []
        while count < len(courses_links):

            final_data = {}
            final_data["link"] = courses_links[count]

            try:
                driver.get(course_main_url + courses_links[count])
                driver.find_element_by_class_name("CurriculumAndProjects_view-more-btn__3ggZL").click()
            except Exception as e:
                logging.info("no view more button found on courses")

            # common information block
            try:
                category_boxes_ele = driver.find_element_by_class_name("Hero_course-category-breadcrumb__2-9JD")
                category_and_subcategory = category_boxes_ele.text.split(">")
                course_category = category_and_subcategory[0]
                course_subcategory = category_and_subcategory[1]

                course_name = driver.find_element_by_class_name("Hero_course-title__1a-Hg").text
                course_desc = driver.find_element_by_class_name("Hero_course-desc__26_LL").text

                final_data["category"] = course_category
                final_data["subcategory"] = course_subcategory
                final_data["name"] = course_name
                final_data["description"] = course_desc
            except Exception as e:
                logging.critical(e, exc_info=True)
            # course_price = driver.find_element_by_class_name("CoursePrice_dis-price__3xw3G").text

            # course_under_company = driver.find_element_by_class_name("CoursePrice_no-cost-emi__5rPTT").text.split("part of")[1]

            detail_page = bs(driver.page_source, "html.parser")
            # extract features
            try:
                features_tag = detail_page.find("div", {"class": "CoursePrice_course-features__2qcJp"}).find(
                    "ul").findAll(
                    "li")
                features = []
                for i in features_tag:
                    features.append(i.text)
                final_data["features"] = features
            except Exception as e:
                logging.critical(e, exc_info=True)

            # extract learning
            try:
                learning_tag = detail_page.find("div", {"class": "CourseLearning_card__WxYAo card"}).find("ul").findAll(
                    "li")
                learnings = []
                for i in learning_tag:
                    learnings.append(i.text)

                final_data["learnings"] = learnings
            except Exception as e:
                logging.critical(e, exc_info=True)

            # extract requirements
            try:
                requirements_tag = detail_page.find("div", {"class": "CourseRequirement_card__3g7zR"}).find(
                    "ul").findAll(
                    "li")
                requirements = []
                for i in requirements_tag:
                    requirements.append(i.text)
                final_data["requirements"] = requirements
            except Exception as e:
                logging.critical(e, exc_info=True)

            # extract syllabus
            try:
                course_curriculum_headers_tags = detail_page.findAll("div", {
                    "class": "CurriculumAndProjects_accordion-header__3ALRY"})
                course_curriculum_data_tags = detail_page.findAll("div",
                                                                  {
                                                                      "class": "CurriculumAndProjects_accordion-body__3R51L"})
                course_headers = []
                for i in course_curriculum_headers_tags:
                    course_headers.append(i.span.text)

                course_heading_nd_topics = {}
                for index, d in enumerate(course_curriculum_data_tags):
                    child_data_tags = d.find("ul").findAll("li")
                    topics = []

                    for i in child_data_tags:
                        topics.append(i.text)

                    course_heading_nd_topics[course_headers[index]] = topics
                final_data["syllabus"] = course_heading_nd_topics

            except Exception as e:
                logging.critical(e, exc_info=True)
            # extract mentors
            try:
                mentors_tags = detail_page.findAll("div", {"class": "InstructorDetails_mentor__2hmG8"})

                mentors = []
                for i in mentors_tags:

                    left_tags = i.find("div", {"class": "InstructorDetails_left__3jo8Z"})

                    name = left_tags.find("h5").text
                    desc = left_tags.find("p").text

                    link_tags = left_tags.find("div", {"class": "InstructorDetails_flex__2ePsQ flex"}).findAll("a")

                    links = []
                    for j in link_tags:
                        links.append(j["href"])

                    data = {"name": name, "desc": desc, "social_links": links}

                    try:
                        photo = i.find("div", {"class": "InstructorDetails_right__J_1nt "}).find("img")["src"]
                        data["photo"] = photo
                    except Exception as e:
                        logging.error(f"not found {name} mentor image ")

                    mentors.append(data)

                final_data["mentors"] = mentors
            except Exception as e:
                logging.error(e, exc_info=True)

            logging.info(f"{count}, {final_data['link']}")

            final_details.append(final_data)
            finalized_links.append(courses_links[count])
            count += 1

        return final_details, finalized_links

    def open_ineuron(self, driver):
        """start scrapping """
        try:

            driver.get(self.base_url)
            driver.find_element_by_class_name("btn-secondary").click()

            courses_links = self.collect_course_detail_links(driver)
            course_main_url = driver.current_url
            courses_links = list(set(courses_links))
            # print(len(courses_links), courses_links[-1])
            finalized = []
            temps = []
            try:

                for i in self.db_operation.current_coll.find({}, {"link": 1}):
                    temps.append(i['link'])

            except Exception as e:
                logging.error(e, exc_info=True)

            diff_online_data = []
            if len(temps) < len(courses_links):
                diff_online_data = self.diff(courses_links, temps)

                if len(diff_online_data) > 0:
                    courses_links = diff_online_data

            while len(diff_online_data) > 0:
                final_details, finalized_links = self.collect_detail(courses_links, driver, course_main_url)

                logging.info(f"final_details {len(final_details)}")
                finalized += final_details
                left_links = self.diff(courses_links, finalized_links)
                logging.info(f"left_links {len(left_links)}")
                courses_links = left_links
                if len(left_links) == 0:
                    break

            if len(finalized) > 0:
                self.db_operation.insert_bulk_data(finalized)
            driver.dispose()

            logging.info("Scrapping done")

        except Exception as e:
            logging.error(e, exc_info=True)
            driver.dispose()

    def diff(self, li1, li2):
        return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

    def connect_chrome(self):
        """connect to chrome driver with options """
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-site-isolation-trials')
        # chrome_options.add_argument("window-size=1920,1080")
        chrome_options.page_load_strategy = 'eager'

        with webdriver.Chrome(executable_path="scrapping/chromedriver.exe", options=chrome_options) as wd:
            self.open_ineuron(wd)
