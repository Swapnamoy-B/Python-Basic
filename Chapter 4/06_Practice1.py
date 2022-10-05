# Take a list of fruits from user

f1 = input("Enter fruit number 1 : \n")
f2 = input("Enter fruit number 2 : \n")
f3 = input("Enter fruit number 3 : \n")
f4 = input("Enter fruit number 4 : \n")
f5 = input("Enter fruit number 5 : \n")
f6 = input("Enter fruit number 6 : \n")
f7 = input("Enter fruit number 7 : \n")

fruitList = [f1, f2, f3, f4, f5, f6, f7]
print(fruitList)

# Take six marks input from the and sort them

m1 = input("Enter the 1st marks : \n")
m2 = input("Enter the 2nd marks : \n")
m3 = input("Enter the 3rd marks : \n")
m4 = input("Enter the 4th marks : \n")
m5 = input("Enter the 5th marks : \n")
m6 = input("Enter the 6th marks : \n")

marksList = [m1, m2, m3, m4, m5, m6]
marksList.sort()
print(marksList)

# Sum a list of 4 numbers

l1 = [1, 2, 3, 4]
# Or
print(l1[0]+l1[1]+l1[2]+l1[3])
# Or
print(sum(l1))  # --> Method to print sum of a list
a = l1[0]
b = l1[1]
c = l1[2]
d = l1[3]

print(a+b+c+d)
