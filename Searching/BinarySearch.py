# FOr binary search, list should be already sorted
def bSearch(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l + u)//2
        if list[mid] == n:
            return True
        elif list[mid] < n:
            l = mid
        else:
            u = mid


list = [2,12,13,15,23,25,33,43]
######,,0,,1,,2,,3,,4,,5,,6,,7
n=3
if bSearch(list,n):
    print("Found")

else:
    print("not Found")