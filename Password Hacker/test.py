import json
import itertools

tmp = 'a'
print(tmp[:-1])

string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# for word in password_tmp:
#     mixed_case = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word)))
#     for message in mixed_case:
#         client_socket.send(message.encode())
#         response = client_socket.recv(1024)
#         if response.decode() == 'Connection success!':
#             print(message)
#             exit()

# def brute_force_login(self):
#     for login in self.tmp_login:
#         self.lp_json["login"] = login
#         client_socket.send(message.encode())
#         response = client_socket.recv(1024)
#         if response.decode() == 'Connection success!':