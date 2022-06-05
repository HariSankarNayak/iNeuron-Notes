import logging
logging.basicConfig(filename='mytup.log',level=logging.INFO,format='%(asctime)s %(message)s %(levelname)s')
class mytuple:
    def __init__(self,t):
        self.t=t
        
    def typeCheck_tup(self):
        logging.info('To check if the type is tuple')
        if type(self.t)!=tuple:
            raise Exception('Not a tuple')
        return True
    
    def COUNT(self,n):
        ''' This function counts the number of occurrences
            for an element in the tuple'''
        
        logging.info('This is a replica of tuple count')
        try:
            if self.typeCheck_tup():
                for i in self.t:
                    if i==n:
                        return self.t.count(i)
        except Exception as e:
            logging.exception('error message '+str(e))
          
    def INDEX(self,n):
        ''' This function returns position or index of an
            element of the tuple, works for duplicate numbers as well'''
        
        logging.info('This is a replica of tuple index')
        try:
            l=[]
            if self.typeCheck_tup():
                for i in range(len(self.t)):
                    if self.t[i]==n:
                        l.append(i)
                return l
                        
    
        except Exception as e:
            logging.exception('error message ',e)
            
        