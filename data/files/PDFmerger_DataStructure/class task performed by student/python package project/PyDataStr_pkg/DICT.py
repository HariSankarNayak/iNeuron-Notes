import logging
logging.basicConfig(filename='mydict.log',level=logging.INFO, format='%(asctime)s %(message)s %(levelname)s')
class mydict:
    def __init__(self,d):
        self.d=d
        
    def typeCheck(self):
        if type(self.d)!=dict:
            raise Exception (self.d, 'is not a dictionary')
        return True
    
    def CLEAR(self):
        logging.info('This is a replica of dictionary clear function')
        try:
            if self.typeCheck():
                self.d.clear()
                return self.d
        except Exception as e:
            logging.exception('error message: '+str(e))
            
    def COPY(self):
        logging.info('This is a replica of dictionary copy function')
        try:
            if self.typeCheck():
                d_copied=self.d.copy()
            return d_copied
        except Exception as e:
            logging.exception('error message: '+str(e))
            
    def FROMKEYS(self,x,y):
        ''' This method returns a dictionary with the 
            specified keys and the specified value'''
        
        logging.info('This is a replica of dictionary fromkeys function')
        try:
            if self.typeCheck():
                try:
                    if iter(x):
                        return self.d.fromkeys(x,y)
                except Exception as e:
                    logging.exception('error message'+ str(e))
        except Exception as e:
            logging.exception('error message: '+str(e))
    
    def GET(self,key):
        logging.info('This is a replica of dictionary get function')
        try:
            if self.typeCheck():
                for i in self.d.keys():
                    if i==key:
                        return self.d.get(i)
        except Exception as e:
            logging.exception('error message: '+str(e)) 
            
    def ITEMS(self):
        logging.info('This is a replica of dictionary items function')
        try:
            if self.typeCheck(): 
                return self.d.items()
            
        except Exception as e:
            logging.exception('error message: '+str(e)) 
    
    def KEYS(self):
        logging.info('This is a replica of dictionary keys function')
        try:
            if self.typeCheck(): 
                return self.d.keys()
            
        except Exception as e:
            logging.exception('error message: '+str(e)) 
            
    def POP(self,key):
        logging.info('This is a replica of dictionary pop function')
        try:
            if self.typeCheck():
                try:
                    for i in self.d.keys():
                        if i==key:
                            self.d.pop(i)
                            return self.d
                except :
                    self.logger('The entered key is NOT in d')
            
        except Exception as e:
            logging.exception('error message: '+str(e))
            
    def POPITEM(self):
        ''' This method removes the item that was
            last inserted into the dictionary'''
        
        logging.info('This is a replica of dictionary popitem function')
        try:
            if self.typeCheck():
                self.d.popitem()
                return self.d
                
            
        except Exception as e:
            logging.exception('error message: '+str(e))
            
    def SETDEFAULT(self,key,val):
        ''' method returns the value of the
            item with the specified key'''
        
        logging.info('This is a replica of dictionary setdefault function')
        try:
            if self.typeCheck():
                try:
                    for i in self.d.keys():
                        if i==key:
                            self.d.setdefault(i,val)
                            return self.d
                except :
                    self.logger('The entered key is NOT in d')
            
        except Exception as e:
            logging.exception('error message: '+str(e))
    
    def UPDATE(self,**kwrgs):
        '''method inserts the specified items to the dictionary
           items can be a dictionary, an iterable object with key value pairs'''
        
        logging.info('This is a replica of dictionary update function')
        try:
            if self.typeCheck():
                try:
                    for k,v in kwrgs.items():
                        self.d[k] = v
                        return self.d
                except :
                    self.logger('The entered key is NOT Key-Value format')
            
        except Exception as e:
            logging.exception('error message: '+str(e))
    
    def VALUES(self):
        logging.info('This is a replica of dictionary values function')
        try:
             if self.typeCheck():
                    for i in self.d.items():
                        print(i[1])
        except Exception as e:
            logging.exception('error message: ' + str(e))
                    
                
    def logger(self,log):
        logger=logging.error(log)
        
    