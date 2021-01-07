class Student:
    school = 'TJPV, Vairag'

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def avg(self,marks):
        sum=0
        for i in self.marks:
            sum=sum+i
        a=sum/len(marks)
        return a
    @classmethod
    def info(cls):
        return cls.school

    #def sortAge(self):

s1 = Student('Nitin',34,[91,94,97])
s2 = Student('Jaysing',39,[96,93,99])
s3 = Student('Viraj',9,[96,93,99])
s4 = Student('Shivanjali',3,[96,93,99])
s5 = Student('Sapana',29,[96,93,99])

print("Avg marks of s1: ", s1.avg(s1.marks))
print("Avg marks of s2: ", s2.avg(s2.marks))

print(Student.info())
