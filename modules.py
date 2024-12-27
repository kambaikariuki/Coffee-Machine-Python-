cups = 0
water = 400
milk = 540
beans = 120
money = 550
disposable_cups = 9

# Done
def make_expresso(water, beans, disposable_cups, money) :
    coffee = [water // 250, beans // 16]
    coffee_cups = min(coffee)
    if coffee_cups != 0:
        coffee_cups = 1
        print("I have enough resources, making you a coffee!\n")
        water = water - (coffee_cups * 250)
        beans = beans - 16
        disposable_cups = disposable_cups - coffee_cups
        money = money + (coffee_cups * 4)
        print_status(water, milk, beans, disposable_cups, money)
        return water, beans, disposable_cups, money
           
    else:
        print("Sorry, not enough resources!\n")
        exit
    return water, beans, disposable_cups, money
# Done
def make_latte(water, milk, beans, disposable_cups, money) :
    coffee = [water // 350, milk // 75, beans // 20]
    coffee_cups = min(coffee)
    if coffee_cups != 0:
        coffee_cups = 1
        print("I have enough resources, making you a coffee!\n")
        water = water - (coffee_cups * 350)
        beans = beans - (coffee_cups * 16)
        milk = milk - (coffee_cups * 75)
        disposable_cups = disposable_cups - coffee_cups
        money = money + (coffee_cups * 7)
        print_status(water, milk, beans, disposable_cups, money)
        return water, milk, beans, disposable_cups, money
           
    else:
        print("Sorry, not enough resources!\n")
        exit
    return water, milk, beans, disposable_cups, money

# Done
def make_cappucino(water, milk, beans, disposable_cups, money) :
    coffee = [water // 200, milk // 100, beans // 12]
    coffee_cups = min(coffee)
    if coffee_cups != 0:
        coffee_cups = 1
        print("I have enough resources, making you a coffee!\n")
        water = water - (coffee_cups * 200)
        beans = beans - (coffee_cups * 12)
        milk = milk - (coffee_cups * 100)
        disposable_cups = disposable_cups - coffee_cups
        money = money + (coffee_cups * 6)
        print_status(water, milk, beans, disposable_cups, money)
        return water, milk, beans, disposable_cups, money
           
    else:
        print("Sorry, not enough resources!\n")
        exit
    return water, milk, beans, disposable_cups, money

# Done
def fill_coffee(water, milk, beans, disposable_cups) :
    added_water = int(input("Write how many more ml of water you want to add:\n"))
    added_milk = int(input("Write how many more ml of milk you want to add:\n"))
    added_beans = int(input("Write how many more grams of coffee you want to add:\n"))
    added_disposable_cups = int(input("Write how many more disposable cups you want to add:\n"))
    water = water + added_water
    milk = milk + added_milk
    beans = beans + added_beans
    disposable_cups = disposable_cups + added_disposable_cups
    return water, milk, beans, disposable_cups

# Done
def take_money(money) :
    print(f"I gave you ${money}\n")
    money = 0
    return money

def print_status(water, milk, beans, disposable_cups, money) :
    print(f"""\nThe coffee machine has:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{disposable_cups} disposable cups
${money} of money\n""")