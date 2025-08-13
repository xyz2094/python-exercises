class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_data(self):
    print(f"\nName: {self.name}, Age: {self.age}\n")
    print("-" * 20)

print("-" * 20)

person1 = Person("Vittor", 21)
person1.print_data()

person2 = Person("Livia", 19)
person2.print_data()