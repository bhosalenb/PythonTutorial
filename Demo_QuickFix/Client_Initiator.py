import quickfix
from Demo_QuickFix import MyApplication
settings = quickfix.SessionSettings('client.cfg')
application = MyApplication.MyApplication()
storeFactory = quickfix.FileStoreFactory(settings)
logFactory = quickfix.FileLogFactory(settings)

initiator = quickfix.SocketInitiator(application,storeFactory,settings,logFactory)
initiator.start()
application.run()

initiator.stop()


