from menu import MENU, resources


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_price(total_price, order_price):
    if total_price < order_price:
        return False
    else:
        return True


def calculate_price(quarters_price, dimes_price, nickles_price, pennies_price):
    """This function calculate coins inserted and return the total into dollars"""
    return (0.25 * quarters_price) + (0.10 * dimes_price) + (0.05 * nickles_price) + (0.010 * pennies_price)


def check_resources(choice):
    """This function check the resource is available in resources or not"""
    if MENU[choice]['ingredients']['water'] <= resources['water']:
        if choice != 'espresso':
            if MENU[choice]['ingredients']['milk'] <= resources['milk']:
                if MENU[choice]['ingredients']['coffee'] <= resources['coffee']:
                    return True
                else:
                    print("Sorry that's not enough coffee.")
                    return False
            else:
                print("Sorry that's not enough milk.")
                return False
        else:
            if MENU[choice]['ingredients']['coffee'] <= resources['coffee']:
                return True
            else:
                print("Sorry that's not enough coffee.")
                return False
    else:
        print("Sorry that's not enough water.")
        return False


machine_off = True
money = 0
while machine_off:
    user_choice = input("What would you like? (Espresso(e)/Latte(l)/Cappuccino(c)): ").lower()
    if user_choice == 'e':
        user_choice = 'espresso'
    elif user_choice == 'l':
        user_choice = 'latte'
    elif user_choice == 'c':
        user_choice = 'cappuccino'

    if user_choice == 'report' or user_choice == 'r':
        report()
    elif user_choice == 'off':
        print("Remaining Resources: ")
        report()
        print("Thank you!")
        machine_off = False
    elif user_choice == 'collection':
        print(f"${money} Collection till now")
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if check_resources(user_choice):
            print("Please insert coins.")
            quarters = int(input("how many quarters?($0.25) : "))
            dimes = int(input("how many dimes?($0.10) : "))
            nickles = int(input("how many nickles?($0.05) : "))
            pennies = int(input("how many pennies?($0.01) : "))
            entered_price = round(calculate_price(quarters, dimes, nickles, pennies), 2)
            if check_price(entered_price, MENU[user_choice]['cost']):
                change = round(entered_price - MENU[user_choice]['cost'], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice.title()} ☕️. Enjoy!")
                money += MENU[user_choice]['cost']
                resources['water'] -= MENU[user_choice]['ingredients']['water']
                resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                if user_choice != 'espresso':
                    resources['milk'] -= MENU[user_choice]['ingredients']['milk']
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("""
        You spell something Wrong :( 
        You can Type ('e' or 'l' or 'c') instead of (Espresso/Latte/Cappuccino)
        """)
