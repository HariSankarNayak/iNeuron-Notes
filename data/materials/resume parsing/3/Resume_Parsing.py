#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Read all the resume form ineurno git in pdf , word , and try to create a dataframe with resume name as a index value , and
in column i am expecting email id , linked in id , git id  , sills as a result . '''


# In[2]:


import logging
logging.basicConfig(filename = "task_regex.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )


# In[3]:


try:
    import re
    import pandas as pd
    import numpy as np
    import docx2txt
    from docx import Document
    import os
    import PyPDF2
    logging.info("required libraries imported")
except Exception as e:
    logging.error("Error occurred while importing libraries")
    logging.exception("Exception while importing libraries"+str(e))


# In[4]:


try:
    dict1={}
    logging.info("creating a dictionary to be later converte into dataframe")
except Exception as e:
    logging.error("Error occurred while creating a dictionary")
    logging.exception("Exception while creating a dictionary"+str(e))


# In[5]:


'''creating a class find_txt'''
class find_txt:
    logging.info("parent class created")
    
    '''creating constructor'''
    try:
        def __init__(self,file_name):
            self.file_name = file_name
            logging.info("initializing contructor")
    except Exception as e:
        logging.error("Error occured while defining constructor")
        loggin.exception("Exception while defining constructor"+str(e))

        
    '''defining a fucntion to read pdf file'''    
    def find_in_pdf(self):
        a = PyPDF2.PdfFileReader(self.file_name)
        page_num=a.numPages
        fl_txt= ""
        for i in range(0,page_num):
            fl_txt += a.getPage(i).extractText()
            with open("pdf_tx1.txt","w",encoding='utf-8') as f:
                f.write(fl_txt)
        try:
            '''finding the email, linkedin id, guthub id using regular expression'''
            pattern_linkedin = re.findall("www.linkedin.com/[\w]{2,3}/[\w]{2,20}",fl_txt)
            pattern_email = re.findall(r'[\w.%_+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}',fl_txt)
            pattern_github = re.findall("github.com/[\w]{2,20}",fl_txt)
            logging.info("finding pattern in file ")
        except Exception as e:
            logging.error("Error occurred while finding a pattern in file ")
            logging.exception("Exception while finding a pattern in the file"+str(e))

        '''creating a dummy dictionary which will be used as nested dictionary'''
        dict_sub={'email':'NA','linkedin':'NA','Github':'NA'}

        if pattern_email:
            dict_sub['email']=pattern_email[0]
        if pattern_linkedin:
            dict_sub['linkedin']=pattern_linkedin[0]
        if pattern_github:
            dict_sub['Github']=pattern_github[0]


        try:
            dict1[os.path.basename(self.file_name)]=dict_sub
            logging.info("writing the pattern into main dictionary")
        except Exception as e:
            logging.error("Error occurred while writing the dictionary ")
            logging.exception("Exception while fwriting the dictionary"+str(e))
            
    '''defining a fucntion to read docx file'''    
    def find_in_docx(self):
        file1_text = docx2txt.process(self.file_name)
        pattern_linkedin = re.findall("www.linkedin.com/[\w]{2,3}/[\w]{2,20}",file1_text)
        pattern_email = re.findall(r'[\w.%_+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}',file1_text)
        pattern_github = re.findall("github.com/[\w]{2,20}",file1_text)
        dict_sub={}
        dict_sub={'email':'NA','linkedin':'NA','Github':'NA'}
        if pattern_email:
            dict_sub['email']=pattern_email[0]
        if pattern_linkedin:
            dict_sub['linkedin']=pattern_linkedin[0]
        if pattern_github:
            dict_sub['Github']=pattern_github[0]
        
        try:
            dict1[os.path.basename(self.file_name)]=dict_sub
            logging.info("writing the pattern into main dictionary")
        except Exception as e:
            logging.error("Error occurred while writing the dictionary ")
            logging.exception("Exception while fwriting the dictionary"+str(e))


# In[6]:


class_inst = find_txt("C:\\Users\\neeti\\Downloads\\4+.docx")
class_inst.find_in_docx()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\8+.docx")
class_inst.find_in_docx()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\3+.docx")
class_inst.find_in_docx()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\3+ (2).docx")
class_inst.find_in_docx()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\12+.docx")
class_inst.find_in_docx()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\12+ (2).docx")
class_inst.find_in_docx()


# In[7]:


class_inst = find_txt("C:\\Users\\neeti\\Downloads\\15+.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\mteh fresher.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\freasher .pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\8+.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\6+.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\5+.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\5+ .pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\3+.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\20.pdf")
class_inst.find_in_pdf()
class_inst = find_txt("C:\\Users\\neeti\\Downloads\\15+ (1).pdf")
class_inst.find_in_pdf()


# In[8]:


pd.DataFrame.from_dict(dict1,orient='index')


# In[ ]:




