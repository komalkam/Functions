class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def get_account_number(self):
        return self.account_number

    def get_holder_name(self):
        return self.holder_name

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

if __name__ == "__main__":
    account1 = BankAccount("123456789", "Alice", 1000)
    account2 = BankAccount("987654321", "Bob")

    print(f"Account Number: {account1.get_account_number()}, Holder Name: {account1.get_holder_name()}, Balance: ${account1.get_balance()}")
    print(f"Account Number: {account2.get_account_number()}, Holder Name: {account2.get_holder_name()}, Balance: ${account2.get_balance()}")

    account1.deposit(500)
    account1.withdraw(200)2

    account2.deposit(1000)
    account2.withdraw(1500)