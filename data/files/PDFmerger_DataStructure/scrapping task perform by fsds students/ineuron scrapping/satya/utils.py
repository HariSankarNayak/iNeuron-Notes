import string
import random

class utilityFunctions:

    def getUsernameforMongoDB(self):
        username = "mongo"
        return username

    def getPasswordforMongoDB(self):
        password = "mongo"
        return password

    def getIneuronUrl(self):
        ineuron_url = "https://courses.ineuron.ai/"
        return ineuron_url

    def getCourseKeys(self):
        keys = "['props']['pageProps']['initialState']['filter']['initCourses']"
        return keys

    def generateUniqueIdsForUI(self, size):
        chars = string.ascii_uppercase + string.digits
        unique_id = ''.join(random.choice(chars) for x in range(size))
        return unique_id

    def getWhatYouWillLearn(self):
        what_will_learn_class = {"class": "CourseLearning_card__WxYAo card"}
        return what_will_learn_class

    def getRequirements(self):
        requirement_class = {"class": "CourseRequirement_card__3g7zR requirements card"}
        return requirement_class

    def getCourseFeatures(self):
        features_class = {"class": "CoursePrice_course-features__2qcJp"}
        return features_class

    def getCourseTitle(self):
        course_title = {"class": "Hero_course-title__1a-Hg"}
        return course_title

    def getCourseDescription(self):
        description = {"class": "Hero_course-desc__26_LL"}
        return description

    def getCourseFees(self):
        fees_div  = {"class": "CoursePrice_dis-price__3xw3G"}
        return fees_div

    def getClassTimings(self):
        timing_class  ={"class": "CoursePrice_time__1I6dT"}
        return timing_class

    def getMentorsName(self):
        mentors_class = {"class": "InstructorDetails_left__3jo8Z"}
        return mentors_class

    def getCurriculumList(self):
        curriculum_cards =  {"class": "CurriculumAndProjects_curriculum-accordion__2pppc CurriculumAndProjects_card__7HqQx card"}
        return curriculum_cards

    def getCurriculumCard(self):
        curriculum_single_card =  {"class": {"CurriculumAndProjects_accordion-header__3ALRY CurriculumAndProjects_flex__1-ljx flex"}}
        return curriculum_single_card