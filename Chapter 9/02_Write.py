f = open('another.txt','w')
f.write("Write in a file here")

f.close()

f = open('another.txt','a')
f.write("I am appending")
f.close()