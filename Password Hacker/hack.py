import socket
from sys import argv
import itertools


class Client:
    def __init__(self, host, port, tmp_pass):
        self.host = host
        self.port = int(port)
        self.tmp_pass = tmp_pass

    def __call__(self, *args, **kwargs):
        with socket.socket() as client_socket:
            client_socket.connect((self.host, self.port))
            for i in range(1, 10):
                for j in itertools.product(self.tmp_pass, repeat=i):
                    message = ''.join(j)
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024)
                    if response.decode() == 'Connection success!':
                        print(message)
                        exit()


if __name__ == '__main__':
    host, port = argv[1:]
    tmp_pass = 'abcdefghijklmnopqrstuvwxyz0123456789'
    run = Client(host, port, tmp_pass)
    run.__call__()
