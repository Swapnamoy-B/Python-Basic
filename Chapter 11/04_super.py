class person:
    country = "India"
    def __init__(self):
        print("Initialising person ....")
    
    def takebreak(self):
        print("I am breathing")

class Employee(person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initialising Employee....")

    def getSalary(self):
        print(f"Salary  is {self.salary}")

    def takebreak(self):
        super().takebreak()
        print("I am Luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initialising Programmer....")

    def getSalary(self):
        print("No salary")

    def takebreak(self):
        super().takebreak()
        print("I am also breathing")


p = person()
p.takebreak()

e = Employee()
e.takebreak()

pr = Programmer()
pr.takebreak()


