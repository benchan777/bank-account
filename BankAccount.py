class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    # Method for adding specified amount to the balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${self.balance}")
        return self.balance

    # Method for removing specified amount from the balance
    def withdraw(self, amount):
        # Charges $10 overdraft fee if an amount greater than the balance is attempted to be withdrawn
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
            return self.balance

    # Method for printing the current balance
    def get_balance(self):
        print(f"Your current balance is ${self.balance}.")
        return self.balance

    # Method for adding interest to the balance
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        return self.balance

    # Method for printing out the receipt
    def print_receipt(self):
        account_number_string = str(self.account_number)
        censored_string = ''
        counter = 0
        # Replaces the first 4 numbers of the account number with *
        for number in range(len(account_number_string)):
            if counter < 4:
                censored_string += "*"
                counter += 1
            else:
                censored_string += account_number_string[counter]
                counter += 1

        print(f"{self.full_name}\nAccount No.: {censored_string}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}")

    # Method for charging an extra fee when withdrawing money
    def withdrawal_fee(self):
        self.balance -= 2
        print("A $2 ATM fee has been added.")

ben = BankAccount("Ben Chan", 39287362, 928162736, 0)
david = BankAccount("David Chan", 66751479, 899878318, 0)
steven = BankAccount("Steven George", 49516794, 974897183, 0)

# ben.deposit(45.01)
# ben.withdraw(95.00)
# ben.add_interest()
# ben.get_balance()
# ben.print_receipt()

while True:
    user_input = int(input("Select an option. Enter 'quit' to exit.\n1: Deposit\n2: Withdraw\n3: Add Interest\n4: Get Balance\n5: Print receipt\nEnter your option here: "))

    if user_input == 1:
        deposit_input = float(input("Enter how much money you would like to deposit: "))
        ben.deposit(deposit_input)
    elif user_input == 2:
        withdraw_input = float(input("Enter how much money you would like to withdraw: "))
        ben.withdrawal_fee()
        ben.withdraw(withdraw_input)
    elif user_input == 3:
        ben.add_interest()
        print("Interest has been added!")
    elif user_input == 4:
        ben.get_balance()
    elif user_input == 5:
        ben.print_receipt()
    else:
        break