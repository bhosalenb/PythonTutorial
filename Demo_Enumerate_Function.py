# Define a function that take two arguments:
#1. list cointaining string
#2. string that want to find in your list
# and this function will return the index of string in your list and if string is not present then return -1


def Enumerate_Function(str_list, str1):

    for pos,item in enumerate(str_list):
        if item == str1:
            return pos
    return  -1

str_list = ['nitin','jay','mahesh', 'vijay']
str1 = 'jay'

print(Enumerate_Function(str_list,str1))