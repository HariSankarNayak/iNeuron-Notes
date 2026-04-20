import logging
class tuple_func:
    logging.basicConfig(filename="tuple_logger.log", level= logging.INFO, format='%(asctime)s \t %(levelname)s \t %(message)s')
    
    def __init__(self, l):
        
        try:
            if type(l) == tuple:
                self.l = l
                logging.info(f"You have entered a valid tuple: {self.l}")
            else:
                raise TypeError(f"Not a tuple {self.l}")
        
        except Exception as e:
            logging.warning("\t Warning! Wrong data type")
            logging.exception(f"\tIt is not a valid tuple, Error: {e}")
    
   
    
    def element_count(self, value):
        """Returns total no of occurance of a element passed in the tuple"""
        count = 0
        logging.info(f"Method element_count called. Finding count of {value}")
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                count +=1
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                logging.info(f"{value} found in given tuple. Count = {count}")
                return count
                break
        else:
            logging.warning("Warning problem occurred")
            logging.error(f" Element {value} is not present")
        
    def first_index(self, value):
        """Returns the index of first occurrance of element passed in the tuple"""
        logging.info(f"Method first_index called. Finding index of {value}")
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                logging.info(f"{value} found in given tuple. Index = {i}")
                return i
                break
        else:
            logging.warning("Warning problem occurred")
            logging.error(f" Element {value} is not present")
    
   