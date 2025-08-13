class Car:

  def __init__(self, manufacturer, model, year):
    self.manufacturer = manufacturer
    self.model = model
    self.year = year

  def print_data(self):
    print(f"\nManufacturer: {self.manufacturer}, Model: {self.model}, Year: {self.year}\n")
    print("-" * 20)

print("-" * 20)

car1 = Car("Toyota", "Corolla", 2020)
car1.print_data()

car2 = Car("Honda", "Civic", 2021)
car2.print_data()

carro3 = Car("Ford", "Focus", 2019)
carro3.print_data()
