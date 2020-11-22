import socket

client_socet = socket.socket()
address = ('127.0.0.1', 9090)
client_socet.connect(address)
