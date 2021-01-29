import threading
class Test:
    def m1(self):
        for i in range(10):
            print("Child Thread")

obj = Test()
t = threading.Thread(target=obj.m1)
t.start()

for i in range(10):
    print("Main Thread")