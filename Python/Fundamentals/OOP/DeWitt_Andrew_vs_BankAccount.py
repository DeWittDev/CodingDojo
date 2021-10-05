class BankAccount:
    bankName = 'First National Dojo'
    allAccounts = []
    def __init__(self, name, intRate, balance):
        self.name = name
        self.intRate = intRate/1000
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

    @classmethod
    def defaultBalance(cls):
        savings = 0
        for account in cls.allAccounts:
            savings += account.balance
        return savings


Phoenix = BankAccount('Andrew', 15, 2348)
Guido = BankAccount('Guido', 10, 23)

Phoenix.deposit(340).deposit(4620).deposit(324).withdrawal(4503).yieldInterest()
print(Phoenix.displayAccountInfo())

Guido.deposit(3446).deposit(3000).withdrawal(21).withdrawal(657).withdrawal(345).withdrawal(32).yieldInterest()
print(Guido.displayAccountInfo())