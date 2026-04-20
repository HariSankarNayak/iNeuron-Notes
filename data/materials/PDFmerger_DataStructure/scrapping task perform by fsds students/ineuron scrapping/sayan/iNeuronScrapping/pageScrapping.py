from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time


class CourseScrapper:
    '''
    This class shall be used to extract all information from website

    Written By: Sayan Saha
    Version: 1.0
    Revision: None
    '''
    def __init__(self, driver_path, chrome_options):
        try:
            self.driver_path=driver_path
            self.chrome_options=chrome_options
        except Exception as e:
            raise e

    def get_all_course_links(self, url, load_time):
        '''
        Method Name: get_all_course_links
        Description: It opens the course page and wait for the given load_time,
                    if all course links are not loaded then it waits every 5 seconds and
                    checks all course links loaded or not, finally returns all course links

        Output: course_links (type: set)
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            with webdriver.Chrome(executable_path=self.driver_path, chrome_options=self.chrome_options) as wd:
                wd.get(url)
                wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                course_links = set()
                sec = load_time
                while True:
                    try:
                        time.sleep(sec)
                        links = set(wd.find_elements(By.XPATH, "//div[@class='Course_right-area__1XUfi']/a"))
                        for link in links:
                            course_links.add(link.get_attribute("href"))
                        break
                    except:
                        sec = 5
                        continue
            return course_links
        except Exception as e:
            raise e


    def get_topic(self, page_html):
        '''
        Method Name: get_topic
        Description: Extracts topic from HTML page
        Output: topic (type: str)
        On Failure: 'Not Found'

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            topic=page_html.find('div', {'class': "Hero_course-category-breadcrumb__2-9JD"}).find_all('a')[0].text
            return topic
        except Exception as e:
            return 'Not Found'

    def get_sub_topic(self, page_html):
        '''
        Method Name: get_sub_topic
        Description: Extracts sub topic from HTML page
        Output: sub_topic (type: str)
        On Failure: 'Not Found'

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            sub_topic=page_html.find('div', {'class': "Hero_course-category-breadcrumb__2-9JD"}).find_all('a')[1].text
            return sub_topic
        except Exception as e:
            return 'Not Found'

    def get_course_name(self, page_html):
        '''
        Method Name: get_course_name
        Description: Extracts course name from HTML page
        Output: course_name (type: str)
        On Failure: 'Not Found'

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            course_name = page_html.find('h3', {'class': "Hero_course-title__1a-Hg"}).text
            return course_name
        except Exception as e:
            return 'Not Found'

    def get_course_description(self, page_html):
        '''
        Method Name: get_course_description
        Description: Extracts course description from HTML page
        Output: course_description (type: str)
        On Failure: 'Not Found'

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            course_description = page_html.find('div', {'class': "Hero_course-desc__26_LL"}).text
            return  course_description
        except Exception as e:
            return 'Not Found'

    def get_course_features(self,page_html):
        '''
        Method Name: get_course_features
        Description: Extracts course features from HTML page
        Output: course_features (type: list)
        On Failure: ['Not Found']

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            course_features = page_html.find('div', {'class': "CoursePrice_course-features__2qcJp"}).find_all('li')
            course_features = [feature.text for feature in course_features]
            return course_features
        except Exception as e:
            return ['Not Found']

    def get_what_you_will_learn(self,page_html):
        '''
        Method Name: get_what_you_will_learn
        Description: Extracts What you will learn from HTML page
        Output: what_you_will_learn (type: list)
        On Failure: ['Not Found']

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            what_you_will_learn = page_html.find('div', {'class': "CourseLearning_card__WxYAo card"}).find_all('li')
            what_you_will_learn = [item.text for item in what_you_will_learn]
            return what_you_will_learn
        except Exception as e:
            return ['Not Found']

    def get_requirements(self,page_html):
        '''
        Method Name: get_requirements
        Description: Extracts Requirements from HTML page
        Output: requirements (type: list)
        On Failure: ['Not Found']

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            requirements = page_html.find('div', {'class': "CourseRequirement_card__3g7zR requirements card"}).find_all('li')
            requirements = [req.text for req in requirements]
            return requirements
        except Exception as e:
            return ['Not Found']

    def get_course_curriculum(self,page_html):
        '''
        Method Name: get_course_curriculum
        Description: Extracts Course Curriculum from HTML page
        Output: course_curriculum (type: list)
        On Failure: ['Not Found']

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            course_curriculum = page_html.find_all('div', {'class': "CurriculumAndProjects_curriculum-accordion__2pppc CurriculumAndProjects_card__7HqQx card"})
            course_curriculum = [curriculum.div.text for curriculum in course_curriculum]
            return course_curriculum
        except Exception as e:
            return ['Not Found']

    def get_instructors(self,page_html):
        '''
        Method Name: get_instructors
        Description: Extracts Instructors from HTML page
        Output: instructors (type: list)
        On Failure: ['Not Found']

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            instructors = page_html.find_all('div', {'class': "InstructorDetails_mentor__2hmG8 InstructorDetails_card__14MoH InstructorDetails_flex__2ePsQ card flex"})
            instructors = [instructor.div.h5.text for instructor in instructors]
            if len(instructors)==0:
                instructors=['Not Found']
            return instructors
        except Exception as e:
            return ['Not Found']

    def get_all_course_info(self, all_course_links):
        '''
        Method Name: get_all_course_info
        Description: Opens every course url, then clicks View More option under Course Curriculum
                     if present else pass, and extracts all information from a course page,
                     afterthat stores in a list
        Output: all_course_info (list of dictionaries)
        On Failure: Exception

        Written By: Sayan Saha
        Version: 1.0
        Revision: None
        '''
        try:
            all_course_info = []
            with webdriver.Chrome(executable_path=self.driver_path, chrome_options=self.chrome_options) as wd:
                for link in all_course_links:
                    wd.get(link)
                    try:
                        view_more = wd.find_element(By.CLASS_NAME, "CurriculumAndProjects_view-more-btn__3ggZL")
                        view_more.click()
                    except:
                        pass
                    page_source = wd.page_source
                    page_html = bs(page_source, "html.parser")
                    topic=self.get_topic(page_html)
                    sub_topic=self.get_sub_topic(page_html)
                    course_name=self.get_course_name(page_html)
                    course_description=self.get_course_description(page_html)
                    course_features=self.get_course_features(page_html)
                    what_you_will_learn=self.get_what_you_will_learn(page_html)
                    requirements=self.get_requirements(page_html)
                    course_curriculum=self.get_course_curriculum(page_html)
                    instructors=self.get_instructors(page_html)
                    course_info = {'topic': topic, 'sub_topic': sub_topic, 'course_name': course_name,
                             'course_description': course_description, 'course_features': course_features,
                             'what_you_will_learn': what_you_will_learn, 'requirements': requirements,
                             'course_curriculum': course_curriculum, 'instructors': instructors,
                            'course_link':link
                             }
                    all_course_info.append(course_info)
            return all_course_info
        except Exception  as e:
            raise e