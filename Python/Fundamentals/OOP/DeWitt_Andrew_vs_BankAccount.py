class BankAccount:
    bankName = 'First National Dojo'
    allAccounts = []
    def __init__(self, intRate, balance):
        self.intRate = intRate
        self.balance = balance
        BankAccount.allAccounts.append(self)

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

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__(intRate, balance)

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__(intRate, balance)