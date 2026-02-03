# Here we use wasiq inplace of self

class Person :

    def __init__(sudh,name,surname , emailid , year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def __init__(sudh,name,surname ):
        sudh.name1 = name
        sudh.surname = surname

    def age(sudh , curretn_year):
        return curretn_year

anuj_var  = Person("anuj" , "bhandari")
sudh = Person("sudhanshu " ,"kumar" )
gargi = Person("gargi" , "xyz" )
print(anuj_var.age(2022))