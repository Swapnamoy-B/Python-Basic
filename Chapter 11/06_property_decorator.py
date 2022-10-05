class Employee:
    company = "Bharat Gas"
    salary = 5600
    # salarybonus = int(input("Enter bonus : "))
    salarybonus = 100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary) # We dont need () as it acts as a property
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
