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

    def fundTransfer(self, transferee, amount):
        self.accountBalance -= amount
        transferee.accountBalance += amount
        print(self.name, 'Balance: $' + str(self.accountBalance))
        print(transferee.name, 'Balance: $' + str(transferee.accountBalance))

guido = User('Guido van Rossum', 'guido@python.org')
monty = User('Monty Python', 'monty@python.org')
phoenix = User('Andrew DeWitt', 'DeWitt@protonmail.ch')


guido.deposit(1352)
guido.deposit(436)
guido.deposit(777)
guido.withdrawal(647)
guido.displayBalance()

monty.deposit(348)
monty.deposit(24005)
monty.withdrawal(3349)
monty.withdrawal(20000)
monty.displayBalance()

phoenix.deposit(3984)
phoenix.withdrawal(124)
phoenix.withdrawal(248)
phoenix.withdrawal(496)
phoenix.displayBalance()

print()
guido.fundTransfer(phoenix, 300)


