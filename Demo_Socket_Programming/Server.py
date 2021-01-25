import socket

ss = socket.socket()
ss.bind(('localhost',1234))

ss.listen(3)
print("Waiting for the Clients: ")
while True:
    cs, addr = ss.accept()
    c_name = cs.recv(1024).decode()
    print('Connection established with ', c_name)
    cs.send(bytes('Welcome to the Server space','utf-8'))
    cs.close()
