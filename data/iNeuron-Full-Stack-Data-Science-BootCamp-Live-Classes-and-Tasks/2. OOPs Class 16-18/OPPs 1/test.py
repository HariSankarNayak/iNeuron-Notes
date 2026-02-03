class Person :

    def __init__(self, name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj" , "bhandari" , "anuj@gmail.com" , 1994)
sudh = Person("sudhanshu", "kumar", "sudhanshu@gmail.com", 1990)
gargi = Person("gargi", "xyz", "gargi@gmail.com", 2000)
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))