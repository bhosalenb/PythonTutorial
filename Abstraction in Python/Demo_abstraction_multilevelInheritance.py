from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class B(A):
    def m1(self):
        print("I am in method m1")

class C(B):
    def m2(self):
        print("I am in method m2")

#b = B()

c = C()
c.m1()
c.m2()