class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer") # --> Overidding

e = Employee()
p =Programmer()

p.showDetails()