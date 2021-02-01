
import quickfix
import time

class MyApplication(quickfix.Application):
    sessionID = None
    def onCreate(self, sessionID):
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        return

    def onLogout(self,sessionID):
        return


    def toAdmin(self,message,sessionID):
        msg = message.toString().replace(__SOH__, "|")

    def fromAdmin(self,message,sessionID):
        msg = message.toString().replace(__SOH__, "|")

    def toApp(self,message,sessionID):
        msg = message.toString().replace(__SOH__, "|")

    def fromApp(self,message,sessionID):
        msg = message.toString().replace(__SOH__, "|")

    def run(self):
        while 1:
            time.sleep(2)