from Browser_logger import *
def getpath(pathname):
    '''
    This function will return the list of files and directories in the given path
    to the calling module
    '''
    writelogs('getpath','info','Entered into getpath')
    try:

        path=pathname
        lst_dir=fetchlist(path)
        return lst_dir
    except Exception as e:
        writelogs('getpath','error','Error occurred while listing files and directories')
        writelogs('getpath','exception',e)
    else:
        writelogs('getpath','info','Getting the list of files and directories is successful')


def fetchlist(path1):
    '''
    This function will find the list of files and directories in the given path
    '''
    writelogs('fetchlist','info','Entered into getlist')
    try:
        import os
        lst = os.walk(top=str(path1))
        l1 = []

        for i in list(lst):
            l1.append("Direcotory Path: " + i[0])
            l1.append("Files :")
            l1.append(i[2])
            l1.append("Folders:")
            l1.append(i[1])
            l1.append("*****************************************************************")
        return l1
    except Exceptin as e:
        writelogs('fetchlist', 'error', 'Error occurred while listing files and directories')
        writelogs('fetchlist', 'exception', e)
