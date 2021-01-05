# Factorial program without function
def fact(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    print(f"Factorial of {n} is: {fac}")

n= int(input("Enter no. to display factorial: "))

fact(n)