class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = +9
    money = 550

    def __init__(self):
        self.coffee = None

    def fill_coffee(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def ft_take(self):
        print("I give you $" + str(self.money))
        self.money = 0

    def ft_remaining(self):
        print("\nThe coffee machine has: ")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")

    def buy_coffee(self, coffee):
        if coffee == 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.disposable_cups -= 1
        elif coffee == 2:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
            self.disposable_cups -= 1
        elif coffee == 3:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.disposable_cups -= 1

    def valid(self, coffee):
        if coffee == 1 and self.water - 250 < 0 or coffee == 2 and self.water - 350 < 0 \
                or coffee == 3 and self.water - 200 < 0:
            print("\nSorry, not enough water!")
        elif coffee == 2 and self.milk - 75 < 0 or coffee == 3 and self.milk - 100 < 0:
            print("\nSorry, not enough milk!")
        elif coffee == 1 and self.coffee_beans - 16 < 0 or coffee == 2 and self.coffee_beans - 20 < 0\
                or coffee == 3 and self.coffee_beans - 12 < 0:
            print("\nSorry, not enough coffee_beans!")
        elif self.disposable_cups == 0:
            print("\nSorry, not enough disposable_cups!")
        else:
            print("\nI have enough resources, making you a coffee!")
            self.buy_coffee(coffee)


my_class = CoffeeMachine()
while True:
    push = input("\nWrite action (buy, fill, take, remaining, exit): ")
    while push == "buy":
        push = (input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if push == "back":
            break
        else:
            my_class.valid(int(push))
    if push == "fill":
        my_class.fill_coffee()
    elif push == "take":
        my_class.ft_take()
    elif push == "remaining":
        my_class.ft_remaining()
    elif push == "exit":
        break



