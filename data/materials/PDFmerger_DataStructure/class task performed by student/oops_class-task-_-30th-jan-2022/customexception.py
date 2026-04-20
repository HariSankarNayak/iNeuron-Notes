import logging

logging.basicConfig(filename = "customexception.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )

class customexception(Exception):
   
    def __init__(self,message, count) -> None:
        self.message =  message
        self.count =  count
    
    

class calcualte():
    
    def __init__(self,nooferror) -> None:
        self.nooferrormessage =  nooferror
        
    def nooferrorhappen(self):
        try:
            if self.nooferrormessage > 5 :
                logging.error("System have more error")
                raise(customexception("System  have more exception , count as  %s", self.nooferrormessage ))
            else:
                logging.error("System Working good")
                raise(customexception("System  working good, No of error is %s ", self.nooferrormessage ))
        except customexception as c:
            logging.error("System have more error")
            logging.exception("Number of error available %s ",self.nooferrormessage)  

class senddetails(calcualte):
    c  = calcualte(6)
    c.nooferrorhappen()

