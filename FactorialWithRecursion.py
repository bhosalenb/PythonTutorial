# factorial program using recursion

def fact(n):
    if n==1:
        return n
    fac=n*fact(n-1)

    return fac

n= int(input("Enter no. to display factorial of a given no: "))
result=fact(n)

print("Result: ",result)