class User:
    bankName = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(intRate=0.015, balance=0)

    def makeDeposit(self, amount):
        self.account.deposit(amount)
        return self

    def makeWithdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def displayBalance(self):
        print(self.name, 'has a balance of $' + str(self.account.balance))
        return self

    def fundTransfer(self, transferee, amount):
        self.account.withdrawal(amount)
        transferee.account.deposit(amount)
        print(self.name, 'Balance: $' + str(self.account.balance))
        print(transferee.name, 'Balance: $' + str(transferee.account.balance))


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


guido = User('Guido van Rossum', 'guido@python.org')
monty = User('Monty Python', 'monty@python.org')
phoenix = User('Andrew DeWitt', 'DeWitt@protonmail.ch')

phoenix.makeDeposit(23543)
phoenix.fundTransfer(guido, 3500)
