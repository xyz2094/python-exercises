from abc import ABC, abstractmethod

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass
    
class Duck(Flyer, Swimmer):
    def fly(self):
        return "\nDuck is flying!\n"
    
    def swim(self):
        return "\nDuck is swimming!\n"

class Eagle(Flyer):
    def fly(self):
        return "\nEagle is flying!\n"
    
class Fish(Swimmer):
    def swim(self):
        return "\nFish is swimming!\n"
    
duck = Duck()
eagle = Eagle()
fish = Fish()

print("-" * 20)
print(duck.fly())
print(duck.swim())
print("-" * 20)
print(eagle.fly())
print("-" * 20)
print(fish.swim())
print("-" * 20)