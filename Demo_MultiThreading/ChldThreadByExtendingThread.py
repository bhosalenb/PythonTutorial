import threading
class MyThread(threading.Thread):
    for i in range(10):
        print("Child Thread:")

t = threading.Thread()
t.start()

for i in range(10):
    print("Main Thread: ")
