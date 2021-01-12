names = ['Nitin', 'Mahesh', 'Vijay', 'Gajanan']
companies = ['Wells', 'Microsoft', 'Master Card', 'HSBC']

lst1= list(zip(names, companies))
tuple1 = tuple(zip(names, companies))
set1 = set(zip(names, companies))

dict1 = dict(zip(names, companies))

print("zipped list: ", lst1)
print("zipped tuple: ",tuple1)
print("zipped Set: ",set1)
print("zipped Dict: ",dict1)

print("#"*50)
for i in zip(names, companies):
    print(i)