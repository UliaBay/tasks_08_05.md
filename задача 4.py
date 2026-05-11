class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"
    def honk(self):
        return "Beep beep!"
class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors
    def info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h, Doors: {self.doors}"
    def open_trunk(self):
        return "Trunk opened"
class Motorcycle(Vehicle):
    def __init__(self, brand, speed, has_sidecar):
        super().__init__(brand, speed)
        self.has_sidecar = has_sidecar
    def honk(self):
        return "Beep! (louder)"
    def wheelie(self):
        return "Doing a wheelie!"
car = Car("Toyota", 180, 4)
print(car.info())
print(car.honk())
print(car.open_trunk())
bike = Motorcycle("Harley", 120, False)
print(bike.info())
print(bike.honk())
print(bike.wheelie())