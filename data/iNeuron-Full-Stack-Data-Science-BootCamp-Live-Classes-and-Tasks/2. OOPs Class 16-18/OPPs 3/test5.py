class ineuron:
    def __init__(self):
        self.students1 = "data science "

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "data analytics"
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "data science "

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1 = new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "big data"
i1.students()
i1.student_change("Mohammad Wasiq")
i1.students()

