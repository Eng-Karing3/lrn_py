class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self, password):
        if password == "admin123":
            return self.__balance
        
        else:
            return "Access denied"

account1 = BankAccount()

print(account1.deposit(10000))
print(account1.withdraw(1000))
print(account1.get_balance("admin123"))
