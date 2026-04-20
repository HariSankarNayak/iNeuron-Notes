import requests
import json
from bs4 import BeautifulSoup as bs
from logger import logger


def course_schema(page_data: dict, detailed_data: dict, meta_data: dict, curriculum_data: dict, overview_data: dict):
    course_details = {}
    course_details["Title"] = page_data["title"]
    course_details["Job Guaranteed"] = page_data["isJobGuaranteeProgram"]
    course_details["Description"] = detailed_data["description"]
    course_details["Mode"] = detailed_data["mode"]
    course_details["Pricing"] = detailed_data["pricing"]
    course_details["instructor"] = len(meta_data["instructors"])
    course_details["curriculum"] = []
    for i in curriculum_data:
        course_details["curriculum"].append(curriculum_data[i])
    course_details["learn"] = overview_data["learn"]
    course_details["requirements"] = overview_data["requirements"]
    course_details["features"] = overview_data["features"]
    course_details["language"] = overview_data["language"]
    return course_details


def fetch_course(site_url: str = None, course_name: str = None, *, db_collection: object, full_url: str = None):
    """Scrap course from https://courses.ineuron.ai with specific url. If already existing in database then pass


    Args:
        site_url (str): https://courses.ineuron.ai as input
        course_name (str): coursename from https://courses.ineuron.ai for scrapping
        db_collection (object): collection object
        full_url (str): course url for specific course scrapping
    """
    course_url = full_url if full_url else site_url + "/" + course_name.replace(" ", "-")
    course_name = course_name or full_url.split("/")[-1].replace("-", " ")
    if not db_collection.find_one({"Title": course_name}):
        logger.debug(f"Fetching for {course_name}")
        course_res = requests.get(course_url)
        course_soup = bs(course_res.content, "html.parser")
        course_json = json.loads(course_soup.find("script", src=None).text)
        raw_data_json = course_json["props"]["pageProps"]
        page_data_json = raw_data_json["data"]
        detailed_data_json = page_data_json["details"]
        meta_data_json = page_data_json["meta"]
        curriculum_json = meta_data_json["curriculum"]
        overview_json = meta_data_json["overview"]
        courses = course_schema(page_data_json, detailed_data_json, meta_data_json, curriculum_json, overview_json)
        db_collection.insert_one(courses)
        logger.debug(f"Completed fetching for {course_name}")


def scrap_all(site_url: str, db_collection: object):
    """Scrap all the course from https://courses.ineuron.ai/

    Args:
        site_url (str): https://courses.ineuron.ai as input 
        db_collection (object): collection object
    """
    logger.debug(f"Scrapping all courses")
    ineuron_res = requests.get(site_url)
    ineuron_soup = bs(ineuron_res.content, "html.parser")
    ineuron_script = ineuron_soup.find("script", src=None)
    raw_json = json.loads(ineuron_script.text)
    raw_course = raw_json["props"]["pageProps"]["initialState"]["init"]
    course_names = list(raw_course["courses"].keys())
    for course_name in course_names:
        fetch_course(site_url, course_name, db_collection=db_collection)


def scrap_one(site_url: str, db_collection: object):
    """Scrap one site only

    Args:
        site_url (str): site url from https://courses.ineuron.ai to scrap
        db_collection (object): collection object
    """
    fetch_course(db_collection=db_collection, full_url=site_url)
