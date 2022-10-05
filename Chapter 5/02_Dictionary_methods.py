myDict = {
    
    "Fast": "In a quick manner",
    "Subai": "A coder",
    "Marks": [1, 2, 3, 4],  
    "anotherdict": {  
        'happy': 'boy'
    },
    1:2
}

print(myDict.keys()) #-->printing every key in a dictionary
print(myDict.values()) #-->printing every values in a dictionary
print(type(myDict.keys())) #--> class 'dict_keys'>
print(list(myDict.keys())) #--> Printing the keys as list (typecasting to list)
print(myDict.items()) #--> Prints the (Key, value) for all contents of the dictionary

# Updating a dictionary
print(myDict)

updatedict={
    "lovish":"Friend",
    'Subai' : 'python' #--> We can also change existing values
}
myDict.update(updatedict)
print(myDict)

# get() function
print(myDict['Subai'])   #--> Print the value of the key
print(myDict.get('Subai')) #--> This will give the same output as the above one

# Difference between .get() and syntax for dictionaries
print(myDict['Subai1']) #--> This will throw an error
print(myDict.get('Subai1')) #--> This will print 'none' as there is no matching key
