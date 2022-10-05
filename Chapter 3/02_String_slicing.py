greeting = "Good Morning"
name = "Subai"
n="subaiisdone"
print(type(name))

print(greeting + name)  # Concate the names
c = name + greeting  # You can also concatinate like this
print(c)
print(name[0])  # You will get the character at index 0

'''In python string indexes are started with 0'''
# name[3] = "d" --> Does not work

print(name[0:3])  # --> It will show the character from 0 to 2
sl = name[1:4]  # --> Assinging a new varible for the sliced part
print(sl)
print(name[:4])  # --> is same as name[0:4](minimum index)
print(name[1:])  # --> is same as name[1:5](maximum index)

'''Why use negetive indexes ?'''
" -1 is the last index and it goes back from that, like -2 is second last index -3 is third last index "

c = name[-4:-1]  # --> is same as name[1:4]
d = name[-5:-2]  # --> is same as name[0:2]
e = name[-5:-1]  # --> is same as name[0:4]
print(c)
print(d)
print(e)

f=n[0::3] #--> skips every 2 values
print(f)