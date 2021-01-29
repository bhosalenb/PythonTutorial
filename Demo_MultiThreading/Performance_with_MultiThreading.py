import threading
import time

def doubles(numbers):
    for i in numbers:
        print("doubles: ", i *2)

def squares(numbers):
    for i in numbers:
        print("squares=", i*i)

numbers = [1,2,3,4,5,6,7,8,9]
t1 = threading.Thread(target=doubles,args=(numbers,))
t2 = threading.Thread(target=squares,args=(numbers,))
start_time = time.time()

t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()

print("Total time taken to execute 2 functions: ", end_time-start_time)
