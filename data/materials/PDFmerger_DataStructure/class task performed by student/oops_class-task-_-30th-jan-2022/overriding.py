import logging

logging.basicConfig(filename = "overriding.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )

class parent:
    
    def numberofcoco(self):
        """This is the method used to provide coco by parent"""
        logging.info("parents provide %s cacolate",500)  
        print("parent")  
        return "500"

    def aditionalcoco():
        print("Planning to add more coco")    




class child(parent):
    
    def numberofcoco(self):
        logging.info("In child function")
        return "1000"

f = parent()
fc = f.numberofcoco()
logging.info("Number of cacolate child get from parent is %s",fc)  

