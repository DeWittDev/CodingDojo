import PetMod
class Ninja:
    def __init__(self, firstName, lastName, treats, petFood):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = PetMod.Pet('Benyamin', 'cat', 'hunt')
    
    def walk():
        self.pet.play()
        print(f'{self.pet.name} has {self.pet.health} health.')

    def feed():
        self.pet.eat()
        print(f'{self.pet.name} has {self.pet.health} health and {self.pet.energy} energy.')
    
    def bathe():
        self.pet.noise()


Phoenix = Ninja('Andrew', 'DeWitt', 'mouse', 'steak')

Phoenix.bathe()