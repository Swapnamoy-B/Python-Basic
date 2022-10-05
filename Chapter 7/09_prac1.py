# Print Multiplication table of a number

num=int(input("Enter the number"))
for i in range(1,11):
    if(num%2==0):
        print(str(num)+"X"+str(i)+"="+str(i*num))
    else:
        print(f"{num} X {i} = {num*i}") #--> By writing ' f ' we can write calculate variables within {}