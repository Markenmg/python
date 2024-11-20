class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def america(self):
        print(f"{self.name} is from America.")

class Son(Father):
    def __init__(self, name, age):
        super().__init__(name, age)

    def play(self):
        print(f"{self.name} is playing.")

class Daughter(Father):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(f"{self.name} is studying.")


father = Father("John", 45)
father.america()

son = Son("Mike", 20)
son.play()

daughter = Daughter("Anna", 18)
daughter.study()
