
list1=[10,20,30,40,50]
list2=["apple","strawberry","pineapples"]
list3=[101,"Sara",67.67,True]
print(list1)
print(list1[2:4]) # [30,40]
print(list1[3]) # 40
print(list1[3:]) # [40,50]
print(list1[:3]) # [10,20,30]

# list - mutable
list1[3]=1000
print(list1) #[10,20,30,1000,50]
print("*************************************")
list1=[10,20,30,40,50]
list1[2:4]=[100]

print(list1)
print("*************************************")

list1=[10,20,30,40,50]
list1[2:4]=[100,200,300,400,500]
print(list1)

list1=[10,20,30,40,50]
list1[2:4]=["hello",False]
print(list1)

list1=[10,20,30,40,50]
del list1[2]
print(list1)

list1=[10,20,30,40,50]
list1.remove(50)
print(list1)

list1=[10,20,30,40,50]
print("Popped out element:",list1.pop()) #50
print(list1)
#IndexError: pop index out of range
list1=[10,20,30,40,50]
print("Popped out element:",list1.pop(1)) # 20;
print(list1)
# 0 1 2 3 4
#-5-4-3-2-1
list1=[10,20,30,40,50]
print("Popped out element:",list1.pop(-3)) # 30
print(list1)

list1=[10,20,30,40,50]
print(list1[-3]) # 30

list1=[10,20,30,40,50]
list1.append(60)
print("Appended list",list1) #[[10,20,30,40,50,60]

# insert at a particular pos
list1.insert(3,35)
print(list1) # [10,20,30,35,40,50,60]

list1=[10,20,30,40,50]
list1.append([60,70])
print("Appended list",list1) # [10,20,30,40,50,[60,70]]

list1=[10,20,30,40,50]
list1.extend([60,70])
print("Appended list",list1) # [10,20,30,40,50,60,70]

list1.extend(list2)
print(list1)


list1=[101,20,10,111,25,99]
list1.sort()
print(list1) #[10,20,25,99,101,111]
list1.reverse()
print(list1)

'''
list1=[101,20,10,111,True,"hello"]
list1.sort()
print(list1) # error
'''

list1=[101,20,10,111,True]
list1.sort()
print(list1) # [True, 10,20,101,111]

list2.sort()
print(list2) #

list1=[11,2,1,3,1,3,1]
print(list1.count(1))

print(list1.index(1))

# Tuples
# immutable

tuple1=(10,20,30,40,50)
print(tuple1)
print(tuple1[0]) # 10
print(tuple1[2:4]) # 30,40

# tuple1[0]=1000; error

#del tuple1[0]

del tuple1 # successful

tuple1=(1,2,3,4,5)
# use cases
# gender =("M","F","O")
tuple2=(1,"M",77)
print(tuple2)