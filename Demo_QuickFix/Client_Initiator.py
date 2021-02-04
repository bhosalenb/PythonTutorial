import quickfix
import time
import sys
import quickfix42
from Demo_QuickFix import MyApplication
settings = quickfix.SessionSettings('client.cfg')
application = MyApplication.MyApplication()
storeFactory = quickfix.FileStoreFactory(settings)
logFactory = quickfix.FileLogFactory(settings)

initiator = quickfix.SocketInitiator(application, storeFactory, settings, logFactory)
initiator.start()
#application.run()

#while 1:
time.sleep(2)

if input() == '1':
    print("Sending order: ")
    application.send_order()
if input() == '2':
    sys.exit(0)

else:
    print("value input is 1 for order, 2 for exit")


initiator.stop()
