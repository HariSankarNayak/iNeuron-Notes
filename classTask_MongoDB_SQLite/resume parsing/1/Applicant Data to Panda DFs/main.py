import pandas as pd
import os
import re
import docx
import PyPDF2
from striprtf.striprtf import rtf_to_text

class PatternSearcher():
    
    def __init__(self, src):
        self.src = src
        
    def find_email(self):
        pattern = re.compile('[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}')
        return re.search(pattern, self.src).group()
    
    def find_linkedin(self):
        pattern = re.compile('www.linkedin.com/in/[a-zA-Z-]+[a-z0-9]+')
        return re.search(pattern, self.src).group()
    
    def find_git(self):
        pattern = re.compile('github.com/[a-zA-Z0-9]+')
        return re.search(pattern, self.src).group()
        
for root_folder, sub_folders, files in os.walk('./same-resume-year-wise-master'):
    df = pd.DataFrame({'resume_name': files})
    df.set_index('resume_name', inplace = True)
    emails = []
    linkedin = []
    git = []
    for file in files:
        doc_str = ''
        if file.split('.')[1] == 'docx' or file.split('.')[1] == 'doc':
            docObj = docx.Document('./same-resume-year-wise-master/'+file)
            for para in docObj.paragraphs:
                doc_str += para.text
            buff_obj = PatternSearcher(doc_str)
            emails.append(buff_obj.find_email())
            linkedin.append(buff_obj.find_linkedin())
            git.append(buff_obj.find_git())
        else if file.split('.')[1] == 'pdf':
            f = open('./same-resume-year-wise-master/'+file, 'rb')
            pdfread = PyPDF2.PdfFileReader(f)
            for _ in range(pdfread.numPages):
                buff_pdfpage = pdfread.getPage(_)
                doc_str += buff_pdfpage.extractText
            buff_obj = PatternSearcher(doc_str)
            emails.append(buff_obj.find_email())
            linkedin.append(buff_obj.find_linkedin())
            git.append(buff_obj.find_git())
        else if file.split('.')[1] == 'rtf':
            f = open('./same-resume-year-wise-master/'+file)
            content = f.read()
            docstr += rtf_to_text(content)
            buff_obj = PatternSearcher(doc_str)
            emails.append(buff_obj.find_email())
            linkedin.append(buff_obj.find_linkedin())
            git.append(buff_obj.find_git())
        else:
            print("There is a wrong file format, I can't read")
            print(file.split('.')[1])
            
df.insert(1, "git id", git)
df.insert(1, "linkedIn id", linkedin)
df.insert(1, "email id", emails)
