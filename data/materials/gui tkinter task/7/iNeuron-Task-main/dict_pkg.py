import logging
class dict_func:
    logging.basicConfig(filename='dict_logger.log', level = logging.INFO, format='%(asctime)s \t %(levelname)s \t %(message)s')
    def __init__(self, d):
            if type(d) == dict:
                self.d = d
                logging.info(f"Valid Dictionary entered: {self.d}")
            else:
                logging.warning("Warning! Error occured")
                logging.error(f"Not a  valid dictionary, please enter only valid dictionary")
    
    def dict_keys(self):
        """Returns the list of keys in the dictionary"""
        logging.info("Method dict_keys called.")
        l1=[]
        for i in self.d:
            l1.append(i)
        return l1
        
    def dict_values(self):
        """Returns the list of values in the dictionary"""
        logging.info("Method dict_values called.")
        l2=[]
        for i in self.d:
            l2.append(self.d[i])
        return l2
   
    def dict_clear(self):
        """Removes all the elements in the dictionary"""
        logging.info("Method dict_clear called.")
        self.d={}
        logging.warning("Dictionary cleared")
        return self.d
    
    def dict_copy(self):
        """Returns the shallow copy of the dictionary"""
        logging.info("Method dict_copy called.")
        return self.d
    
    def dict_get(self, key):
        """Returns the corresponding value of the key passed if key is present.
        If key is not present, then it raises Key Error"""
        logging.info(f"Method dict_get called. Getting the value of key : {key}")
        try:
            if type(key)== str:
                for i in self.d:
                    if i == key:
                        logging.info(f"Value: {self.d[i]}")
                        return self.d[i]
                        break
                else:
                    raise KeyError("Key not found")         
            else:
                raise TypeError("Not a valid key")
        except Exception as e:
            logging.warning("Warning! problem occurred")
            logging.exception("Error occurred: ",e)
            
    def dict_items(self):
        """Returns the list of tuples of all key value pair in the dictionary"""
        logging.info("Method dict_items called.")
        l=[]
        for i in self.d:
            t = []
            for j in range(0,2):
                if j == 0: t.append(i)
                if j == 1: t.append(self.d[i])
            l.append(tuple(t))
        logging.info(f"List: {l}")
        return l
    
    def dict_pop(self, key):
        """Removes the specified key value pair and return its value.
        If key is not present, then it raises Key Error"""
        logging.info(f"Method dict_pop called. Deleting the key : {key}")
        try:
            d1={}
            poped = self.d[key]
            if str(key) in self.d:
                la = self.dict_keys()
                la.remove(key)
                for i in range(0, len(la)):
                    d1[la[i]] = self.d[la[i]]
                self.d = d1
                logging.info(f"Poped value is: {poped}")
                return poped
            else:
                raise KeyError("Key is not found")
        except Exception as e:
            logging.warning("Warning! Problem occurred")
            logging.exception("Error: ",e)
    
    def dict_popitems(self):
        """Returns the dictionary after removing the last entry i.e. key value pair"""
        logging.info(f"Method dict_popitems called.")
        la = self.dict_keys()
        logging.warning(f"Removing key: {la[len(la)-1]}")
        d1 ={}
        for i in range(0, len(la)-1):
            d1[la[i]] = self.d[la[i]]
        self.d = d1
        logging.info(f"New Dictionary: {self.d}")
        return self.d
            
    
    def dict_setdefault(self, key, default = None):
        """If the key is not present, then it adds key to dictionary with its corresponding value equal to default,
        by default value of default is None. If key is present, then it returns its corresponding value"""
        logging.info(f"Method dict_setdefault called.")
        try:
            if type(key) == str:
                if key in self.d:
                    logging.info(f"Key, {key} Found. Value : {self.d[key]}")
                    return self.d[key]
                else:
                    logging.info(f"Key, {key} Not Found. Adding it to the dictionary with Value : {default}")
                    self.d[key] = default
                return self.d
            else:
                raise TypeError("Not a valid key")
        except Exception as e:
            logging.warning("Warning! problem occurred")
            logging.exception("Error: ",e)
        
    def dict_updater(self, **kwargs):
        """Updates the dictionary with new key value pair i.e. It can add new key value pair to the dictionary"""
        logging.info("Method dict_updater called")
        try:
            for i in kwargs:
                self.d[i] = kwargs[i]
            logging.info(f"Updated Dictionary: {self.d}")
            return self.d
        except Exception as e:
            logging.warning("Warning! problem occurred")
            logging.exception("Error: ",e)
            
    def dict_fromkeys(self, iterable, value = None ):
        """Returns new dictionary with each element of iterables as key and its value set to value passed, 
        by default value = None """
        logging.info("Method dict_fromkeys called")
        try:
            d3 = {}
            for i in iterable:
                d3[i] = value
            logging.info(f"New Dictionary: {d3}")
            return d3
        except Exception as e:
            logging.warning("Warning! problem occurred")
            logging.exception("Error: ",e)
             