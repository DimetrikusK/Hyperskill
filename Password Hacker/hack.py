import socket
from sys import argv
import itertools


class Client:
    def __init__(self, host, port, tmp_pass):
        self.host = host
        self.port = int(port)
        self.tmp_pass = tmp_pass

    def __call__(self):
        with socket.socket() as client_socket:
            client_socket.connect((self.host, self.port))
            for word in password_tmp:
                mixed_case = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word)))
                for message in mixed_case:
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024)
                    if response.decode() == 'Connection success!':
                        print(message)
                        exit()


class Password:
    def __init__(self):
        self.password_tmp = str()

    def parsing_password(self):
        with open('passwords.txt', 'r', encoding='utf-8')as file:
            for password in file:
                self.password_tmp += password
            self.password_tmp = self.password_tmp.split('\n')
            self.password_tmp = [x for x in self.password_tmp if x.isalpha()]

        return self.password_tmp


if __name__ == '__main__':
    host, port = input(), input()
    password_tmp = Password()
    password_tmp = password_tmp.parsing_password()
    run = Client(host, port, password_tmp)
    run.__call__()
