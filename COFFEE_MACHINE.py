# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
sel = "init"
menu = {"espresso":
            {"ingredients":
                {"water" : 50,
                 "coffee" : 18,
                 "milk": 0
                 },
             "cost": 1.5
            },
        "latte":
            {"ingredients":
                 {"water": 200,
                  "coffee": 24,
                  "milk": 150
                  },
             "cost":2.5
             },
        "cappuccino":
            {"ingredients":
                 {"water":250,
                  "coffee": 24,
                  "milk":100
                  },
             "cost": 3
             }
        }

resource = {"milk": 10,
            "water": 1000,
            "coffee": 500,
            "money": 50
            }




def report():
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}gm")
    print(f"Money: ${resource['money']}")

def make_coffee(selection):
    print(f"Here is your {selection} enjoy!!! ")
    resource["water"] -= menu[selection]["ingredients"]["water"]
    resource["coffee"] -= menu[selection]["ingredients"]["coffee"]
    resource["milk"] -= menu[selection]["ingredients"]["milk"]


def process_coin(selection):
    quart = int(input("How many quarters: "))
    dime = int(input("How many dime: "))
    nickel = int(input("How many nickel: "))
    pennies = int(input("How many pennies: "))

    total_amt = (quart*0.25) + (dime*0.1)+(nickel*0.05)+(pennies*0.01)

    if(menu[selection]["cost"] > total_amt):
        print("Not enough money, money refunded")
    elif (menu[selection]["cost"] < total_amt):
        bal = round(total_amt - menu[selection]["cost"],2)
        print(f"Here is {bal} in change ")
        resource["money"] += menu[selection]["cost"]
        make_coffee(selection)


def check_resource(selection):
        if resource["water"] < menu[selection]["ingredients"]["water"]:
            print("Sorry no water")
        elif resource["coffee"] < menu[selection]["ingredients"]["coffee"]:
            print("Sorry no coffee")
        elif resource["milk"] < menu[selection]["ingredients"]["milk"]:
            print("Sorry no milk")
        else:
            process_coin(selection)



while sel != "off":
    sel = input("What would you like (espresso/latte/cappuccino):  ")
    if sel == "print":
       report()
    elif sel == "espresso" or sel =="latte" or sel =="cappuccino":
        check_resource(sel)
    elif sel == "off":
        print("Shutting down Bye !!: ")
    else:
        print("Invalid selection !!")




