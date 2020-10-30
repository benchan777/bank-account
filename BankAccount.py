class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount Deposited: ${self.balance}"


ben = BankAccount("Ben chan", 39287362, 928162736, 0)
print(ben.deposit(45.01))