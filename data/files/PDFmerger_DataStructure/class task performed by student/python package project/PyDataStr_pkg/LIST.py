import logging
logging.basicConfig(filename='mylist_assgnmt.log',level=logging.INFO,format='%(asctime)s $(message)s %(levelname)s ')
class mylist:
    def __init__(self,l):
        self.l=l
    
    def typeCheck(self):
        logging.info('To check if the type is list')
        if type(self.l)!=list:
            raise Exception (self.l, 'is NOT a list')
        return 1
            
    def APPEND(self,l1):
        ''' method appends an element to the end of the list'''
        
        logging.info('This is a replica of list append')
        try:
            if self.typeCheck():
                if type(l1)==list:
                    for i in l1:
                        self.l.append(i)
                
                else:
                    self.l.append(l1)
                return self.l 
        except Exception as e:
            self.logger('An error occured')
            logging.exception('type of error'+str(e))
                
    def CLEAR(self):
        logging.info('This is a replica of list clear')
        ''' Removes all elements from the list'''
        
        try:
            if self.typeCheck:
                self.l.clear()
                return self.l
        except Exception as e:
            self.logger('An error occurred')
            logging.exception('type of error is '+str(e))
            
    def COPY(self):
        logging.info('This is a replica of list copy')
        try:
            if self.typeCheck():
                return self.l.copy()
        except Exception as e:
            self.logger('An error occured')
            logging.exception('type of error is ',str(e))
            
    def COUNT(self,n):
        logging.info('This is a replica of list count')
        try:
            
            if self.typeCheck():
                return self.l.count(n)
        except Exception as e:
            self.logger("An error occurred")
            logging.exception ('type of error is ',str(e))
            
    def EXTEND(self,l2):
        ''' method adds the specified list elements 
           (or any iterable) to the end of the current list'''
        
        logging.info('This is a replica of list extend')
        try:
            if self.typeCheck():
                try:
                    if type(l2)==list:
                        self.l.extend(l2)
                        return self.l
                except:
                    self.logger('Please enter a list')
                    
        except Exception as e:
            self.logger('An error occurred')
            logging.exception('type of error is ',str(e))
            
    def INDEX(self,n):
        '''method returns the position, works for multiple 
           occurrences of the specified value'''
        
        logging.info('This is a replica of list index')
        try:
            index_list=[]
            if self.typeCheck():
                for i in range(len(self.l)):
                    if self.l[i]==n:
                        index_list.append(i)
                return index_list
                
                
        except Exception as e:
            self.logger('An error occurred')
            logging.exception('type of error is ',str(e))  
            
    def INSERT(self,indx,num):
        '''method inserts the specified value at the specified position'''
        
        logging.info('This is a replica of list insert')
        try:
            if self.typeCheck():
                self.l.insert(indx,num)
                return self.l
        except:
            self.logger('Enter list')
            logging.exception('Enter list', str(e))
            
    def POP(self,indx):
        logging.info('This is a replica of list pop')
        try:
            if self.typeCheck():
                self.l.pop(indx)
                return self.l
        except Exception as e:
            self.logger('An occurred')
            logging.exception('type of error'+ str(e))
            
    def REMOVE(self,n):
        logging.info('This is a replica of list remove')
        try:
            if self.typeCheck():
                for i in self.l:
                    if i==n:
                        self.l.remove(n)
                        return self.l
        except Exception as e:
            self.logger('An error occured')
            logging.exception('type of error' + str(e))
            
    def REVERSE(self):
        logging.info('This is a replica of list reverse')
        try:
            if self.typeCheck():
                for i in range(len(self.l)):
                    return self.l[::-1]
                
        except Exception as e:
            self.logger('An error occurred')
            logging.exception('type of error', str(e))
    
    def SORT(self):
        '''method sorts the list, takes user input of
           if ascending or descending order'''
        
        logging.info('This is a replica of list sort')
        order=input('Enter ascending/descending')
        try:
            if self.typeCheck():
                if order=='ascending':
                    return sorted(self.l,reverse=False)
                else:
                    return sorted(self.l,reverse=True)
                    
        except Exception as e:
            self.logger('An error occurred')
            logging.exception('type of error', str(e))
            
        def __str__(self):
            return 'this is a class for various functions of list'        
            
    def logger(self,log):
        logger=logging.error(log)
        
    
        