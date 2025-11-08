#Banking system!

import random
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'accounts.json')

with open(json_path, 'r') as file:
    data = json.load(file)

def save_data():
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

def createAccount():
    username = input("Account Username: ")
    pin = input("Account Pin:")
    initial_balance = random.randrange(10000, 1000000)

    if username in data:
        return False
    
    data[username] = {
         "pin": pin,
        "balance": initial_balance,
        "pocket": 0,
        "transactions": []
    }

    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Account {username} successfully created!")
    return True

def verifyLogin():
    username = input("Account Username: ")
    pin = input("Account Pin: ")

    if username in data and data[username]["pin"] == pin:
        return {
            "username": username,
            "balance": data[username]["balance"],
            "pocket": data[username]["pocket"],
            "transactions": data[username]["transactions"]
        }
    return None

print("Hello welcome to supernova Banks. what would you like to do?")
print("1. Login Account")
print("2. Create new Account")

action1 = int(input("Action (1 or 2): "))
print("\n")

if action1 == 1:
    account_data = verifyLogin()
    if account_data:
        print(f"Welcome back {account_data['username']}! What would you like to do?")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Past Transactions")

        action2 = int(input("Action (1, 2, 3 or 4): "))

        if action2 == 1:
            print(f"Your account balance is ${account_data['balance']}")
        elif action2 == 2:
            print(f"Currently you have ${account_data['pocket']} in your pocket")
            amount = int(input("How much do you want to deposit: $"))

            if amount > account_data["pocket"]:
                print("You dont have enough in your pocket to make this deposit, try again")
            else:
                data[account_data['username']]['balance'] += amount
                data[account_data['username']]['pocket'] -= amount
                print(f"Your new balance is ${account_data['balance']}")
                print(f"Your new pocket balance is ${account_data['pocket']}") 
                data[account_data["username"]]["transactions"].append(f"Deposited: ${amount}")   
                save_data()
        elif action2 == 3:
            print(f"Your account balance is ${account_data['balance']}")
            amount = int(input("How much do you want to withdraw: $"))

            if amount > account_data["balance"]:
                print("You dont have enough in your bank balance to make this withdraw, try again")
            else:
                data[account_data['username']]['balance'] -= amount
                data[account_data['username']]['pocket'] += amount
                print(f"Your new balance is ${account_data['balance']}") 
                print(f"Your new pocket balance is ${account_data['pocket']}")
                data[account_data["username"]]["transactions"].append(f"Withdraw: ${amount}")
                save_data()
        elif action2 == 4:
            print(account_data['transactions'])
    else:
        print("Invalid account, Try again")

elif action1 == 2:
    createAccount()

input("Press Enter to exit...")