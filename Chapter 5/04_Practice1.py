#Create a dictionary for hindi to english words and let the user look up the word

myDict={
    'Alsi' : 'lazy',
    'Ghumna' : 'Travelling',
    'Sona' : 'Sleeping'
}


print("The optons are",myDict.keys())
a= input("Enter the hindi word ")
print("The meaning of your word is",myDict.get(a))

# Write a program to input 8 numbers from the user and display all the unique numbers(once)

n1=int(input("Enter the 1 st number"))
n2=int(input("Enter the 2 nd number"))
n3=int(input("Enter the 3 rd number"))
n4=int(input("Enter the 4 rd number"))
n5=int(input("Enter the 5 rd number"))
n6=int(input("Enter the 6 rd number"))
n7=int(input("Enter the 7 rd number"))
n8=int(input("Enter the 8 rd number"))

s1={n1,n2,n3,n4,n5,n6,n7,n8}

print(s1)

#Can we have a set with 18(int) 18(str) as a value in it ?

s2={3,"3"}
print(s2)

#Yes we can as string and integer are not same

#What will be the length of the set

s3=set()

s3.add(20)
s3.add("20")
s3.add(20.0)

print(len(s3))

#The length will be 2 as 20.0 and 20 have same values

'''Create an empty dictionary. Allow 4 friends to enter their favourite languages
and use keys as their names.Assume that the names are unique'''

empDict={}

a=input("Enter your favourite language Mathu\n")
b=input("Enter your favourite language Naman\n")
c=input("Enter your favourite language Subai\n")
d=input("Enter your favourite language Rahul\n")

empDict['Mathu']=a
empDict['Naman']=b
empDict['Subai']=c
empDict['Rahul']=d

print(empDict)