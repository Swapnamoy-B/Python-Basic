import os

#String Functions

st="I am learning strings functions"

print(len(st)) # --> Finds the length of the string
print(st.endswith("functions")) # --> Returns True or False if the end matches or not
print(st.count("o")) # --> Returns the occurence of a character or word as a number
print(st.capitalize()) # --> Capitalizes the character or whole string
print(st.find("am")) # --> Finds the first index of the character or string searched
str=(st.replace("functions", "methods")) #-->  Finds and replaces everytikme the first character or string appears
str = (str.strip()) #--> strips extra spaces in the string
print(str)