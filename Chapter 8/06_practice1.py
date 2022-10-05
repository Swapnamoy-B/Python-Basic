def max (num1,num2,num3):
    if num1>num2:
        numg1=num1
    else:
        numg1=num2
    if numg1>num3:
        return numg1
    else:
        return num3

n1=int(input("Enter the first number : \n"))
n2=int(input("Enter the second number : \n"))
n3=int(input("Enter the third nujmber : \n"))

print("The greatest number is : ",max(n1,n2,n3))

