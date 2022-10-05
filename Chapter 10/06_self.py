class Employee:
    company = "Google"
    def getsalaray(self):
        print(f"The salary for the company {self.company} is {self.salary} ")

harry = Employee()

harry.salary= 500

# harry.getsalaray() # -- It internally converts to the code below
Employee.getsalaray(harry) # --> Same as the code above