#Write hello in front of names starting with 'S'

li=["Rahul","Soniya","Chetan","Ketan"]

for name in li: #--> We can write anything like item or name
    if name.startswith("S"):
        print("Hello "+name)