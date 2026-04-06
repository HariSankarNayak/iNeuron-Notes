import logging

logging.basicConfig(filename = "logs.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )

class grandparents:
   
    def __init__(self,noofcoco) -> None:
        self.numberofchocolate =  noofcoco
    
    def numberofchacolaterequest(self):
        """This is the method used to provide coco by gransparents"""
        logging.info("grans parents provide %s cacolate",self.numberofchocolate)    
        return self.numberofchocolate

class parents(grandparents):

       
    
    def noofcocobyparent(self):
        """This is the method used to provide coco by parents"""
        
        r = grandparents(5)
        getchacolate = r.numberofchacolaterequest()
        logging.info("Number of chacolate %s",getchacolate)
        logging.info("parents provide %s cacolate",10*(getchacolate))  
        return  10*(getchacolate)


class child(parents):
    c = parents(10)
    pc = c.noofcocobyparent()
    logging.info("Number of cacolate child get from parents and grandparents is %s",pc)  