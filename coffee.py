MENU = {
    "espresso": {
        "ingredients": {
            "milk":150,
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
profit=0
resources = {
    "water": 600,
    "milk": 400,
    "coffee": 200,
}



def chek(saad):
    count=0
    for item in resources.keys():
        if resources[item]<=MENU[saad]['ingredients'][item]:
            print(f'Sorry, There is no enough {item}')
            count+=1
    if count==0:
        return True
    else:
        return False





def mon_in():
    print("Please insert coins")
    quarters=int(input('How many quarters?'))
    dimes=int(input('How many dimes?'))
    nickles=int(input('How many nickles?'))
    pennies=int(input('How many pennies'))
    dollars=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    return dollars



def makeCoffee(seda):
    resources['water'] = resources['water']-MENU[seda]['ingredients']['water']
    resources['coffee'] = resources['coffee']-MENU[seda]['ingredients']['coffee']
    resources['milk'] = resources['milk']-MENU[seda]['ingredients']['milk']


def monPro(a, b, saad):
    if a > b:
        c = a-b
        d = round(c,3)
        global profit
        profit += MENU[saad]['cost']
        print(f"Here is ${d} in change. \nHere is your {saad}. Enjoy!")
        return True
    elif a == b:
        print(f'no change. \n Here is your {saad}. Enjoy!')
        return True
    else:
        return False



option = ['espresso','latte','cappuccino','report','no']
power = True
while power:
    drink = input("What would you like(espresso, latte, cappuccino)?")
    if drink == 'no':
        power = False
    elif drink == 'report':
        print(f"water:{resources['water']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"milk:{resources['milk']}ml")
        print(f"money: ${profit}")
    elif drink not in option:
        print("Invalid Input")
    else:
        if not chek(drink):
            power = False
        else:
            rs = mon_in()
            re = monPro(rs, MENU[drink]['cost'], drink)
            if re == True:
                profit=MENU[drink]['cost']
                makeCoffee(drink)
            else:
                print("Not enough money. Money refunded.")


