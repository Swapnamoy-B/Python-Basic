class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept

    def printDetails(self):
        print(f"The Name of the employee is {self.name} and his salary is \
        {self.salary}  works in {self.dept}")


subai=Programmer("Subai", 500 , "Associate")
rahul=Programmer("Rahul", 400, "Technical")

subai.printDetails()
rahul.printDetails()
