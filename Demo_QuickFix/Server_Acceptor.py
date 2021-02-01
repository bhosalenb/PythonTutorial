import quickfix
from Demo_QuickFix import MyApplication
settings = quickfix.SessionSettings('server.cfg')
application = MyApplication.MyApplication()
storeFactory = quickfix.FileStoreFactory(settings)
logFactory = quickfix.FileLogFactory(settings)
acceptor = quickfix.SocketAcceptor(application,storeFactory,settings,logFactory)

#fix.Session.sendToTarget()
acceptor.start()
application.run()

acceptor.stop()
