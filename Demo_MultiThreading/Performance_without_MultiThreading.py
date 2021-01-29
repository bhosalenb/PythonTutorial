import time
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print("doubles= ", i * 2)

def squares(numbers):
    for i in numbers:
        time.sleep(1)
        print("Squares= ", i * i)

numbers = [1,2,3,4,5,6,7,8,9]
start_time = time.time()
doubles(numbers)
squares(numbers)
end_time = time.time()

print("Total time taken to execute 2 functions: ", end_time-start_time)