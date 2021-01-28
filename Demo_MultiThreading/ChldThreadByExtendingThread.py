#Creating a child thread by extending Thread class / By overriding run Method:
import threading
class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print("Child Thread:")

t = MyThread()
t.start()

for i in range(10):
    print("Main Thread: ")
