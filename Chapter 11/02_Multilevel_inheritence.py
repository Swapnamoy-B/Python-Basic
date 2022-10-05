class Employee:
    company = "visa"
    ecode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):
    
    name = "Rohit"

p = Programmer()
p.upgradelevel()
print(p.level)
print(p.company)
