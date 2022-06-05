from email import message
import logging

logging.basicConfig(filename = "polimor.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )
class customexception(Exception):
   
    def __init__(self,message, count) -> None:
        self.message =  message
        self.count =  count
    
class avatharam():
   
    def __init__(self,message) -> None:
        self.message1 =  message
        # self.message2 = message2

    def attitudechange(self,message):
        self.message = message
        logging.error("character change to %s", self.message1 + self.message)
        return self.message1 + self.message

class changecharacter(avatharam):
    
  
    def changeas(self,level):
        self.level = level
        try:
            c = avatharam("I am very ")
            if self.level < 5 :
                c.attitudechange("Good")
                logging.info("Normal person")
            if self.level > 5 :
                c.attitudechange("Bad")
                logging.info("Bad person")
            else:
                c.attitudechange("Normal person")
                logging.info("Normal person")
        except customexception as c:
            logging.error("System have more error")
            logging.exception("Number of error available %s ",self.nooferrormessage)  

class sendthelevel(changecharacter):
    c  = changecharacter("I am very ")
    c.changeas(5)

