#inputs for a coffee machine 
global water, coffee_powder, milk, total
water = 1500 #ml

coffee_powder = 500 #mg

milk = 1500 #ml

total = 0 #cents


items = {
    '\nindex': "item - cents\n",
    1:"espresso - 50 cents",
    2:"latte - 75 cents",
    3:"cappuccino - 80 cents",
    4:"Mocha - 119 cents\n"
}

# for item in items:
#     print(f"{item} - {items[item]}")
# try:
#     user_input = int(input("What would you like to have? (espresso/latte/cappuccino): "))
# except ValueError:
#     print("Entered wrong input can you please try again")
#     user_input = int(input("What would you like to have? (espresso/latte/cappuccino): "))

def coin_processing():
    global total
    total = 0
    print("Please insert coins below")

    try:
        five = int(input("How many five cents : "))
        ten = int(input("How many ten cents : "))
    except ValueError:
        print("Plese enter coins as integers only")
        five = int(input("How many five cents : "))
        ten = int(input("How many ten cents : "))

    total = ten * 10 + five * 5

    print(f"Total amount inserted : {total} cents\n")

def check_resources():
    global water, milk, coffee_powder
    if water < 200:
        print("Not enough water to make coffee")
        return False
    elif milk < 100:
        print("Not enough milk to make coffee")
        return False
    elif coffee_powder < 50:
        print("Not enough coffee powder to make coffee")
        return False
    else:
        return True

def latte():
    global total, water, milk, coffee_powder
    coin_processing()
    if check_resources() and total >= 75:
        water -= 200
        milk -= 100
        coffee_powder -= 50
        print(f"Your latte is ready! \n Have and enjoy.... \n*4 here is your change {total - 75} cents")


        total = 0
    elif total < 75:
        print("Not enough money inserted to make latte. Please insert more coins.")
        print(f"here is your money back {total} cents")
        total = 0
    else:
        print("Cannot make latte due to insufficient resources.")
        print(f"here is your money back {total} cents")
        total = 0

def espresso():
    global total, water, milk, coffee_powder
    coin_processing()
    if check_resources() and total >= 50:
        water -= 200
        milk -= 100
        coffee_powder -= 50
        print(f"Your espresso is ready\n Have and enjoy.... \n here is your change {total - 50} cents")
        total = 0
    elif total < 50:
        print("Not enough money inserted to make espresso. Please insert more coins.")
        print(f"here is your money back {total} cents")
        total = 0
    else:
        print("Cannot make espresso due to insufficient resources.")
        print(f"here is your money back {total} cents")
        total = 0

def cappuccino():
    global total, water, milk, coffee_powder
    coin_processing()
    if check_resources() and total >= 80:
        water -= 200
        milk -= 100
        coffee_powder -= 50
        print(f"Your cappuccino is ready! \n Have and enjoy.... \n*4 here is your change {total - 80} cents")
        total = 0
    elif total < 80:
        print("Not enough money inserted to make cappuccino. Please insert more coins.")
        print(f"here is your money back {total} cents")
        total = 0
    else:
        print("Cannot make cappuccino due to insufficient resources.")
        print(f"here is your money back {total} cents")
        total = 0

def mocha():
    global total, water, milk, coffee_powder
    coin_processing()
    if check_resources() and total >= 119:
        water -= 200
        milk -= 100
        coffee_powder -= 50
        print(f"Your mocha is ready! \n Have and enjoy.... \n*4 here is your change {total - 119} cents")
        total = 0
    elif total < 119:
        print("Not enough money inserted to make mocha.")
        print(f"here is your money back {total} cents\n order again please")
        total = 0
    else:
        print("Cannot make mocha due to insufficient resources.")
        print(f"here is your money back {total} cents")
        total = 0

def main_function():
    for item in items:
        print(f"{item} - {items[item]}")
    try:
        user_input = int(input("enter the corresponding index number to your choice : "))
    except ValueError:
        print("Entered wrong input can you please try again")
        user_input = int(input("enter the corresponding index number to your choice : "))

    if user_input == 1:
        espresso()
    elif user_input == 2:
        latte()
    elif user_input == 3:
        cappuccino()
    elif user_input == 4:
        mocha()
    else:
        print("Invalid selection. Please choose a valid option.")

while check_resources():

    main_function()
    # print(f"Remaining resources - Water: {water}ml, Milk: {milk}ml, Coffee Powder: {coffee_powder}mg")

    try :
        continue_choice = str(input("\nWould you like to make another coffee? (yes/no): ").strip().lower())
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue_choice = str(input("\nWould you like to make another coffee? (yes/no): ").strip().lower())

    if continue_choice != 'yes':
        print("Thank you for using the coffee machine. Goodbye!")
        break
    
        
