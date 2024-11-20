class vehicle:
    def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
       
class car(vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        
             
class electric_car(vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        
       
       
       
vehicle = vehicle("Toyota", "Camry", 2020)
car = car("Honda", "Civic", 2022, "Red")
electric_car = electric_car("Tesla", "Model 3", 2023, "Blue")

print(vehicle)
print(electric_car)
print(car)


