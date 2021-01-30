import threading
import time
def job1():
    print("executed by t1")
    t2 = threading.Thread(target=job2)
    print("t2 status: ", t2.isDaemon())
    t2.start()

def job2():
    print("executed by t2")

t1 = threading.Thread(target=job1)
print("t1 status: ", t1.isDaemon())

t1.setDaemon(True)

print("t1 status After change: ", t1.isDaemon())

t1.start()
time.sleep(2)