"--- Set is a collection of non-repetative items ---"

a = {1, 3, 4, 5}
print(type(a))
'b1={}'  # This creates an empty dictionary

b = set()  # Creating an empty set

b.add(4)
b.add(5)
b.add(6)  # Adding a repeated value doesnt change a set

b.add((3, 7, 8))  # --> A tuple can be added to set
print(b)
'b.add([9,10,12])' # --> A list cannot be  added as it is unhashable (We can apply changes)
'b.add({1:2})'  # --> A dictionary can't also be added because it is unhashable


print(len(b))  # Prints the length of the set

b.remove(5)  # --> Removes 5 from set b if present
print(b)
print(b.pop()) # --> removes a random value from set

b.clear() # --> Empties the set b
print(b)


