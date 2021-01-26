
import quickfix as fix

class FixFunctions:
    def onCreate(self, sessionID):
        pass
    def onLogon(self, sessionID):
        pass
    def onLogout(self,sessionID):
        pass
    def fromApp(self,message,sessionID):
        pass
    def toApp(self,message,sessionID):
        pass
    def fromAdmin(self,message,sessionID):
        pass
    def toAdmin(self,message,sessionID):
        pass

settings = fix.SessionSettings('FixSettings.cfg')
Application = fix.MyApplication()
storeFactory = fix.FileStoreFactory(settings)
logFactory = fix.FileLogFactory(settings)

acceptor = fix.SocketAcceptor(Application,storeFactory,settings,logFactory)

acceptor.start()

