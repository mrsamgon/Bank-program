     #python banking program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    print("****************")


def deposit(balance):
    amount = float(input(" Enter amount to be deposit: "))

    if amount > 0:
        # print(f"You have Successfully deposit {amount:.2f}")
        new_balance = balance + amount  # Calculate the new balance
        print(f"${amount:.2f} successfully added. Now, the remaining balance is ${new_balance:.2f}.")
        return amount

    elif amount < 0 :
        print("That's not a valid amount")
        return 0

    else:
        return 0
    

def withdraw(balance):

    amount = float(input(" Enter amount to be withdrawn: "))
    print("****************")

    if amount > balance:
        print("****************")

        print("Insufficent balance.")
        print("****************")

        return 0
    elif amount < 10:
        print("****************")

        print("Withdrawal amount should be Minimum 10$")
        print("****************")

        return 0
    else:
        # print(f"You have Successfully withdraw {amount:.2f}")
        print(f"${amount:.2f} successfully withdrawn. Now, the remaining balance is ${balance - amount:.2f}.")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************")
        print("Banking Program")
        print("****************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************")


        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            deposit_amount = deposit(balance)
            balance += deposit_amount
            print(f"New balance after deposit: ${balance:.2f}")


        elif choice == '3':
            withdraw_amount = withdraw(balance)
            balance -= withdraw_amount
            print(f"New balance after withdraw: ${balance:.2f}")
    
        elif choice == '4':
            is_running = False

        else:
            print("****************")

        print("That is not valid choice.")
        print("****************")

    print("****************")

    print("Thank you! have a nice Day!")

if __name__ == '__main__':
    main()
