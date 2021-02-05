
import quickfix
#from model.Message import Base, Types, __SOH__
import time

class MyApplication(quickfix.Application):
    sessionID = None
    def onCreate(self, sessionID):
        print("calling onCreate method from server.....session created")
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("calling onLogon method from server.....Successful Logged into session '%s'." % sessionID.toString())
        return

    def onLogout(self,sessionID):
        print("calling logout method from server")
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

        #symbol = message.getField(quickfix.Symbol())
        side = message.getField(quickfix.Side())
        ordType = quickfix.OrdType()
        orderQty = message.getField(quickfix.OrderQty())
        price = quickfix.Price()
        clOrdID = quickfix.ClOrdID()
        message.getField(ordType)

        print("Received message from Client: ", message.toString())

        executionReport = quickfix.Message()
        executionReport.getHeader().setField(quickfix.MsgType(quickfix.MsgType_ExecutionReport))

        executionReport.setField(quickfix.OrderID('41'))
        executionReport.setField(quickfix.ExecID('51'))
        executionReport.setField(quickfix.OrdStatus(quickfix.OrdStatus_FILLED))
        executionReport.setField(quickfix.Symbol("TCS"))
        executionReport.setField(quickfix.Side(quickfix.Side_BUY))
        executionReport.setField(quickfix.OrdType(quickfix.OrdType_MARKET))

        executionReport.setField(quickfix.OrderQty(1001))
        executionReport.setField(quickfix.CumQty(1001))
        executionReport.setField(quickfix.AvgPx(33.33))
        executionReport.setField(quickfix.LeavesQty(0))
        executionReport.setField(quickfix.ExecType(quickfix.ExecType_FILL))
        executionReport.setField(quickfix.ExecTransType(quickfix.ExecTransType_NEW))

        quickfix.Session.sendToTarget(executionReport, sessionID)
        print("Execution msg sent to Client: ", executionReport.toString())

    def run(self):
        while 1:
            time.sleep(2)
