# Create a class for Dictoinary functions

import logging
logging.basicConfig(filename="LoggingInformation_Dict.log", level=logging.DEBUG)
logging.basicConfig(filename="LoggingInformation_Dict.log", level=logging.INFO)
logging.basicConfig(filename="LoggingInformation_Dict.log", level=logging.WARNING)
logging.basicConfig(filename="LoggingInformation_Dict.log", level=logging.ERROR)

class DictFunc:
    def __init__(self,d,*args):
        if type(d) ==dict:
            self.d=d
            self.iterable=args
            self.val=args
        else :
            logging.error("Input is not a dictionary")
            logging.shutdown()
            raise Exception("Input is not a dictionary")
            #return
        
    def mydictkeys(self):
        try:
            return list[self.d.keys()]
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictitems(self):
        try:
            return self.d.items()
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictclear(self):
        try:
            return self.d.clear()
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictcopy(self):
        try:
            d2={}
            d2=self.d.copy()
            return d2
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictfromkeys(self,iterable,val):
        try:
            locald={}
            locald=self.d.fromkeys(iterable,val)
            return locald
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictget(self,key):
        try:
            return self.d.get(key)
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()

    def mydictpop(self,key):
        try:
            return self.d.pop(key)
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
      
    def mydictpopitem(self,key):
        try:
            return self.d.popitem()
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def myDictSetDefault(self,key):  
        try:
            self.d.setdefault(key)
            return (self.d)
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
    
    def mydictvalues(self):
        try:
            return self.d.values()
        except Exception as e:
            logging.exception("exception occured"+str(e))
            logging.shutdown()
