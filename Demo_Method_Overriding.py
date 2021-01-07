class A:
    def show(self):
        print("in class A")

class B(A):
    def show(self):
        print("in class B")

a1 = A()
b1 = B()
a1.show()
b1.show()