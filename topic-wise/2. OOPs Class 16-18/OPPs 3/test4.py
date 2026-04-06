# Data Abstraction
class ineuron:
    __students = "data science"

    def students(self):
        print("print the class of students", ineuron.__students)

i = ineuron()
i.students()
print(i._ineuron__students)
