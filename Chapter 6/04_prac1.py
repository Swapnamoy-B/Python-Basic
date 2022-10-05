a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a > b and a > c and a > d):
    print("A is the greatest")
elif(b > c and b > d):
    print("B is the greatest")
elif(c > d):
    print("C is greatest")
else:
    print("D is greatest")

    # Or
if(a > d):
    f1 = a
else:
    f1 = d

    if(b > c):
        f2 = b
    else:
        f2 = c

        if(f1 > f2):
            print(str(f1) + " Is greatest")
        else:
            print(str(f2) + "Is Greatest")
