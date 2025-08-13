class Vehicle:
    def move(self):
        print("-" * 20)
        print("\nThe vehicle is moving.\n")
        print("-" * 20)

class Car(Vehicle):
    def refuel(self):
        print("\nThe car is being refueled.\n")
        print("-" * 20)
    
class SportsCar(Car):
    def turbo(self):
        print("\nThe sports car is in turbo mode!\n")
        print("-" * 20)


vehicle = Vehicle()
vehicle.move()

vehicle = Car()
vehicle.refuel()

vehicle = SportsCar()
vehicle.turbo()
