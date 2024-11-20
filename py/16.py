class Transport:
    def move(self):
        print("Moving")

    def stop(self):
        print("Stopped")

class Bus(Transport):
    def move(self):
        print("Bus is moving")

class Motorcycle(Transport):
    def move(self):
        print("Motorcycle is moving")

class Bicycle(Transport):
    def move(self):
        print("Bicycle is moving")


bus = Bus()
bus.move()  
bus.stop()  

motorcycle = Motorcycle()
motorcycle.move()  
motorcycle.stop()  

bicycle = Bicycle()
bicycle.move()  
bicycle.stop()
