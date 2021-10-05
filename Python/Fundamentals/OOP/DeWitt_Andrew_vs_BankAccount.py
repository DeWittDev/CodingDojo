class BankAccount:

    def __init__(self, name, intRate, balance):
        self.name = name
        self.accountBalance = balance
        self.interestRate = intRate/1000

    def deposit(self, amount):
        self.accountBalance += amount
        return self

    def withdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def displayBalance(self):
        print(self.name, 'Balance: $' + str(self.accountBalance))

    def yieldInterest(self):
        self.accountBalance *= self.interestRate
    
    def displayAccountInfo(self):
        print(self.name, self.interestRate, self.accountBalance)


Phoenix = BankAccount('Andrew', 15, 2348)
