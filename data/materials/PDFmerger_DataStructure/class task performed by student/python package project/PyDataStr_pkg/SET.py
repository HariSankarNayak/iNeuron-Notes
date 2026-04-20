import logging
logging.basicConfig(filename='myset.log',level=logging.INFO, format='%(asctime)s %(message)s %(levelname)s')

class myset:
    def __init__(self,s):
        self.s=s
        
    def typeCheck_set(self):              
               
        if type(self.s) !=set:
            raise Exception(self.s, 'Not in form of set')
        return True
    
    def ADD(self,n):
        logging.info('This is a replica of dictionary clear function')
        try:
            if self.typeCheck_set():
                
                    if iter(n):
                        for i in n:
                            self.s.add(i)                    
                    if type(n)==int:
                        self.s.add(n)
                    
                    return self.s
        except Exception as e:
            logging.exception('error message: '+str(e))
    def CLEAR(self):
        logging.info('This is a replica of set clear function')
        try:
            if self.typeCheck_set():
                self.s.clear()
                return self.s
        except Exception as e:
            logging.exception('error message: '+str(e))
            
    def COPY(self):
        logging.info('This is a replica of set copy function')
        try:
            if self.typeCheck_set():
                s_copied=self.s.copy()
            return s_copied
        except Exception as e:
            logging.exception('error message: '+str(e))
    
    def DIFFERENCE(self,s2):
        ''' Return a set that contains the items that
           only exist in original set, and not in 2nd set '''
        
        logging.info('This is a replica of set difference function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.difference(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))   
            
    def DISCARD(self,n):
        ''' method removes the specified item from the set
            doesn not raise if the item is not in the set'''
        
        logging.info('This is a replica of set discard function')
        
        try:
            if self.typeCheck_set():
                self.s.discard(n)
            return self.s    
        
        except Exception as e:
            logging.exception('error message: '+str(e))   

    def INTERSECTION(self,s2):
        ''' method returns a set that contains the 
            similarity between two or more sets'''
        
        logging.info('This is a replica of set intersection function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.intersection(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))   
       
    def ISDISJOINT(self,s2):
        ''' method returns True if none of the items are 
            present in both sets, otherwise it returns False'''
        
        logging.info('This is a replica of set isdisjoint function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.isdisjoint(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))   
            
    def ISSUPERSET(self,s2):
        ''' method returns True if all items in the specified 
            set exists in the original set, otherwise it retuns False'''
        
        logging.info('This is a replica of set issuperset function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.issuperset(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))   
            
    def POP(self):
        ''' method removes a random item from the set'''
        
        logging.info('This is a replica of set pop function')
        
        try:
            if self.typeCheck_set():
                self.s.pop()
            return self.s    
        
        except Exception as e:
            logging.exception('error message: '+str(e)) 
            
    def REMOVE(self,n):
        ''' method removes the specified element from the set
            unlike discard(), this method  raise an error if 
            the specified item does not exist'''
        
        logging.info('This is a replica of set remove function')
        
        try:
            if self.typeCheck_set():
                self.s.remove(n)
            return self.s    
        
        except Exception as e:
            logging.exception('error message: '+str(e))   

    def SYMMETRIC_DIFFERENCE(self,s2):
        ''' Return a set that contains all items from both sets,
            except items that are present in both sets'''
        
        logging.info('This is a replica of set symetric_difference function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.symmetric_difference(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))  
            
    def UNION(self,s2):
        ''' Returns a set that contains all items
            from both sets, duplicates are excluded'''
        
        logging.info('This is a replica of set union function')
        try:
            if self.typeCheck_set():
                try:
                    if type(s2)==set:
                        z=self.s.union(s2)
                    return z
                except Exception as e:
                    self.logger('Not a set')
                    logging.exception('error message '+str(i))
                
        except Exception as e:
            logging.exception('error message: '+str(e))   

