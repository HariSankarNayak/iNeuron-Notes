# importing required packages
import json
import time
import random
import string
import sqlite3
import requests
from datetime import date
from googlesearch import search
from bs4 import BeautifulSoup as bs


# helper function to get urls
def get_url(route, page_type='course'):
    base_url = 'https://courses.ineuron.ai/'
    if page_type == 'category':
        base_url += 'category/'
    page_url = base_url + route.replace(' ', '-')
    return page_url


# helper function to get script tag data
def get_script_data(page, category_type='course'):
    page_url = get_url(page, page_type=category_type)
    response = requests.get(page_url)
    soup = bs(response.text, 'html.parser')
    return [script.contents for script in soup.find_all('script') if len(script) > 0]


# helper function to get course categories data
def get_course_categories_data(selected_category_name):
    # get script data and load as json string
    script_data = get_script_data(selected_category_name, category_type='category')
    json_data = json.loads(''.join(script_data[0]))

    # get categories details
    categories_keys = json_data['props']['pageProps']['initialState']['init']['categories'].keys()
    categories = json_data['props']['pageProps']['initialState']['init']['categories']

    # get sub-categories details
    category_data = []
    category_counter = 1
    for category_key in categories_keys:
        category_name = categories[category_key]['title']
        new_entry = {'category-number': category_counter, 'course-category': category_name,
                     'course-sub-category': [], 'course-category-url': get_url(category_name, page_type='category'),
                     'course-sub-category-url': []}
        for sub_category_key in list(categories[category_key]['subCategories'].keys()):
            sub_topic_name = categories[category_key]['subCategories'][sub_category_key]['title']
            new_entry['course-sub-category'].append(sub_topic_name)
            new_entry['course-sub-category-url'].append(get_url(sub_topic_name, page_type='category'))
        category_data.append(new_entry)
        category_counter += 1

    return category_data


# helper function to get course details
def get_courses_detail_data(selected_category_name):
    # get script data and load as json string
    script_data = get_script_data('Data Science', category_type='category')
    json_data = json.loads(''.join(script_data[0]))

    # data container for course data
    courses_data = []

    # get courses details
    bundle_name = 'NA'
    for course, course_details in json_data['props']['pageProps']['initialState']['init']['courses'].items():
        if 'courseInOneNeuron' in course_details.keys():
            bundle_name = course_details['courseInOneNeuron']['bundleName']

        if 'pricing' in course_details.keys():
            if course_details['pricing']['isFree']:
                courses_data.append({'course-name': course, 'course-price-inr': 'Free', 'course-price-usd': 'Free',
                                     'bundle-name': bundle_name})
            else:
                inr_price = course_details['pricing']['IN']
                usd_price = course_details['pricing']['US']
                courses_data.append(
                    {'course-name': course, 'course-price-inr': inr_price, 'course-price-usd': usd_price,
                     'bundle-name': bundle_name})

    tech_neuron_course_counter = 0
    kids_neuron_course_counter = 0
    tech_neuron_free_course_counter = 0
    kids_neuron_free_course_counter = 0
    for data in courses_data:
        # count total tech neuron courses
        if data['bundle-name'] == 'Tech Neuron':
            tech_neuron_course_counter += 1
            # count free courses
            if data['course-price-inr'] == 'Free':
                tech_neuron_free_course_counter += 1

        # count total kids neuron courses
        if data['bundle-name'] == 'Kids Neuron':
            kids_neuron_course_counter += 1
            # count free courses
            if data['course-price-inr'] == 'Free':
                kids_neuron_free_course_counter += 1

    return courses_data, tech_neuron_course_counter, kids_neuron_course_counter, tech_neuron_free_course_counter, \
           kids_neuron_free_course_counter


