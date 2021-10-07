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

    def fundTransfer(self, user, amount):
        self.account.withdrawal(amount)
        user.account.deposit(amount)
        self.displayBalance()
        user.displayBalance()
        print(f'{self.name} transferred ${amount} to {user.name}.')

import DeWitt_Andrew_vs_BankAccount


guido = User('Guido van Rossum', 'guido@python.org')
monty = User('Monty Python', 'monty@python.org')
phoenix = User('Andrew DeWitt', 'DeWitt@protonmail.ch')

phoenix.makeDeposit(23543)
phoenix.fundTransfer(guido, 3500)
phoenix.displayBalance()