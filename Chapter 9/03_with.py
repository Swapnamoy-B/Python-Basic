# with statement automatically opens and closes a file

with open('another.txt','r') as f:
    a=f.read()
    print(a)

with open('file.txt','w') as f:
    b=f.write("I am writing a new thing")
    