class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
        print(self.name,self.id)
    class Laptop:
        def __init__(self,cpu,ram):
            self.cpu=cpu
            self.ram = ram
        def show(self):
            print(self.cpu,self.ram)


s1 = Student('Nitin',33)
s2 = Student('Viraj',40)

s2.show()

L2 = Student.Laptop('i5', '8GB')
L2.show()
s1.show()

