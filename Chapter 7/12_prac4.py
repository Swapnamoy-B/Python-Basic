# n!= 1 X 2 X 3 X 4 X 5....Xn
# 5!= 1 X 2 X 3 X 4 X 5

num=int(input("Enter a number : \n"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
    
print(f"Factorial of {num} is {factorial}")