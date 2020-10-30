class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
            return self.balance

    def get_balance(self):
        print(f"Your current balance is ${self.balance}.")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        return self.balance

    def print_receipt(self):
        account_number_string = str(self.account_number)
        censored_string = ''
        counter = 0
        for number in range(len(account_number_string)):
            if counter < 4:
                censored_string += "*"
                counter += 1
            else:
                censored_string += account_number_string[counter]
                counter += 1

        print(f"{self.full_name}\nAccount No.: {censored_string}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}")

ben = BankAccount("Ben Chan", 39287362, 928162736, 0)
# david = BankAccount("David Chan", )

ben.deposit(45.01)
ben.withdraw(95.00)
ben.add_interest()
ben.get_balance()
ben.print_receipt()