balance = 0
change = 0

def deposit():
    global change
    global balance
    print("How much would you like to deposit into your account?")
    change = int(input())
    balance = balance + change
    print("Your current balance is now " + str(balance))

def withdraw():
    global change
    global balance
    print("How much would you like to withdraw from your account?")
    change = int(input())
    balance = balance - change
    print("Your current balance is now " + str(balance))

def main():
    global change
    global balance
    print("How much is your balance with us?")
    balance = int(input())
    deposit()
    withdraw()
    print("Thank you for using our bank, Please come again.")

main()