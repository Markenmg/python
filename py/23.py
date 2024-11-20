class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)  # Initialize the parent class attributes
        self.color = color
  
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)  # Initialize the parent class (Car) attributes
        self.battery_capacity = battery_capacity
        
vehicle = Vehicle("Toyota", "Camry", 2020)
car = Car("Honda", "Civic", 2022, "Red")
electric_car = ElectricCar("Tesla", "Model 3", 2023, "Blue", 75)

print(vehicle)  
print(car)      
print(electric_car)  
