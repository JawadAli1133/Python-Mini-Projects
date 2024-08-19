import os
import art
import data

total_water = data.resources["water"]
total_coffee = data.resources["coffee"]
total_milk = data.resources["milk"]


def check_resources(order_type):
    global total_milk,total_coffee,total_water
    # order_ingredients = data.MENU[order_type]["ingredients"]
    order_water = data.MENU[order_type]["ingredients"]["water"]
    order_coffee = data.MENU[order_type]["ingredients"]["coffee"]
    order_milk = data.MENU[order_type]["ingredients"]["milk"]
    if order_water <= total_water and order_coffee <= total_coffee and order_milk <= total_milk:
        total_water -= order_water
        total_milk -= order_milk
        total_coffee -= order_coffee
        return True
    return False


def check_bill(order_type, quarters, dimes, nickles, pennies):
    order_cost = data.MENU[order_type]["cost"]
    cost = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if cost >= order_cost:
        cost -= order_cost
        return round(cost,2)
    return -1


print(art.logo)
while True:
    os.system('cls')
    coffee_type = input("What would you like? (espresso/latte/cappuccino) :")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    change = check_bill(coffee_type,quarters,dimes, nickles, pennies)
    if change != -1:
        if check_resources(coffee_type):
            print(f"Here is your {coffee_type} ☕. Enjoy!")
            if change > 0:
                print(f"Here is you ${change} change.")
        else:
            print("Sorry we don't have enough items. Money Refunded!")
    else:
        print("Sorry that's not enough money. Money Refunded!")
