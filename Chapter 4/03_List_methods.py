# Sorting a List
name=["rahul","Soniya","Chetan"]
L1= [1,8,7,6,5,9]
print(L1)
L1.sort() #--> It sorts the original L1 list unlike Strings
print(L1)
#Or
print(L1.sort())
print(L1)
#Or
l2=L1
print(l2)

#Reverse a list
l2.reverse()
print(l2)

#Append (add to the end)
L1.append(45) #--> Adds 45 at the end
print(L1)

#Inserting in a List

L1.insert(4, 15) #--> Adds 15 at the 4th index[0,1,2,3,4,...] and after the 3rd index
print(L1)

#Poping and Removing an item
L1.pop(2) #--> Pops the item at index 2
print(L1)
L1.remove(15) #--> Removes 15 from the list(If it is present)

print(L1.index(8)) #--> Return first index of the value

print(sum(L1)) #--> Method to print sum of a list
print(len(name))

'''There are many list method every one of them is not possible to list down
Search ' List methods python docs ' on google to get more list methods :) '''