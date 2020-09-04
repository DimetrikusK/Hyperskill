import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', default=None)
# parser.add_argument("--principal", type=int, default=None)
# parser.add_argument("--interest", type=float, default=None)
# parser.add_argument("--payment", type=float, default=None)
# parser.add_argument("--periods", type=int, default=None)
name_key = parser.parse_args()

if name_key.type == 'diff' and name_key.payment is not None:
    print('Incorrect parameters')
if name_key.type == 'diff':
    print(name_key.principal * 2)
elif name_key.type is "annuity":
    print(2)
else:
    print('Incorrect parameters')


def count_of_months():
    print("Enter credit principal:")
    principal = int(input())
    print("Enter monthly payment:")
    payment = int(input())
    print("Enter credit interest:")
    proc = float(input())
    i = proc / (12 * 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    ears = math.ceil(n) // 12
    month = math.ceil(n) % 12
    if math.ceil(n) // 12 == 0:
        print("You need 0 years and {} months to repay this credit!".format(month))
    else:
        print("You need {} years and {} months to repay this credit!".format(ears, month))


def annuity_monthly_payment():
    print("Enter credit principal:")
    principal = int(input())
    print("Enter count of periods:")
    n = int(input())
    print("Enter credit interest:")
    proc = float(input())
    i = proc / (12 * 100)
    a = math.ceil(principal * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print("Your annuity payment = {}!".format(a))


# def monthly_payment(): #ежемесячный платеж
#     print("Enter monthly payment:")
#     a = float(input())
#     print("Enter count of periods:")
#     n = int(input())
#     print("Enter credit interest:")
#     proc = float(input())
#     i = proc / (12 * 100)
#     p = math.floor(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
#     print("Your credit principal = {}!".format(p))


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
        ft_diff(name_key)
    elif name_key.type == 'annuity':
        ft_annuity(name_key)
else:
    print('Incorrect parameters')
    exit()

