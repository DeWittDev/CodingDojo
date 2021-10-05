class User:
    bankName = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accountBalance = 0

    def deposit(self, amount):
        self.accountBalance += amount
        return self

    def withdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def displayBalance(self):
        print(self.name, 'Balance: $' + str(self.accountBalance))
        return self

    def fundTransfer(self, transferee, amount):
        self.accountBalance -= amount
        transferee.accountBalance += amount
        print(self.name, 'Balance: $' + str(self.accountBalance))
        print(transferee.name, 'Balance: $' + str(transferee.accountBalance))

guido = User('Guido van Rossum', 'guido@python.org')
monty = User('Monty Python', 'monty@python.org')
phoenix = User('Andrew DeWitt', 'DeWitt@protonmail.ch')


guido.deposit(1352).deposit(436).deposit(777).withdrawal(647).displayBalance()

monty.deposit(348).deposit(24005).withdrawal(3349).withdrawal(20000).displayBalance()

phoenix.deposit(3984).withdrawal(124).withdrawal(248).withdrawal(496).displayBalance()

print()
guido.fundTransfer(phoenix, 300)


