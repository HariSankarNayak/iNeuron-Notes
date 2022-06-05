# Create a class for Dictoinary functions

import logging
logging.basicConfig(filename="LoggingInformation_List.log", level=logging.DEBUG)
logging.basicConfig(filename="LoggingInformation_List.log", level=logging.INFO)
logging.basicConfig(filename="LoggingInformation_List.log", level=logging.WARNING)
logging.basicConfig(filename="LoggingInformation_List.log", level=logging.ERROR)

class ListFunctions:
    def __init__(self,lst,*args):
        if type(lst) ==list:
            self.lst=lst
            self.index=args
            self.val=args
        else :
            logging.error("Input is not a list")
            logging.shutdown()
            raise Exception("Input is not a list")
    def mylistLength(self):
        try:
            return len(self.lst)  
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistCopy(self):
        try:
            l=self.lst.copy()
            return (l)
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistInsert(self,index,val):
        try:
            l=[]
            l=self.lst
            l.insert(index,val)
            return l
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    def mylistPop(self,index):
        try:
            self.lst.pop(index)
            return self.lst
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistAppend(self,lst):
        try:
            l=[]
            l=self.lst
            l.append(lst)
            self.lst=l
            return self.lst
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistCount(self,val):
        try:
            count=0
            for i in self.lst:
                if i == val:
                    count=count+1
            return count
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistClear(self):
        try:
            l=[]
            self.lst=l
            return self.lst
        except Exception as e:
            logging.exception("exception occured "+str(e))
            logging.shutdown()
    
    def mylistExtend(self,newlst):
        try:
            self.lst=self.lst+newlst
            return self.lst
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistIndex(self,val):
        try:
            count=0
            for i in self.lst:
                if i != val:
                    count=count+1
                else:
                    break
            return count
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()

    def mylistRemove(self,val):
        try:
            self.lst.remove(val)
            return self.lst
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistReverse(self):
        try:
            return self.lst[::-1]
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mylistSort(self):
        try:
            self.lst.sort()
            return self.lst
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()