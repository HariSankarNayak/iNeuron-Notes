class dictionary:
    def __init__(self,d):
        self.d=d
        
    def get_keys(self):
        if type(self.d)==dict:
            for i in self.d.keys():
                print(i)
                
    def get_values(self):
        if type(self.d)==dict:
            for i in self.d.items():
                print(i[1])
                
    def get_except(self):
        if type(self.d)!=dict:
            raise Exception ('incorrect input')
                
            
    def get_input(self):
        self.d=eval(input())
        print(self.get_keys()) 
        print(self.get_values())
                
    def new_valu(self,k,v):
        self.d[k]=v