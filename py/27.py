class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Boy(Human):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")
        self.bonus = 250
        self.salary = 300
        self.total_salary = self.salary + self.bonus  

class Girl(Human):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")
        self.bonus = 100
        self.salary = 200
        self.total_salary = self.salary + self.bonus  

boy1 = Boy("John", 25)
girl1 = Girl("Alice", 23)


print(f"Boy: {boy1.name}, Gender: {boy1.gender}, Total Salary: {boy1.total_salary}")
print(f"Girl: {girl1.name}, Gender: {girl1.gender}, Total Salary: {girl1.total_salary}")