# helper function to get course data
def get_course_data(selected_course_name):
    # get script data and load as json string
    script_data = get_script_data(selected_course_name)
    json_data = json.loads(''.join(script_data[0]))

    # course name
    course_name = json_data['props']['pageProps']['data']['details']['seo']['keywords']

    # course description
    course_description = json_data['props']['pageProps']['data']['details']['description']

    # what you'll learn
    course_learnings = json_data['props']['pageProps']['data']['meta']['overview']['learn']

    # requirements
    course_requirements = json_data['props']['pageProps']['data']['meta']['overview']['requirements']

    # course features
    course_features = json_data['props']['pageProps']['data']['meta']['overview']['features']

    # course price
    course_details = json_data['props']['pageProps']['data']['details']
    if 'pricing' in course_details.keys():
        if 'IN' in course_details['pricing'].keys():
            course_price = course_details['pricing']['IN']
        else:
            course_price = 0
    else:
        course_price = 0

    topic_data = []
    topic_keys = json_data['props']['pageProps']['data']['meta']['curriculum'].keys()
    for topic_key in topic_keys:
        curriculum = json_data['props']['pageProps']['data']['meta']['curriculum'][topic_key]
        course_title = curriculum['title']
        new_entry = {'topic-name': course_title}
        sub_topics = []
        for item in curriculum['items']:
            sub_topics.append(item['title'])
        new_entry['sub-topic'] = sub_topics
        topic_data.append(new_entry)

    course_data = [{'course-name': str.title(course_name), 'course-description': course_description,
                    'course-learnings': course_learnings, 'course-features': course_features,
                    'course-requirements': course_requirements, 'topic-data': topic_data,
                    'course-price': course_price}]
    return course_data


# helper function create search query
def get_search_query(course_name):
    query = []
    ignore_words_list = ['bootcamp']
    course_name_words = course_name.lower().split(' ')
    for course_name_word in course_name_words:
        if course_name_word not in ignore_words_list:
            query.append(course_name_word)
    return ' '.join(query)


# helper function to get course name
def get_similar_course_name(course_url):
    course_details = [word for word in course_url.replace("//", "#").split("/") if word != '']
    course_details = [word.replace("#", "//") for word in course_details]
    if len(course_details) > 2:
        course_name = ' - '.join([str.title(word.replace('-', ' ')) for word in course_details[1:]])
        return {'course-url': course_url, 'course-base-url': course_details[0], 'course-name': course_name}
    else:
        course_name = ''
        if len(course_details) == 1:
            course_name = course_details[0].split("//")[1].replace('.', ' ')
        return {'course-url': course_url, 'course-base-url': course_details[0],
                'course-name': str.title(course_name)}


# helper function to find out similar content
def get_similar_content(query, num_results=10):
    similar_courses = []
    for search_results in search(query, num_results=num_results):
        similar_courses.append(get_similar_course_name(search_results))
    return similar_courses


# helper function to get website html data
def get_html(site_url):
    return bs(requests.get(site_url).text, 'html.parser')


# helper function to find data in html
def find_tag_data(site_html, tag, tag_type, tag_value, find_all=False):
    return site_html.find(tag, {tag_type: tag_value}) if not find_all else site_html.findAll(tag, {tag_type: tag_value})


# helper function to search on Google
def search_on_google(query, num_results=10):
    return list(search(query, num_results=num_results))


# scrape coursera website data
def scrape_coursera_pages(page_url):
    # get coursera page html
    coursera_html = get_html(page_url)

    # get course name
    course_name = find_tag_data(coursera_html, 'h2', 'class', '_1f1t6bn').text

    # course description
    course_description = find_tag_data(coursera_html, 'div', 'class', 'content-inner').text

    # course rating
    course_ratings = find_tag_data(coursera_html, 'span', 'class', '_16ni8zai').text.split('st')[0] + '/5'

    # course reviews count
    course_reviews_count = find_tag_data(coursera_html, 'div', 'class', '_wmgtrl9').text.split(' ')[0]

    # course enrollments count
    course_enrollments_count = find_tag_data(coursera_html, 'div', 'class', '_1fpiay2').text.split(' ')[0]

    # course syllabus
    course_syllabus = [course.text for course in
                       find_tag_data(coursera_html, 'h2', 'class', 'headline-2-text', find_all=True)]

    # get coursera review page html
    coursera_user_reviews_html = get_html(page_url + '/reviews')

    # get user reviews
    course_user_reviews = [review.text for review in
                           find_tag_data(coursera_user_reviews_html, 'p', 'class', 'top-review_comment', find_all=True)]
    for review in find_tag_data(coursera_user_reviews_html, 'div', 'class', 'rc-CML', find_all=True):
        course_user_reviews.append(review.div.p.text)

    return {'course-name': course_name, 'course-description': course_description, 'course-ratings': course_ratings,
            'course-reviews-count': course_reviews_count, 'course-enrollments-count': course_enrollments_count,
            'course-syllabus': course_syllabus, 'course-reviews': course_user_reviews}


