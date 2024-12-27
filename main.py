from modules import *

while True:
        
    action = input("Write action (buy, fill, take, remaining, exit): \n")
    if action == "buy":
        buy = input("\nWhat do you want to buy?\n 1. Expresso\n 2. Latte\n 3. Cappucino\n 4. Back to main menu\n")
        if buy == "1":
            water,beans,disposable_cups, money = make_expresso(water, beans, disposable_cups, money)
        elif buy == "2":
            water,beans, milk, disposable_cups, money = make_latte(water, beans, milk, disposable_cups, money)
        elif buy == "3":
            water,beans, milk, disposable_cups, money = make_cappucino(water, milk, beans, disposable_cups, money)
        elif buy == "4":
            continue
        else:
            print("\nWrong input")
    elif action == "fill":
        water,milk, beans, disposable_cups = fill_coffee(water, milk, beans, disposable_cups)
    elif action == "take":
        money = take_money(money)
    elif action == "remaining":
        print_status(water, milk, beans, disposable_cups, money)
    elif action == "exit":
        break
    else:
        print("Wrong input")

