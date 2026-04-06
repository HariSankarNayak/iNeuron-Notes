from flask import Flask,jsonify,request,render_template
from bs4 import BeautifulSoup as bs
import requests
from flask_cors import CORS,cross_origin
from urllib.request import urlopen as uReq
import json
import logging as logger
from Databases.db import DatabaseOpr

logger.basicConfig(filename='./Log/app_logs.log', level=logger.INFO, format=f'%(asctime)s - %(levelname)s - %(message)s')




class webParser:
    def __init__(self):
        self.base_URl = "https://courses.ineuron.ai/"
        self.dbObj = DatabaseOpr()


    def courseScaper(self):
        """Scaper for course list page"""
        try:
            uclint = uReq( self.base_URl)
            inueronHome = uclint.read()
            uclint.close()

            inueronHome_Html = bs(inueronHome, "html.parser")
            courseListBox = inueronHome_Html.find_all("script", {"id": "__NEXT_DATA__"})

            res = str(courseListBox[0].string)
            res_dist = json.loads(res)

            courseList = res_dist["props"]["pageProps"]["initialState"]["init"]["courses"]

            course_detail_lst = []
            for key in courseList.keys():
                url_slug = self.base_URl+"-".join(str(key).split(" "))
                courseList[key]["url_slug"] = url_slug
                courseList[key]["course_name"] = key

                checkCourseExist = self.dbObj.findCourseName(key)
                if checkCourseExist == 0:
                    course_detail_lst.append(courseList[key])

            #logger.info(json.dumps(course_detail_lst))

            """try:
                with open("../sample.json", "w") as outfile:
                    outfile.write(json.dumps(courseList))
            except Exception as e:
                logger.exception("Error occured while saving json in file:====>  " + str(e))"""

            #insert data into collections
            if len(course_detail_lst) > 0:
                self.dbObj.insertCourseInfo(course_detail_lst)
            else:
                return "Everything is already Scraped!"

        except Exception as e:
            logger.exception("Error occured while parsing:====>  "+str(e))

    def courseDetailScaper(self,cDetails):
        """Scaper for course detail page"""
        try:
            for item in cDetails:


                slug = item["url_slug"].split("/")[-1]
                logger.info(slug)
                checkRes = self.dbObj.findIndivisualCourse(slug)
                if checkRes == 1:
                    continue
                else:
                    c_url = item["url_slug"]
                    uclint = uReq(c_url)

                    inueronCourseDetails = uclint.read()
                    uclint.close()

                    inueronCourseDetails_Html = bs(inueronCourseDetails, "html.parser")
                    courseListBox = inueronCourseDetails_Html.find_all("script", {"id": "__NEXT_DATA__"})


                    res = str(courseListBox[0].string)
                    res_dist = json.loads(res)

                    """checkRes = self.dbObj.findIndivisualCourse(slug)
                    if checkRes == 0:"""
                    insert_id = self.dbObj.insertCourseIndividuals(res_dist)
                    logger.info(insert_id)


        except Exception as e:
            logger.exception("Error occured while parsing:====>  " + str(e))

    def getCourse_Details(self):
        """get all course list"""
        return self.dbObj.getCourseDetails()

    def getCourse_DetailsWithCourseName(self,c_name):
        """get all course detail based on it's name"""
        return self.dbObj.courseNameDetails(c_name)