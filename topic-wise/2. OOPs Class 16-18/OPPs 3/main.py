# Inheritance
class car :

    def __init__(self , body , engin , tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage (self):
        print("milage of this car ")

c = car("sold" , "v6" , "radial")
print(c)

class tata(car):
    pass

t = tata("solid1" , "v8" , "radial1")
print(t)
print(t.milage())
