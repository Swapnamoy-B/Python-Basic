class Employee:
    company = "Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("This method runs automatically")
    def getdetails(self):
        print(f"The name is {self.name}")
        print(f"The salary is {self.salary}")
        print(f"The subunit is {self.subunit}")

harry=Employee("Harry",500,"Youtube")

harry.getdetails()

