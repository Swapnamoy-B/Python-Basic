class Employee():
    comapany ="Google"
    salary= 500

Subai = Employee()
Rajni = Employee()

print(Subai.comapany)
print(Rajni.comapany)

Subai.salary = 300
Rajni.salary = 400

Employee.comapany = "Youtube"

print(Subai.comapany)
print(Rajni.comapany)

print(Subai.salary)
print(Rajni.salary)