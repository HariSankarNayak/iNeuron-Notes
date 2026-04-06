import logging

logging.basicConfig(filename = "multiplelogs.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )

class father:
   
    def __init__(self,noofcoco) -> None:
        self.numberofchocolate =  noofcoco
    
    def numberofcoco(self):
        """This is the method used to provide coco by father"""
        logging.info("father parents provide %s cacolate",self.numberofchocolate)    
        return self.numberofchocolate

class mother:

    def __init__(self,noofcoco) -> None:
        self.numberofchocolate =  noofcoco
    
    def numberofcoco(self):
        """This is the method used to provide coco by mother"""
        logging.info("father parents provide %s cacolate",self.numberofchocolate)    
        return  self.numberofchocolate


class child(father,mother):
    f = father(10)
    fc = f.numberofcoco()
    logging.info("Number of cacolate child get from father is %s",fc)  

    m = mother(10)
    mc = m.numberofcoco()
    logging.info("Number of cacolate child get from mother is %s",mc)  

    logging.info("Total number of coco is %s", fc*mc)