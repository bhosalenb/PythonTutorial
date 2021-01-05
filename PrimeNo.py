# List of prime nos between 1 to 100:

def primeNo(n):
    flag=0
    if n <=1:
        return None
    else:

        for i in range(2, int(n/2)):
            if n % i == 0:
                flag=0
                break
        else:
                flag = 1
        if flag ==0:
            return None
        else:
            return n

print("List of prime nos between 1 to 100:")
for j in range(1,101):
    pn = primeNo(j)
    if pn is not None:
        print(pn)