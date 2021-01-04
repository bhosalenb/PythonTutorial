# Program to print all the perfect square numbers between 1 to 100
import math

i=1
while i<=100:
   number=math.sqrt(i)
   check_int = number.is_integer()
   #print(check_int)
   if check_int==True:
       print(i)
   i=i+1





