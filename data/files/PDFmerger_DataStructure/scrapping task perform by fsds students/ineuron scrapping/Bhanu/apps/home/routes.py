# import required packages
import time
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.home.util import (get_courses_detail_data, get_course_categories_data, get_course_data, get_similar_content,
                            get_search_query, scrape_coursera_pages, insert_scrapped_data_for_course,
                            insert_scrapped_data_for_courses_details, insert_scrapped_data_for_course_categories,
                            log_user_activity, get_timestamp, get_indeed_job_data)

from apps import db
from apps.home.models import ScrappedDataCourses, ScrappedDataCourse


@blueprint.route('/index')
@login_required
def index():
    # log user activity
    # user_activity = 'navigated to applications home/landing page'
    # log_user_activity([user_activity, get_timestamp()])

    # get course data
    courses_details, tech_count, kids_count, tech_free, kids_free = get_courses_detail_data('Data Science')
    tech_neuron_percentage = int(round((int(tech_count) / len(courses_details)) * 100, 0))
    kids_neuron_percentage = int(round((int(kids_count) / len(courses_details)) * 100, 0))

    # insert courses data
    insert_scrapped_data_for_courses_details([str(courses_details), str(tech_neuron_percentage),
                                              str(kids_neuron_percentage), get_timestamp()])

    # get course category data
    course_categories = get_course_categories_data('Data Science')

    # enter select feature data to db
    for course_data in course_categories:
        db_entry = ScrappedDataCourses(
            course_categories=course_data['course-category'],
            course_sub_categories=', '.join(course_data['course-sub-category']),
            tech_neuron_course_count=tech_count,
            kids_neuron_course_count=kids_count
        )
        db.session.add(db_entry)
        db.session.commit()

    # insert courses category data
    insert_scrapped_data_for_course_categories([str(course_categories), get_timestamp()])

    # render index.html with fetch (scrapped) data
    return render_template('home/index.html', segment='index', categories_count=len(course_categories),
                           courses_count=len(courses_details), course_categories=course_categories,
                           courses_details=courses_details, tech_neuron_count=tech_count, zip=zip,
                           tech_neuron_percentage=tech_neuron_percentage, kids_neuron_count=kids_count,
                           kids_neuron_percentage=kids_neuron_percentage, tech_free=tech_free, kids_free=kids_free)


@blueprint.route('/<template>/<string:course>')
@login_required
def route_template(template, course):
    # log user activity
    # user_activity = f'opened {template} page for course {course}'
    # log_user_activity([user_activity, get_timestamp()])

    try:
        if not template.endswith('.html'):
            template += '.html'

        # detect the current page
        segment = get_segment(request)

        # get selected course data
        course_data = get_course_data(course)
        print(course_data)

        # get similar content data
        similar_content = get_similar_content(get_search_query(course), num_results=5)

        # enter select feature data to db
        db_entry = ScrappedDataCourse(
            course_name=course_data[0]['course-name'],
            course_features=', '.join(course_data[0]['course-features']),
            course_fee=course_data[0]['course-price'],
            similar_content=', '.join([content['course-url'] for content in similar_content])
        )
        db.session.add(db_entry)
        db.session.commit()

        # insert course data to database
        insert_scrapped_data_for_course([str(course_data), str(similar_content), get_timestamp()])

        # course url
        course_url = 'https://courses.ineuron.ai/' + course.replace(' ', '-')

        # render course.html with fetch (scrapped) data
        return render_template("home/" + template, segment=segment, course_data=course_data[0],
                               similar_content_count=len(similar_content), similar_content=similar_content,
                               timestamp=get_timestamp(), course_url=course_url)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


# helper - extract current page name from request
def get_segment(app_request):
    try:
        segment = app_request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None


@blueprint.route('/coursera')
def coursera():
    # log user activity
    # user_activity = 'opened applications coursera page'
    # log_user_activity([user_activity, get_timestamp()])

    # define site url
    site_url = 'https://www.coursera.org/learn/machine-learning'

    # scrape coursera website data
    coursera_data = scrape_coursera_pages(site_url)

    # render analysis.html with fetch (scrapped) data
    return render_template("home/coursera.html", segment='coursera', coursera_data=coursera_data,
                           timestamp=get_timestamp(), site_url=site_url)


@blueprint.route('/analysis')
def analysis():
    # log user activity
    # user_activity = 'opened applications analysis page'
    # log_user_activity([user_activity, get_timestamp()])

    # render analysis.html with fetch (scrapped) data
    return render_template("home/analysis.html", segment='analysis')


@blueprint.route('/settings')
def settings():
    # log user activity
    # user_activity = 'opened applications settings page'
    # log_user_activity([user_activity, get_timestamp()])

    # render analysis.html with fetch (scrapped) data
    return render_template("home/settings.html", segment='settings')


@blueprint.route('/jobs')
def jobs():
    indeed_portal_data = get_indeed_job_data()

    # render analysis.html with fetch (scrapped) data
    return render_template("home/jobs.html", segment='jobs', indeed_portal_data=indeed_portal_data)


@blueprint.route('/data')
def data():
    # get all the data
    db_entries_course = ScrappedDataCourse.query.all()
    db_entries_courses = ScrappedDataCourses.query.all()
    print(db_entries_course)

    # render analysis.html with fetch (scrapped) data
    return render_template("home/data.html", segment='data')


@blueprint.route('/offers')
def offers():
    # render analysis.html with fetch (scrapped) data
    return render_template("home/offers.html", segment='offers')
