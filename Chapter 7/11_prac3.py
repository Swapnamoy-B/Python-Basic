temp = 0

num=int(input("Enter a number : \n"))

for i in range(2,num):
    if(num%i==0):
        temp=temp+1
    

if(temp==1):
    print("The number is not prime")
else:
    print("The number is prime")

