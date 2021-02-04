
import quickfix
#from model.Message import Base, Types, __SOH__
import time

class MyApplication(quickfix.Application):
    sessionID = None
    def onCreate(self, sessionID):
        print("on Create")
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("Successful Logon to session '%s'." % sessionID.toString())
        return

    def onLogout(self,sessionID):
        print("logged out")
        return


    def toAdmin(self,message,sessionID):
        pass
        #msg = message.toString().replace(__SOH__, "|")


    def fromAdmin(self,message,sessionID):
        pass
        #msg = message.toString().replace(__SOH__, "|")

    def toApp(self,message,sessionID):
        pass
        #msg = message.toString().replace(__SOH__, "|")

    def fromApp(self,message,sessionID):
        beginString = quickfix.BeginString()
        msgType = quickfix.MsgType()

        message.getHeader().getField(beginString)
        message.getHeader().getField(msgType)

        symbol = quickfix.Symbol()
        side = quickfix.Side()
        ordType = quickfix.OrdType()
        orderQty = quickfix.OrderQty()
        price = quickfix.Price()
        clOrdID = quickfix.ClOrdID()
        message.getField(ordType)
        print("Order Type: ", ordType)
        print("Received Application message: ")
        #msg = message.toString().replace(__SOH__, "|")

    def run(self):
        while 1:
            time.sleep(2)
    def send_order(self):
        print("Creating the following order: ")

        order = quickfix.Message()

        #order.getHeader().setField(quickfix.BeginString(quickfix.BeginString_FIX42))
        order.getHeader().setField(quickfix.MsgType(quickfix.MsgType_NewOrderSingle))

        order.setField(quickfix.ClOrdID('123'))
        order.setField(quickfix.HandlInst('3'))
        order.setField(quickfix.Symbol("TCS"))
        order.setField(quickfix.Side(quickfix.Side_BUY))
        order.setField(quickfix.TransactTime())
        order.setField(quickfix.OrderQty(1001))
        order.setField(quickfix.OrdType(1))

        print(order.toString())
        print(self.sessionID)

        quickfix.Session.sendToTarget(order, self.sessionID)
