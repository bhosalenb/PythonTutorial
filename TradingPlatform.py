class Order:
    def __init__(self,lst1):
        self.Command = lst1[0]
        self.Sym = lst1[1]
        self.Side = lst1[2]
        self.Price = lst1[4]
        self.Qty = lst1[3]

    def new(self):
        # N,SYM,Side,Price, Qty
        print(type(self.Sym))
        #if self.Sym !=


    def amend(self):
        pass
    def cancel(self):
        pass
    def match(self):
        pass
    def showBuy(self):
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
        buy_list[j].showBuy()
        sell_list[j].showSell()
def match(buy_list, sell_list):
    for i in buy_list:
        for j in sell_list:
            if i.Price == j.Price:
                print("Order matching done")
                buy_list.remove(i)
                sell_list.remove(j)
                break
    else:
        print("Match did not happened.")


if __name__ == '__main__':
    n = int(input("Total no. of commands to enter:"))
    print("This program supports action like: N(New), A(Amend), X(Cancel), M(Match) or Q(Query)")
    print("New order Syntax: N,SYM,Side,Price, Qty")
    buy_list = []
    sell_list = []

    while n >0 :
        lst1 = input().upper().split(',')

        if lst1[0] == 'N' and lst1[2] == 'B':
            if lst1[1].isnumeric():
                print('invalid Order')
            else:
                buy_list.append(Order(lst1))
        elif lst1[0] == 'N' and lst1[2] == 'S':
            if lst1[1].isnumeric():
                print('invalid Order')
            else:
                sell_list.append(Order(lst1))
        elif lst1[0] =='Q':
            query(buy_list, sell_list)

        elif lst1[0] == 'M':
            match(buy_list,sell_list)

        n -= 1



