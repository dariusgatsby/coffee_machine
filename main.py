from machine import MENU, resources

MENU = MENU
print(MENU)

profit = 0
quarters = .25
dimes = .10
nickels = .05
pennies = .01
# Ask user what kind of coffee they want, collect money

coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
print('Please insert coins.')
quarters_given = float(input('how many quarters?: '))
dimes_given = float(input("how many dimes?: "))
nickels_given = float(input("how many nickels?: "))
pennies_given = float(input("how many pennies?: "))

profit = (quarters_given * quarters) + (dimes_given * dimes) + (nickels_given * nickels) + (pennies_given * pennies)
print(profit)


def check_money(coffee_type, money_given):
    if coffee_choice == 'espresso':
        espresso_price = MENU['espresso']['cost']
        if profit >= espresso_price:
            change = profit - espresso_price
            print(f"Thank you your change is ${round(change)}")
        elif profit == espresso_price:
            print(f"Thank you! Enjoy your coffee")
        else:
            difference = espresso_price - profit
            print(f"Not enough money, money refunded. Put in {difference} more.")
    elif coffee_choice == 'latte':
        latte_price = MENU['latte']['cost']
        if profit >= latte_price:
            change = profit - latte_price
            print(f"Thank you your change is ${round(change)}")
        elif profit == latte_price:
            print(f"Thank you! Enjoy your coffee")
        else:
            difference = latte_price - profit
            print(f"Not enough money, money refunded. Put in {difference} more.")
    if coffee_choice == 'cappuccino':
        cappuccino_price = MENU['cappuccino']['cost']
        if profit >= cappuccino_price:
            change = profit - cappuccino_price
            print(f"Thank you your change is ${round(change)}")
        elif profit == cappuccino_price:
            print(f"Thank you! Enjoy your coffee")
        else:
            difference = cappuccino_price - profit
            print(f"Not enough money, money refunded. Put in {difference} more.")

# Turn off coffee machine with "off"

# Print machine resources with "report"

# Check if resources has enough to make drink

# Check if the amount of money is enough and process or deny the transaction

# Make coffee and update resources
