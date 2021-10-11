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
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        if self.ptype == 'dog':
            print('Arf!')
        elif self.ptype == 'cat':
            print('Meow!')
