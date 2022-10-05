''' ---Dictionary is a collection of key value pairs---'''
''' * It is unordered 
* It is mutable
* It is indexed
* Cannot contain duplicate keys'''



myDict = {
    # --> Fast is the 'key' and other is the 'value' give a comma(,) for next line
    "Fast": "In a quick manner",
    "Subai": "A coder",
    "Marks": [1, 2, 3, 4],  # --> We can also give a list in the value
    "anotherdict": {  # --> We can also make a dictionary within a dictionary
        'happy': 'boy'
    },
    1:2
}

print(myDict['Fast'])  # --> This will print the value of the fast 'key'
print(myDict["Subai"])  # --> This will print the value of the subai 'key'
print(myDict["Marks"])  # --> This print the list assigned to marks
myDict['Marks']=[45,78] # --> Changing the values in marks
print(myDict['anotherdict']) # --> This will print both key and value of anotherdict
print(myDict["Marks"])

print(myDict.keys()) #-->printing every key in a dictionary