class Order:
    def __init__(self,lst1):
        #N,1,TCS,S,32,108
        #0,1,,2,,3,4,,,5
        self.Command = lst1[0]
        self.ordId=lst1[1]
        self.Sym = lst1[2]
        self.Side = lst1[3]
        self.Qty = lst1[4]
        self.Price = lst1[5]

    def new(self):
        print(type(self.Sym))

    def showBuy(self):
        if self.Side == 'B':
            print()
        print(self.Sym,',',self.Side,',',self.Qty,',',self.Price,end='')
    def showSell(self):
        print('--',self.Price,',',self.Qty,',',self.Side)

def query(buy_list, sell_list):
    #sorted_sell_list = sorted(sell_list, key=lambda x: x.)

    buy_list.sort(key=lambda x: x.Price, reverse=True)
    sell_list.sort(key=lambda x: x.Price)
    maxLength=0
    if len(buy_list) >len(sell_list):
        maxLength=len(buy_list)
    elif len(sell_list)>len(buy_list):
        maxLength=len(sell_list)
    else:
        maxLength=len(buy_list)
    for j in range(maxLength):
        if len(buy_list) > j:
            buy_list[j].showBuy()

        if len(sell_list) > j:
            sell_list[j].showSell()
def amend(buy_list, sell_list, oId,field,fldValue):
    orderList = []
    orderList = buy_list+sell_list

    for i in orderList:
        if i.ordId==oId:
            if field == 'P':
                i.Price=fldValue
            elif field == 'Q':
                i.Qty=fldValue
            else:
                print("Invalid Amend")
def cancel(buy_list,sell_list,oId):
    for i in orderList:
        if i.ordId == oId and i.Side == 'B':
            buy_list.remove(i)
        elif i.ordId == oId and i.Side == 'S':
            sell_list.remove(i)
        else:
            print("Invalid Cancel")


def match(buy_list, sell_list):
    flag = 0
    for i in buy_list:
        for j in sell_list:
            if i.Price == j.Price:
                print("Order matching done")
                flag = 1
                buy_list.remove(i)
                sell_list.remove(j)
                break
    if flag == 0:
        print("Match did not happened.")

if __name__ == '__main__':
    #n = int(input("Total no. of commands to enter:"))
    print("This program supports action like: N(New), A(Amend), X(Cancel), M(Match) or Q(Query)")
    print("New order Syntax: N,OrdId,SYM,Side,Price, Qty")
    buy_list = []
    sell_list = []

    while True:
        Str = input().upper().split(',')

        if Str[0] == 'N' and Str[3] == 'B':
            if Str[2].isnumeric():
                print('invalid Order')
            else:
                buy_list.append(Order(Str))
        elif Str[0] == 'N' and Str[3] == 'S':
            if Str[2].isnumeric():
                print('invalid Order')
            else:
                sell_list.append(Order(Str))
        elif Str[0] == 'A':
            ordId=Str[1]
            field=Str[2]
            fldValue=Str[3]
            amend(buy_list,sell_list,ordId,field,fldValue)
        elif Str[0] == 'X':
            ordId = Str[1]
            cancel(buy_list,sell_list,ordId)
        elif Str[0] == 'Q':
            query(buy_list, sell_list)

        elif Str[0] == 'M':
            match(buy_list, sell_list)
        else:
            break





