class Grandfather:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Father(Grandfather):
    def __init__(self, name, age, father):
        super().__init__(father, age) 
        self.father = name

class Son(Father):
    def __init__(self, name, age, father):
        super().__init__(father, age) 
        self.son = name


grandfather = Grandfather("John", 70)
father = Father("Mike", 40, "John")  
son = Son("Tom", 20, "Mike",)  

print(grandfather)
print(father)
print(son)
