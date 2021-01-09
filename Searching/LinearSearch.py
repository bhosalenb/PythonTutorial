def search(list,n):
    for i in list:
        if i == n:
            return True
    else:
        return False

n=3
list = [11,2,3,21,22,4,55,6]

if search(list,n):
    print(" Found")
else:
    print("number not found")