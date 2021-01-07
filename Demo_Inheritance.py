# Multi level inheritance

class A:
    def feature1(self):
        print("I am in Feature1")
    def feature2(self):
        print("I am in Feature2")

class B(A):
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
