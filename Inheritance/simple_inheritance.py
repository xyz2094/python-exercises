class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

class Manager(Employee):
  def __init__(self, name, salary, department):
    super().__init__(name, salary)
    self.department = department

  def print_data(self):
    print(f"\nName: {self.name}, Salary: {self.salary}, Department: {self.department}\n")
    print("-" * 20)

print("-" * 20)

manager = Manager("Vittor", 8000, "IT")
manager.print_data()