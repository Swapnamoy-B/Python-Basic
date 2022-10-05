# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word twinkle

with open('poems.txt','r') as f:
    a=f.read()
    if 'twinkle' in a:
        print("Yes it is present")
    else:
        print("its not present")
        
