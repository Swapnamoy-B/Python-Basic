import time

class Employee:
    company = "Google"

    def getsalaray(self, signature):
        print(
            f"The salary for the company {self.company} is {self.salary} / {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")
   
    @staticmethod
    def showTime():
        seconds = time.time()
        t=time.ctime(seconds)
        print(f"The time is {t}")

harry = Employee()

harry.salary = 500
sig = "By me"

harry.getsalaray("Thanks")
harry.getsalaray(sig)
harry.greet()
harry.showTime()
