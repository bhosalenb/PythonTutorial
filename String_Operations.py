
#"good morning"
#"01234567891011
str1 = "good morning"
print(str1)
print(str1[0]) # g
print(str1[2:5]) #  "od "
print(str1[2:]) #  "od morning"
print(str1[:5]) #  "good "
print(str1*3) # 3 times good morning
print(str1 + "Wells")

str1 = str1.upper()
print(str1)
print(str1.title())
# upper lower title capitalise
print("*******************************************")
str2="123"
print(str2.isdigit()) # True
print("*******************************************")
#index
#malayalam
#012345678
str1 = "malayalam"
# Program to print the various pos where a is there in the string
# traverse through the string
pos1=str1.index("a") # return the pos of the first occurence of the substring in the given string; 1
'''
while(pos1 >= 0):
    print(pos1)
    pos1=str1.index("a",pos1 + 1)
'''
pos1=str1.find("a") # return the pos of the first occurence of the substring in the given string; 1

while(pos1 >= 0):
    print(pos1)
    pos1=str1.find("a",pos1 + 1)

print("Position of z in str1",str1.find("z"))
print("Position of l in str1",str1.find("l",3,5))  # -1
print("Position of y in str1",str1.find("y",0,4)) # -1;4 ;
str1="malayaLAm"
print(len(str1)) #9
# A - 65
# a - 97
print(max(str1)) #  y
print(min(str1)) #  A


print(str1.startswith("mal")) # true
print(str1.startswith("lay",2)) # true

str1="good morning Wells Fargo"
print(str1.split())
print(str1.split("o"))
print(str1.split(" ", 2))