def insert_scrapped_data_for_course(scraped_data, db_name='scrapped-data.db', db_type='sqlite'):
    if db_type == 'sqlite':
        connection = sqlite3.connect(db_name)

        # create curser
        cursor = connection.cursor()
        create_table_query = """ CREATE TABLE IF NOT EXISTS SCRAPPED_DATA_COURSE (
                                    RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    COURSE_DATA TEXT NOT NULL,
                                    SIMILAR_CONTENT TEXT NOT NULL,
                                    TIMESTAMP TEXT NOT NULL
                                 );"""

        cursor.execute(create_table_query)

        # insert record
        cursor.execute('INSERT INTO SCRAPPED_DATA_COURSE (COURSE_DATA, SIMILAR_CONTENT, TIMESTAMP) VALUES(?, ?, ?)',
                       scraped_data)
        connection.commit()
        connection.close()


def insert_scrapped_data_for_courses_details(scraped_data, db_name='scrapped-data.db', db_type='sqlite'):
    if db_type == 'sqlite':
        connection = sqlite3.connect(db_name)

        # create curser
        cursor = connection.cursor()
        create_table_query = """ CREATE TABLE IF NOT EXISTS SCRAPPED_DATA_COURSES (
                                    RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    COURSES_DETAILS TEXT NOT NULL,
                                    TECH_NEURON_COURSE_COUNT TEXT NOT NULL,
                                    KIDS_NEURON_COURSE_COUNT TEXT NOT NULL,
                                    TIMESTAMP TEXT NOT NULL
                                 );"""

        cursor.execute(create_table_query)

        # insert record
        cursor.execute('INSERT INTO SCRAPPED_DATA_COURSES (COURSES_DETAILS, TECH_NEURON_COURSE_COUNT, \
                            KIDS_NEURON_COURSE_COUNT, TIMESTAMP) VALUES(?, ?, ?, ?)', scraped_data)
        connection.commit()
        connection.close()


def insert_scrapped_data_for_course_categories(scraped_data, db_name='scrapped-data.db', db_type='sqlite'):
    if db_type == 'sqlite':
        connection = sqlite3.connect(db_name)

        # create curser
        cursor = connection.cursor()
        create_table_query = """ CREATE TABLE IF NOT EXISTS SCRAPPED_DATA_COURSE_CATEGORIES (
                                    RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    COURSE_CATEGORIES TEXT NOT NULL,
                                    TIMESTAMP TEXT NOT NULL
                                 );"""

        cursor.execute(create_table_query)

        # insert record
        cursor.execute('INSERT INTO SCRAPPED_DATA_COURSE_CATEGORIES (COURSE_CATEGORIES, TIMESTAMP) \
                            VALUES(?, ?)', scraped_data)
        connection.commit()
        connection.close()


def log_user_activity(activity_data, db_name='scrapped-data.db', db_type='sqlite'):
    if db_type == 'sqlite':
        # make connection with database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # create table if not exists
        create_table_query = """ CREATE TABLE IF NOT EXISTS USER_ACTIVITY (
                                            RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            ACTIVITY TEXT NOT NULL,
                                            TIMESTAMP TEXT NOT NULL
                                         );"""
        cursor.execute(create_table_query)

        # insert record
        cursor.execute('INSERT INTO USER_ACTIVITY (ACTIVITY, TIMESTAMP) VALUES(?, ?)', activity_data)
        connection.commit()
        connection.close()


def get_timestamp():
    # get current date and time - timestamp
    return date.today().strftime("%B %d, %Y") + ' ' + time.strftime("%H:%M:%S", time.localtime())


def get_indeed_job_data():
    indeed_html = get_html('https://in.indeed.com/jobs?q=Machine%20Learning')
    website_name = str(indeed_html.find('title')).replace("/", "").split('<title>')[1].split('|')[1].strip(' ')
    job_details = str(indeed_html.find('title')).replace("/", "").split('<title>')[1].split('|')[0].strip(' ')
    job_title_info = [data.replace('<', '').split('>')[1] for sublist in [str(job).replace("/", "").split('span')[1:]
                                                                          for job in
                                                                          find_tag_data(indeed_html, 'h2', 'class',
                                                                                        'jobTitle', find_all=True)]
                      for data in sublist if 'title' in data]
    return {'website-name': website_name, 'job-details': job_details, 'job-title-info': job_title_info}
