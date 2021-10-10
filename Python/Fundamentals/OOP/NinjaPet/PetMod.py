class Pet:
    def __init__(self, name, ptype, tricks):
        self.name = name
        self.ptype = ptype
        self.tricks = tricks
        self.health = 10
        self.energy = 5
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        print(self.health)
        print(self.energy)
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        if self.ptype == 'dog':
            print('Arf!')
        elif self.ptype == 'cat':
            print('Meow!')

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks, health, energy)

class Dog(Pet):
    def __init__():
        super().__init__(name, tricks, health, energy)

class Bird(Pet):
    def __init__():

