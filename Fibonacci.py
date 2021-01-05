# Fibonacci Series
def fibonacci(n):
    a=0
    b=1
    if n<2:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,num):
            c=a+b
            print(c)
            a=b
            b=c

num=int(input("How many fibonacci no. to show:"))
fibonacci(num)