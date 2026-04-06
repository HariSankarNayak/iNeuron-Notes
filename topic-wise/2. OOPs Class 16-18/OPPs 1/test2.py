# Here we use wasiq inplace of self
class Person :

    def __init__(wasiq, name, surname, emailid, year_of_birth):
        wasiq.name = name
        wasiq.surname = surname
        wasiq.emailid = emailid
        wasiq.year_of_birth = year_of_birth

    def age(wasiq, current_year):
        return current_year - wasiq.year_of_birth

anuj_var = Person("anuj " , "bhandari" , "anuj@gmail.com" , 1994)
sudh = Person("sudhanshu", "kumar", "sudhanshu@gmail.com", 1990)
gargi = Person("gargi", "xyz", "gargi@gmail.com", 2000)
print(anuj_var.age(2022))


