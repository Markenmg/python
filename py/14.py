class Animal:
    def __init__(self, name, alive=True):
        self.name = name
        self.alive = alive

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, alive=True):
        self.name = name
        self.alive = alive

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cat(Animal):
    def __init__(self, name, alive=True):
        self.name = name
        self.alive = alive

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Dog(Animal):
        pass
class Cat(Animal):
        pass

Dog1=Dog("tomi",True)
Dog1.eat()
Dog1.sleep()

Cat1=Cat("adc",True)
Cat1.eat()
Cat1.sleep()