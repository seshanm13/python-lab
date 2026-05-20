balance = 1000.0  # Global balance variable

def deposit(amount):
    global balance
    balance += amount
    print(f"Successfully deposited ₹{amount:.2f}")
    check_balance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print(f"Successfully withdrew ₹{amount:.2f}")
    check_balance()

def check_balance():
    print(f"Current Available Balance: ₹{balance:.2f}")

# Demo executions
deposit(500)
withdraw(300)
withdraw(2000) # Testing insufficient balance