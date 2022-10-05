'''---Tuples are immutable---'''

# Creating a tuple
t = (1, 2, 4, 5)  # --> Tuples are created usig ()
t1 = ()  # --> Creating an empty tuple
t2 =(1,) #--> Tuple with single element
't2=(1)' #--> Wrong way declare a tuple with single element


# Printing the elements of a tuple
print(t[0])  # --> To print we use t[i]
print(t1)  # --> Printing the empty tuple

# Cannot update the values of a tuple
't[0]=0'  # --> Will throw an error
