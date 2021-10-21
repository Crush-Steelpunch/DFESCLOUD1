from abc import ABC, abstractmethod

class Animal(ABC):
    def noise(self):
        return "grrr"
    
    @abstractmethod
    def eat(self):
        pass



class Bear(Animal):
    def eat(self):
        return 'meat and fish'

class Bird(Animal):
    def eat(self):
        return 'seeds and worms'


ted = Bear()

print(ted.noise())
print(ted.eat())

pigiotto = Bird()
print(pigiotto.noise())
print(pigiotto.eat())