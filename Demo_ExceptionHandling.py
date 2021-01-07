a=5
b=0

try:
    c=a/b
    print(c)
except Exception as e:
    print("value of b cannot be zero")

finally:
    print("THis must be printed at EOF")