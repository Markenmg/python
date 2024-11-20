class Animal:
    def __init__(self, name, alive=True):
        self.name = name
        self.alive = alive

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow!")

dog1 = Dog("Tomi")
dog1.eat()
dog1.sleep()
dog1.bark()

cat1 = Cat("Adc")
cat1.eat()
cat1.sleep()
cat1.meow()
