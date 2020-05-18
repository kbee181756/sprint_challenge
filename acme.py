import random


class Product():
    def __init__(self, name, price=10, weight=20,
    flammability=0.5, identifier=random.randint(1000000, 9999999)):
    
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal = (self.price/self.weight)
        if steal < 0.5:
            return 'Not so stealable...'
        elif ((steal >= 0.5) and (steal < 1.0)):
            return 'Kinda stealable'
        else:
            return 'Very stealable'
    
    def explode(self):
        blowup = (self.flammability * self.weight)
        if blowup < 10.0:
            return '...fizzle.'
        elif ((blowup >=10) and (blowup < 50)):
            return '...boom!'
        else:
            return '...BABOOM'
      
class BoxingGlove(Product):
    def __init__(self, price, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)
        pass

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        if ((self.weight >= 5)  and (self.weight< 15)):
            return 'Hey that hurt!'
        else:
            return 'OUCH'