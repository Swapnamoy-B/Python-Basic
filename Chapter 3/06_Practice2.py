# Replace name and date in a letter

Letter='''Dear <name>
                You are Selected !!!
                <date>'''
name=input("Enter name : \n")
date=input("Enter Date : \n")

str=(Letter.replace("<name>", name))

str1=(str.replace("<date>",date))

print(str1)

#OR

Letter=(Letter.replace("<name>", name))

Letter=(Letter.replace("<date>",date))

print(Letter)
