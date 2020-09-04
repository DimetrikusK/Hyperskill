import random
import sqlite3

conn = sqlite3.connect("card.s3db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS card (
                id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                `number`    TEXT,
                pin         TEXT,
                balance     INTEGER DEFAULT 0
                )""")
conn.commit()

#
# c.execute("SELECT * FROM card")  # FOR DEBUG
# print(c.fetchall())  # FOR DEBUG


def card_db(card, pincod):
    params = (card, pincod)
    c.execute("INSERT INTO card (`number`, `pin`) VALUES (?, ?)", params)
    conn.commit()
    main()


def gen_number_card():
    global card, pin
    print("""Your card has been created
Your card number:""")
    for i in range(9):
        top = str(random.randint(0, 9))
        card_number.append(top)
    return card_number


def luna(card_number):
    count = 0
    number = 0
    check = 0
    for i in card_number[0:15]:
        i = int(i)
        if check % 2 == 0:
            i *= 2
            if i > 9:
                i -= 9
            count += i
        elif i <= 9:
            count += i
        check += 1
    if len(card_number) == 16:
        count += int(card_number[15])
        if count % 10 == 0:
            return 1
        else:
            return 0
    elif len(card_number) == 15:
        if count % 10 == 0:
            count = 0
        while count % 10 != 0:
            count += 1
            number += 1
        number = str(number)
        card_number.append(number)
        card = ''.join(card_number)
        return card
    else:
        return 0


def pin():
    global pincod
    for i in range(4):
        top = random.randint(0, 9)
        card_pin.append(str(top))
        pincod = ''.join(card_pin)
    print("Your card PIN:")
    print(pincod)
    return pincod


def log_acc():
    input_card = input("Enter your card number:\n")
    input_pin = input("Enter your PIN:\n")
    val = (input_card, input_pin)
    c.execute("SELECT * FROM card WHERE `number` = ? AND pin = ?", val)
    auth = c.fetchone()
    if not auth:
        print("Wrong card number or PIN!\n")
        main()
    else:
        print("You have successfully logged in!\n")
        account(input_card)


def account(card_number):
    push = int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""))
    if push == 1:
        balance(card_number)
    elif push == 2:
        add_income(card_number)
    elif push == 3:
        transfer(card_number)
    elif push == 4:
        close_acc(card_number)
    elif push == 5:
        main()
    elif push == 0:
        exit()


def balance(card_number):
    val = (card_number,)
    c.execute("SELECT balance FROM card WHERE `number` = ?", val)
    balance = c.fetchone()
    print("\nBalance:", balance[0])
    account(card_number)


def add_income(card_number):
    update = int(input("Enter income:\n"))
    val = (update, card_number)
    c.execute("UPDATE card SET balance = balance + ? WHERE `number` = ?", val)
    conn.commit()
    print("Income was added!\n")
    account(card_number)


def chek_valid_card(transfer_number, card_number):
    if card_number == transfer_number:
        print("You can't transfer money to the same account!\n")
        return 0
    if not luna(transfer_number):
        print("Probably you made mistake in the card number. Please try again!\n")
        return 0
    val = (transfer_number, )
    c.execute("SELECT * FROM card WHERE `number` = ?", val)
    card_in_db = c.fetchone()
    if not card_in_db:
        print("Such a card does not exist.\n")
        return 0
    return 1


def transfer(card_number):
    global transfer_money
    print("Transfer\nEnter card number:")
    transfer_number = input()
    if not chek_valid_card(transfer_number, card_number):
        account(card_number)
    try:
        transfer_money = int(input("Enter how much money you want to transfer:\n"))
    except ValueError:
        print("Input is a integer number.")
    val = (card_number, )
    c.execute("SELECT balance FROM card WHERE `number` = ?", val)
    user_balance = c.fetchone()
    if user_balance[0] - transfer_money < 0:
        print("Not enough money!")
        account(card_number)
    else:
        take = (transfer_money, card_number)
        c.execute("UPDATE card SET balance = balance - ? WHERE `number` = ?", take)
        give = (transfer_money, transfer_number)
        c.execute("UPDATE card SET balance = balance + ? WHERE `number` = ?", give)
        conn.commit()
        print("Success!\n")
    account(card_number)


def close_acc(card_number):
    val = (card_number, )
    c.execute("DELETE FROM card WHERE `number` = ?", val)
    conn.commit()
    print("The account has been closed!\n")


def main():
    global card_number
    global card_pin
    while True:
        push = int(input("""1. Create an account
2. Log into account
0. Exit
"""))
        if push == 1:
            card_number = ['4', '0', '0', '0', '0', '0']
            card_pin = []
            new_number = gen_number_card()
            new_card = luna(new_number)
            print(new_card)
            new_pin = pin()
            card_db(new_card, new_pin)
        elif push == 2:
            log_acc()
        else:
            exit()


main()
