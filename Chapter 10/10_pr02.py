import math

class Calculator:

   
    
    def __init__(self):
        self.n=int(input("Enter the number"))
        

    def printResults(self):
        print(f"The Sqaure of the number is {self.n*self.n}")
        print(f"The cube of the number is {self.n*self.n*self.n}")
        print(f"The square root of the number is {math.sqrt(self.n)}")

num=Calculator()


num.printResults()
   