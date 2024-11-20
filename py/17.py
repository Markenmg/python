class Transport:
    def move(self):
        print("Moving")

    def stop(self):
        print("Stopped")

class Bus(Transport):
    def move(self):
        print("Bus is moving")
    def stop(self):
        print("Stopped")

class Motorcycle(Transport):
    def move(self):
        print("Motorcycle is moving")
    def stop(self):
        print("Stopped")

class Bicycle(Transport):
    def move(self):
        print("Bicycle is moving")
    def stop(self):
        print("Stopped")

class car(Transport):
    def move(self):
        print("car is moving")
    def stop(self):
     print("stopped")
     
def test_transport(transport):
    transport.move()
    transport.stop()

     
