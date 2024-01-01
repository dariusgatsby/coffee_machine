from machine import MENU, resources


def check_money(coffee_type, money_given):
    if coffee_choice == 'espresso':
        espresso_price = MENU['espresso']['cost']
        if profit > espresso_price:
            change = profit - espresso_price
            return f"Thank you your change is ${round(change)}"
        elif profit == espresso_price:
            return f"Thank you! Enjoy your coffee"
        else:
            difference = espresso_price - profit
            return f"Not enough money, money refunded. Put in ${difference} more."
    elif coffee_choice == 'latte':
        latte_price = MENU['latte']['cost']
        if profit > latte_price:
            change = profit - latte_price
            return f"Thank you your change is ${round(change)}"
        elif profit == latte_price:
            return f"Thank you! Enjoy your coffee"
        else:
            difference = latte_price - profit
            return f"Not enough money, money refunded. Put in ${difference} more."
    if coffee_choice == 'cappuccino':
        cappuccino_price = MENU['cappuccino']['cost']
        if profit > cappuccino_price:
            change = profit - cappuccino_price
            return f"Thank you your change is ${round(change)}"
        elif profit == cappuccino_price:
            return f"Thank you! Enjoy your coffee"
        else:
            difference = cappuccino_price - profit
            return f"Not enough money, money refunded. Put in ${difference} more."


def check_resources(coffee_type, menu, resources_left):
    water = resources_left['water']
    milk = resources_left['milk']
    coffee = resources_left['coffee']
    coffee_selected = menu[coffee_type]
    ingredients_needed = coffee_selected['ingredients']
    if not coffee_type == 'espresso':
        if milk < ingredients_needed['milk']:
            print('Not enough milk.')
            return True
    if water < ingredients_needed['water']:
        print('Not enough water.')
        return True
    elif coffee < ingredients_needed['coffee']:
        print('Not enough coffee.')
        return True
    else:
        return coffee_type


def make_coffee(coffee_type, menu, resources_left):
    current_water = resources_left['water']
    current_milk = resources_left['milk']
    current_coffee = resources_left['coffee']
    coffee_selected = menu[coffee_type]
    ingredients_needed = coffee_selected['ingredients']
    if not coffee_type == 'espresso':
        milk_left = current_milk - ingredients_needed['milk']
        resources_left['milk'] = milk_left
    water_left = current_water - ingredients_needed['water']
    coffee_left = current_coffee - ingredients_needed['coffee']
    resources_left['water'] = water_left
    resources_left['coffee'] = coffee_left


MENU = MENU

profit = 0
quarters = .25
dimes = .10
nickels = .05
pennies = .01
# Ask user what kind of coffee they want, collect money
machine_on = True
while machine_on:
    insufficient_resources = False
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off machine
    if coffee_choice == 'off':
        print('Turning Off...')
        machine_on = False
        break
    # Print machine resources with "report"
    elif coffee_choice == 'report':
        print(f"Water: {resources['water']}ml \n"
              f"Milk: {resources['milk']}ml \n"
              f"Coffee: {resources['coffee']}g")
        continue
    # Check if resources has enough to make drink
    else:
        resources_left = check_resources(coffee_choice, MENU, resources)
        if resources_left == True:
            insufficient_resources = resources_left
        if insufficient_resources:
            print(resources_left)
            continue
        else:
            print('Please insert coins.')
            quarters_given = float(input('how many quarters?: '))
            dimes_given = float(input("how many dimes?: "))
            nickels_given = float(input("how many nickels?: "))
            pennies_given = float(input("how many pennies?: "))

        profit = (quarters_given * quarters) + (dimes_given * dimes) + (nickels_given * nickels) + (
                    pennies_given * pennies)
        
        # Make coffee and update resources
        make_coffee(coffee_choice, MENU, resources)
        # Check if the amount of money is enough and process or deny the transaction
        result = check_money(coffee_choice, profit)
        print(result)




