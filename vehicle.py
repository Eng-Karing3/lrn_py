class Vehicle:
    def move(self):
        return "Vehicle is moving"
    
class Car(Vehicle):
    def fuel(self):
        return "Car needs fuel"
    
motor_vehicle = Car()

print(motor_vehicle.move())
print(motor_vehicle.fuel())
        