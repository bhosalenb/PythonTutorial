import socket

cs = socket.socket()

cs.connect(('localhost',1234))
name = input("Enter name of the Client")
cs.send(bytes(name,'utf-8'))
print(cs.recv(1024).decode())

