# Multi level inheritance

class A:
    def __init__(self):
        print("I am class A constructor")
    def feature1(self):
        print("I am in Feature1")
    def feature2(self):
        print("I am in Feature2")

class B(A):
    def __init__(self):
        print("I am class B constructor")
    def feature3(self):
        print("I am in Feature3")
    def feature4(self):
        print("I am in Feature4")

class C(B):

    def feature5(self):
        print("I am in Feature5")
    def feature6(self):
        print("I am in Feature6")

a = A()
b = B()
b.feature1()
c = C()
c.feature6()
