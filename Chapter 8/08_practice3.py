#n!=(n-1)! * n
# sum(n) = sum(n-1)+n

def sum(n):

    if n<1 :
        return 1
    else:
        return sum(n-1)+n

num=5

print(sum(num))