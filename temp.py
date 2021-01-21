'''
N:
N,TCS,B,32,104
N,TCS,B,32,106
N,TCS,B,32,103
N,TCS,S,32,107
N,TCS,S,32,106
N,TCS,S,32,108
Q
M

Q:

N , AAA , B , 1 , 105   -   105, S
N , AAA , B , 1 , 104   -   107, S
N , AAA , B , 1 , 103   -   108, S

'''
str = 'n,aaa,b,1,111'
lst1= str.split(',')
print(lst1[1].isnumeric())


class Order:
    def __init__(self, ....):
        pass

    def modify(self):
        pass

    def cancel(self):
        pass

    def match(self):
        pass

class Trading:
    def sell(self, orderToSell):
        pass
    def buy(self, orderToBuy):
        pass
    def query(self, buyOrders, sellOrders):
        buyOrders.sort(key: )

if __name__ == "__main__":
    # input
    # for each input line, create a new order object
    # Also create a single object of the trading class
    Trading t = Trading()
    t.query(orderToBuy, .....)