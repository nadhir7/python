MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 2500,
    "milk": 1200,
    "coffee": 300,
}
def reduce(type):
    global resources
    resources["milk"]-=MENU[type]["ingredients"]["milk"]
    resources["water"]-=MENU[type]["ingredients"]["water"]
    resources["coffee"]-=MENU[type]["ingredients"]["coffee"]
    
def process_money(type):
    print("unexpected inputs will be interpreted as zero")
    try:
        peny = int(input("how many penies?"))
    except :
        peny = 0
    try:
        nickel = int(input("how many nickels?"))
    except :
        nickel = 0
    try:
        dime = int(input("how many dimes?"))
    except :
        dime = 0
    try:
        quarter = int(input("how many quarters?"))
    except :
        quarter = 0

    sum =  peny*0.01+nickel*0.5+dime*0.1+quarter*0.25
    if sum >= MENU[type]["cost"]:
        if sum>MENU[type]["cost"]:
            print(f"here is your {sum-MENU[type]["cost"]} in change")
        print(f"here is your {type} ")
        reduce(type)
    else :
        print("not sufficient")



def check_resources(type):
    r = "insuffient"

    if resources["coffee"]<MENU[type]["ingredients"]["coffee"]:
        r+=" coffee,"
    if resources["milk"]<MENU[type]["ingredients"]["milk"]:
        r+=" milk,"
    if resources["water"]<MENU[type]["ingredients"]["water"]:
        r+=" water."
    if r=="insuffient":
        return True
    else :
        return r[:len(r)-1] +"."

def report():
    print(resources["milk"])
    print(resources["water"])
    print(resources["coffee"])





while True :
    choice = input("how can i serve you?(espresso/latte/cappuccino)").lower()


    if choice =="off":
        break
    elif choice=="report":
        report()
    elif choice=="espresso" or choice=="latte" or choice=="cappuccino":

        if check_resources(choice)==True:
            process_money(choice)
        else:
            print(check_resources(choice))

    else:
        print("try again")

    
