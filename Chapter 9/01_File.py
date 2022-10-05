# Open function takes two parameters ("Filename.ext","mode")

f = open('file.txt', 'r') # --> 'r' means Read mode/If we dont specify any mode it will be 'r'
data=f.read() #--> We are putting the contents in data
'''We cant read a duplicate times'''
data=f.read(5)  # --> It will read upto 5 characters

'''We write multiple readline staements'''
data = f.readline()  # --> It will only read the first line
print(data)
data = f.readline()  # --> Now it will read the second lines
print(data)  # --> We need to print the second line again
f.close()  # --> We always need to close a file after its use

'''Few more modes are :- '''

# 'r' = open for reading
# 'w' = open for writing
# 'a' = open for appending
# 't' = open for updating

# 'rb' Will open for read in binary mode
# 'rt' will open for read in text mode (It is set in default)

