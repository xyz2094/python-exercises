class Product:
  def __init__(self, name, price=None):
    self.name = name
    self.price = price

  def __str__(self):
    if self.price is not None:
      return f"Product(name={self.name}, price={self.price})"
    else:
      return f"Product(name={self.name})"
    
  def print_data(self):
    print(f"\nName: {self.name}, Price: {self.price if self.price is not None else 'Not specified'}\n")
    print("-" * 20)

print("-" * 20)

product1 = Product("Laptop", 4500)
product1.print_data()

product2 = Product("Smartphone")
product2.print_data()