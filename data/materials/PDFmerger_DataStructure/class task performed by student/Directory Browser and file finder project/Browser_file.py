from Browser_logger import *
def fetchfile(file_path):
    '''
    This function will help you to filter only pdf file from a directory
    '''
    writelogs('fetchfile','info','Entered into fetchfile')
    try:

        import os
        a = os.walk(file_path)
        l = []
        dir_lst = list(a)

        import re
        pattern = re.compile(r"\.pdf$")
        import PyPDF2 as pdf
        import os
        from os import path

        f_writer = pdf.PdfFileWriter()


        for lst in dir_lst:
            if type(lst) == tuple:
                for dirct in lst:
                    if type(dirct) == list:
                        for file in dirct:
                            matches = pattern.finditer(file)
                            for match in matches:
                                l.append(file)
                                f1 = open(path.join(lst[0],file), 'rb')

                                f1_read = pdf.PdfFileReader(f1)



                                for page_no in range(f1_read.numPages):
                                    f1_pages = f1_read.getPage(page_no)
                                    f_writer.addPage(f1_pages)


        fnew = open("Mergedfile.pdf", 'wb')
        f_writer.write(fnew)
        filename=path.join(os.getcwd(),'Mergedfile.pdf')

        return l,filename

    except Exception as e:
        writelogs('fetchfile','error','Error occurred while fetching .pdf files')
        writelogs('fetchfile','exception',e)
    else:
        writelogs('fetchfile','info','Fetching .pdf files is successfull')

