#List of odd and even nos:

def analyse_Odd_Even(lst):
    even=[]
    odd=[]

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

lst=[11,22,23,25,6,68,67,9,42,7]
odd,even=analyse_Odd_Even(lst)
print("odd list:",odd)
print("even list:", even)
