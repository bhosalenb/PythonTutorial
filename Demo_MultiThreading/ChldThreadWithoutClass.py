#Creating a child thread without using any class

import threading
def display():
    for i in range(10):
        print("Child Thread: ", threading.current_thread().getName())
t = threading.Thread(target=display)

t.start()

for i in range(10):
    print("Main Thread:", threading.current_thread().getName())