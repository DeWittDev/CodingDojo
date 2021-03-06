class BankAccount:
    bankName = 'First National Dojo'
    def __init__(self, intRate, balance):
        self.intRate = intRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def yieldInterest(self):
        self.balance += (self.balance * self.intRate)
        return self
    
    def displayAccountInfo(self):
        print('Balance: $' + str(self.balance))
        return self

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__(intRate, balance)

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__(intRate, balance)