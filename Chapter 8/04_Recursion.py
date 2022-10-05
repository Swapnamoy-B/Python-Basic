#n!=1 * 2 * 3 * 4 * 5....* n
#n!=1 * 2 * 3 * 4...n-1 * n
#n!=n*(n-1)

# def factorial_inter(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1) #Recur
    


f=factorial_recursive(5)
print(f)

