import json
import logging

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

    def showBuy(self):
        if self.Side == 'B':
            print()
        print(self.ordId,',',self.Sym,',',self.Side,',',self.Qty,',',self.Price,end='')
    def showSell(self):
        print('--',self.Price,',',self.Qty,',',self.Side,',',self.ordId)

def newOrder(Str):
    Str = Str.upper().split(',')
    if Str[2].isnumeric():
        print('invalid Order')
    else:         
        if Str[3] == 'B':
            flag1 = 0        
            for k in buy_list:
                if k.ordId == Str[1]:
                    flag1 = 1
            if flag1 == 0:
                buy_list.append(Order(Str))
            else:
                logging.debug("Duplicate order Id")
        elif Str[3] == 'S':
            flag2 = 0
            for k in sell_list:
                if k.ordId == Str[1]:
                    flag2 = 1
            if flag2 == 0:
                sell_list.append(Order(Str))

def query(buy_list, sell_list):

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
    orderList = buy_list+sell_list
    for i in orderList:
        if i.ordId == oId and i.Side == 'B':
            buy_list.remove(i)
            break
        elif i.ordId == oId and i.Side == 'S':
            sell_list.remove(i)
            break
    else:
        print("Invalid Cancel")


def match(buy_list, sell_list):
    flag = 0
    for i in buy_list:
        for j in sell_list:
            if i.Price == j.Price:
                print("Order matched successfully ")
                flag = 1
                buy_list.remove(i)
                sell_list.remove(j)
                break
    if flag == 0:
        print("There are no orders to match.")

if __name__ == '__main__':
    #n = int(input("Total no. of commands to enter:"))
    print("This program supports action like: N(New), A(Amend), X(Cancel), M(Match) or Q(Query. Use below Syntax for each actrion:)")
    print("New order: N,OrdId,SYM,Side,Price, Qty")
    print("Amend: A,Order ID,Field(P or Q), Field Value")
    print("Cancel: X,Order ID")
    print("Query: Q")
    print("Match: M")
    logging.basicConfig(filename='Demo_OrderMatcherEngine/OrderMatcher.log',level=logging.DEBUG,format='%(asctime)s::%(levelname)s::%(message)s')
    buy_list = []
    sell_list = []

    while True:
        Str = input()

        if Str[0] == 'N':
            newOrder(Str)
        elif Str[0] == 'U':
            with open("../Orders_List.json", 'r') as fr:
                data_dict = json.load(fr)
                for i in data_dict['Orders']:
                    str1 = i['Command']+','+str(i['Ord_ID'])+','+i['Symbol']+','+i['Side']+','+str(i['Qty'])+','+str(i['Price'])
                    newOrder(str1)

        elif Str[0] == 'A':
            Str = Str.upper().split(',')
            ordId=Str[1]
            field=Str[2]
            fldValue=Str[3]
            amend(buy_list,sell_list,ordId,field,fldValue)
        elif Str[0] == 'X':
            Str = Str.upper().split(',')
            ordId = Str[1]
            cancel(buy_list,sell_list,ordId)
        elif Str[0] == 'Q':
            query(buy_list, sell_list)

        elif Str[0] == 'M':
            match(buy_list, sell_list)
        else:
            break





