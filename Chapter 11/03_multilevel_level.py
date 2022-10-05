class person:
    country = "India"
    def takebreak(self):
        print("I am breathing")

class Employee(person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary  is {self.salary}")

    def takebreak(self):
        print("I am Luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary")

    # def takebreak(self):
    #     print("I am also breathing")


p = person()
p.takebreak()
e = Employee()
e.takebreak()
pr = Programmer()
pr.takebreak()
print(p.country)

