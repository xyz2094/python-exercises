class Vehicle:
    def __init__(self, model):
        self.model = model
        print(f"Model: '{self.model}' has been added")
    
    def move(self, model):
        print(f"\nThe vehicle '{model}' is moving.\n")

class Car(Vehicle): 
    def __init__(self, model):
        super().__init__(model)

    def refuel(self):
        print(f"\nThe car '{self.model}' is being refueled.\n")

class SportsCar(Car):
    def __init__(self, model):
        super().__init__(model)

    def turbo_mode(self):
        print(f"\nThe sports car '{self.model}' is in turbo mode!\n")

vehicle = Vehicle("Celta")
vehicle.move(vehicle.model)

car = Car("Civic")
car.refuel()

sports_car = SportsCar("Ferrari")
sports_car.turbo_mode()