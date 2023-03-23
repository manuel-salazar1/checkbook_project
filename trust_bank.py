

# BELOW ARE THE 3 FUNCTIONS USED IN LAST 'WHILE' LOOP

# account_balance function 
def account_balance():
    with open('trust_bank.txt','r') as t: #opens text file in read only mode
        balance = float(t.read()) #converts string to number float
    print(f'Your current balance is: $ {balance}')


# deposit function
def deposit(): #add_credit
    amount = input('Enter the amount to deposit: ') #user will enter a number to deposit
    if not amount.isnumeric(): #checking for number input
        print('Invalid input. Please enter a positive number.')
        deposit()
        return
    amount = float(amount) #turns the input string into a number float
    if amount < 0: #checking if number is less than 0
        print('Invalid input. Cannot Deposit Negative Amount.')
        deposit()
        return
    with open('trust_bank.txt','r') as t: #opens text file in read only. t is alias for this txt file
        balance = float(t.read()) #converts txt string to number float
    balance += amount #if all conditions are met above, will subtract amount from balance
    with open('trust_bank.txt','w') as t: #opens text file in write mode
        t.write(str(balance)) #will write over previous balance and save in text file
    print(f'Deposit successful. Your new balance is: $ {balance}')


# withdrawal funtion
def withdrawal(): #add_debit
    amount = input('Enter the amount to withdraw: ') #user will enter a number to withdraw
    if not amount.isnumeric(): #checking for number input
        print('Invalid input. Please enter a positive number.')
        withdrawal()
        return
    amount = float(amount) #turns the input string into a number float
    if amount < 0: #checking if number is less than 0
        print('Invalid input. Cannot Withdraw Negative Amount.')
        withdrawal()
        return
    with open('trust_bank.txt','r') as t: #opens text file in read only. t is alias for this txt file
        balance = float(t.read()) #converts txt string to number float
    if amount > balance: #checking if amt entered is more than the current balance
        print('Insufficient Funds.')
        return
    balance -= amount #if all conditions are met above, will subtract amount from balance
    with open('trust_bank.txt','w') as t: #opens text file in write mode
        t.write(str(balance)) #will write over previous balance and save in text file
    print(f'Withdrawal successful. Your new balance is: $ {balance}')

# exit_program function
def exit_program():
    global active_program
    active_program = False
    


# BELOW is the program

active_program = True

print("-")
print("Welcome to A Bank You Can Trust!")
print("-")

while active_program:
    username = input("Enter your 4 digit pin: ")
    if len(username) == 4 and username.isdigit():
        break
    else:
        print("Invalid entry. Please enter 4 digit pin.")
        
while active_program:
    print("""
    Available Options Below:
    1) check current balance
    2) record a credit(deposit)
    3) record a debit(withdrawal)
    4) exit
    """)
    
    while active_program:
        user_option = input("What Would You Like To Do Today? ")
        if user_option == "1":
            account_balance()
        elif user_option == "2":
            deposit()
        elif user_option == "3":
            withdrawal()
        elif user_option == "4":
            exit_program()
            print("Thank you for trusting A Bank You Can Trust!")     
        else:
            print("Invalid Entry")
  































