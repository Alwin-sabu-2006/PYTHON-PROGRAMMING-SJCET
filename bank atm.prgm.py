'''
AUTHOR=ALWIN SABU
DATE:28/10/24
DESCRIPTION:a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:

    1.Check Balance
    2.Deposit Money
    3.Withdraw Money
    4.Exit
'''
balance_amount=1000
while True:
    print("1.Check balance \t 2. Deposit Money \t 3 Withdraw money \t 4 Exit")
    choice=int(input("Enter The number of the function that you want to  perform:"))
    if choice==1:
        print("The current balance is:",balance_amount)
    elif choice==2:
        deposit=float(input("Enter the amount of money that you want to deposit:"))
        balance_amount=balance_amount+deposit
        print("The amount has been deposited")
        print("Existing Amount:",balance_amount)
    elif choice==3:
        withdraw=float(input("Enter the amount of money that you want to withdraw:"))
        if withdraw>balance_amount:
            print("INSUFFICIENT BALANCE")
        else:
            balance_amount = balance_amount - withdraw
            print("The amount of money that has been withdrawn from the account", withdraw)
            print("Existing amount in account:", balance_amount)


    elif choice==4:
        break
    else:
        print("INVALID ENTRY")