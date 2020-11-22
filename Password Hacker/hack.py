import socket
from sys import argv

host, port, message = argv[1:]
with socket.socket() as client_socket:
    client_socket.connect((host, int(port)))
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(response.decode())