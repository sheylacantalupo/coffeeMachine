MENU = {
    "espresso": {
        "ingredientes": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredientes": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}
CAIXA = 0
# função para escolha cardápio, retorna a chave referente ao sabor escolhido
def menu():
    escolha = str(input("What would you like?(espresso/latte/cappuccino)"))
    return escolha

# função para receber moedas, soma-las e retornar o valor obtido
def coins():
    print("Please insert coins.")
    quarter = float(input("How many quarters?"))
    dime = float(input("How many dime?"))
    nickel = float(input("How many nickel?"))
    penny = float(input("How many penny?"))
    total = 0.25*quarter + 0.10*dime + 0.05*nickel + 0.01*penny
    print(f"Total: ${total} ")
    return total

# função para retornar o troco
def change(choice, total):
    troco = total - MENU[choice]["cost"]
    return troco

# função para verificar se os recursos são suficientes
def estoque(choice):
    water = MENU[choice]["ingredientes"]["water"]
    milk = MENU[choice]["ingredientes"]["milk"]
    coffee = MENU[choice]["ingredientes"]["coffee"]
    if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
        return True
    else:
        return False

# função para atualizar o estoque de recursos
def resource(choice):
    water = MENU[choice]["ingredientes"]["water"]
    milk = MENU[choice]["ingredientes"]["milk"]
    coffee = MENU[choice]["ingredientes"]["coffee"]
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee

def coffeeMachine():
    global CAIXA
    choice = menu()
    if choice == "report":
        print(f"{resources}")
        print(f"Balance = ${CAIXA}")
    else:
        if estoque(choice) == True:
            valor = coins()
            if valor >= MENU[choice]["cost"]:
                troco = change(choice, valor)
                print(f"Here is ${troco} in change")
                print(f"Here is your {choice}. Enjoy!")
                CAIXA = CAIXA + MENU[choice]["cost"]
                resource(choice)
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print(f"Sorry,insufficient resources. ")
    print("\n")
    coffeeMachine()

coffeeMachine()