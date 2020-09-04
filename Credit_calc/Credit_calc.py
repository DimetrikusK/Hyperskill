import math
import argparse
import json
import os
import sys
import tempfile


def check_parameters():
    global tmp
    flag = 0
    for i in tmp:
        if type(i) == float or type(i) == int:
            if int(i) < 0 or float(i) < 0:
                return False
        if i is None:
            flag += 1
    if flag >= 2:
        return False
    else:
        return True


def ft_diff():
    P = name_key.principal
    N = name_key.periods
    i = name_key.interest / (12 * 100)
    m = 1
    all_payment = 0
    for a in range(N):
        if a < range(N):
            D = math.ceil(P / N + i * (P - (P * (m - 1)) / N))
            all_payment += int(D)
            print("Month {}: paid out {}".format(m, int(D)))
            m += 1
    print("Overpayment = {}".format(all_payment - P))


def ft_overpayment():
    P = name_key.principal
    N = name_key.periods
    i = name_key.interest / (12 * 100)
    m = 1
    all_payment = 0
    for a in range(N):
        if a < range(N):
            D = (P / N + i * (P - (P * (m - 1)) / N))
            all_payment += D
            m += 1
    print("Overpayment = {}".format(math.ceil(int(all_payment - P))))


def ft_annuity():
    if name_key.payment is not None and name_key.periods is not None and name_key.interest is not None:
        i = name_key.interest / (12 * 100)
        A = name_key.payment
        N = name_key.periods
        P = math.floor(A / ((i * (1 + i) ** N) / ((1 + i) ** N - 1)))
        print("Your credit principal = {}!".format(int(P)))
        name_key.principal = P
        ft_overpayment()
    elif name_key.principal is not None and name_key.payment is not None and name_key.interest is not None:
        P = name_key.principal
        i = name_key.interest / (12 * 100)
        n = math.log(P / (P - i * P), 1 + i)
        ears = math.ceil(n) // 12
        month = math.ceil(n) % 12
        if math.ceil(n) // 12 == 0:
            print("You need 0 years and {} months to repay this credit!".format(int(month)))
        else:
             print("You need {} years and {} months to repay this credit!".format(int(ears), int(month)))


parser = argparse.ArgumentParser()
parser.add_argument('--type', default=None)
parser.add_argument("--principal", type=int, default=None)
parser.add_argument("--interest", type=float, default=None)
parser.add_argument("--payment", type=float, default=None)
parser.add_argument("--periods", type=int, default=None)
name_key = parser.parse_args()
tmp = [name_key.principal, name_key.interest, name_key.payment, name_key.periods]
if name_key.type == 'diff' or name_key.type == 'annuity':
    if not check_parameters():
        print('Incorrect parameters')
        exit()
    elif name_key.type == 'diff':
        ft_diff()
    elif name_key.type == 'annuity':
        ft_annuity()
else:
    print('Incorrect parameters')
    exit()



