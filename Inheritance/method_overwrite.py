class Animal:
    def sound(self):
          print("-" * 20)
          print("\nSound animals make:\n")
          print("-" * 20)

class Dog(Animal):
    def sound(self):
        print("\nThe dog does: Woof! Woof!\n")
        print("-" * 20)

class Cat(Animal):
    def sound(self):
        print("\nThe cat does: Meow!\n")
        print("-" * 20)


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()