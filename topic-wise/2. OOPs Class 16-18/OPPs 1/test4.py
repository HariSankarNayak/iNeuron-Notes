class person :

    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_if_input(self, email_id):
        print("Take and mail id from a person and print it ", email_id)

    def ask_name(self):
        name = input("Tell me your name ")
        return name

    def ask_dob(self):
        dob = input("Tell me your date of birth ")
        return dob

sudh = person()
anuj = person()
gargi = person()
krish = person()
hitesh = person()

sudh.email_if_input("sudhanshu@gmail.com")
print(sudh.ask_name())

print(hitesh.ask_dob())
