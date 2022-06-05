import logging
class list_func:
    logging.basicConfig(filename="list_logger.log", level= logging.INFO, format='%(asctime)s \t %(levelname)s \t %(message)s')
    
    def __init__(self, l):
        
        try:
            if type(l) == list:
                self.l = l
                self.l1 = [""]
                logging.info(f"You have entered a valid List: {self.l}")
            else:
                raise TypeError(f"Not a list {self.l}")
        
        except Exception as e:
            logging.warning("\t Warning! Wrong data type")
            logging.exception(f"\tIt is not a valid list, Error: {e}")
    
    def list_appender(self, value):
        """Returns the list after adding the new element at the end of the list passed"""
        try:
            logging.info(f"Method list_appender called. Adding element {value} to the list")
            self.l = self.l + self.l1
            self.l[len(self.l)-1] = value
            return self.l
        except Exception as e:
            logging.warning("Warning! something wrong")
            logging.exception(f"Error occurred: {e}")
    
    def clear_list(self):
        """Clears the content of the list"""
        logging.info("Method clear_list called. Clearing the list")
        self.l = []
        return self.l
    
    def list_copier(self):
        """Returns the copy of list"""
        logging.info("Method list_copier called")
        return self.l
    
    def element_count(self, value):
        """Returns total no of occurance of a element passed in the list"""
        count = 0
        logging.info(f"Method element_count called. Finding count of {value}")
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                count +=1
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                logging.info(f"{value} found in given list. Count = {count}")
                return count
                break
        else:
            logging.warning("Warning problem occurred")
            logging.error(f" Element {value} is not present")
        
    def first_index(self, value):
        """Returns the index of first occurrance of element passed in the list"""
        logging.info(f"Method first_index called. Finding index of {value}")
        for i in range(0, len(self.l)):
            if value == self.l[i]:
                logging.info(f"{value} found in given list. Index = {i}")
                return i
                break
        else:
            logging.warning("Warning problem occurred")
            logging.error(f" Element {value} is not present")
    
    def list_insertion(self, index, value):
        """Returns the list after inserting new element before the index passed"""
        logging.info(f"Method list_insertion called. Inserting {value} before index {index} of given list")
        try:
            a= self.l[0:index]
            b= self.l[index:]
            self.l[index]=value
            self.l= a+self.l[index : index+1]+ b
            logging.info(f"Element {value} inserted. New list : {self.l}")
            return self.l
        except Exception as e:
            logging.warning("Warning! problem occured")
            logging.exception("Error: ",e)
    
    def list_extender(self, value):
        """Returns the list after adding the new element at the end of the list"""
        logging.info(f"Method list_extender called. Extending the given list with {value}")
        try:
            l2= []
            if type(value) == str or type(value)== list or type(value)== tuple or type(value)==dict or type(value)==set:
                for i in value:
                    l2.append(i)
            else:
                l2.append(value)
            self.l = self.l + l2
            return self.l
        
        except Exception as e:
            logging.warning("Warning! problem occured")
            logging.exception("Error: ",e)
            
    def list_popper(self, index = -1 ):
        """Removes any element from the list.
        By default index = -1 """
        logging.info(f"Method list_popper called. Deleting the element at index {index} ")
        try:
            if index >= len(self.l):
                raise Exception("Index out of range")
            if index != -1:
                self.l=self.l[0:index]+self.l[index+1:]
                return self.l
            else:
                self.l = self.l[:-1]
                return self.l
        except Exception as e:
            logging.warning("Warning! problem occured")
            logging.exception("Error: ",e)
        
    def list_reversal(self):
        """Returns the reverse of the list"""
        logging.info("Method list_reversal called")
        return self.l[::-1]
    
    def list_sorter(self, order = False):
        """It sorts the element in ascending or decending order.
        By default, order = False for ascending"""
        logging.info("Method list_sorter called")
        try:
            if order == False:
                for i in range(0, len(self.l)):
                    for j in range(i+1, len(self.l)):
                        if self.l[j]<=self.l[i]:
                            c = self.l[j]
                            self.l[j] = self.l[i]
                            self.l[i] = c    

            elif order == True:
                for i in range(0, len(self.l)):
                    for j in range(i+1, len(self.l)):
                        if self.l[j]>=self.l[i]:
                            c = self.l[j]
                            self.l[j] = self.l[i]
                            self.l[i] = c

            else:
                raise Exception("Wrong value of order passed, please enter order = True/False")
                
        except Exception as e:
            logging.warning("Warning! problem occured")
            logging.exception("Error: ",e)
            
    def list_remover(self, value):
        """Returns the list after removing element from the existing list"""
        logging.info(f"Method list_remover called. Deleting {value} from the list")
        try:
            for i in range(0, len(self.l)):
                if value == self.l[i]:
                    self.l= self.l[0:i]+self.l[i+1:]
                    return self.l
                    break
            else:
                raise Exception("Value does not exist")
        except Exception as e:
            logging.warning("Warning! problem occured")
            logging.exception("Error: ",e)