class Employee:
    def __init__(self, name, salary, background, nationality):
        self.name = name
        self.salary = salary
        self.background = background
        self.nationality = nationality

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Background: {self.background}, Nationality: {self.nationality}"

employee1 = Employee("John Doe", 50000, "Engineering", "eesti")
print(employee1.display_info())
employee2 = Employee("alex kassk", 7000, "Engineering", "eesti")
print(employee1.display_info())
employee3 = Employee("tom kil", 7000, "Engineering", "eesti")
print(employee1.display_info())

def name(self):
    print("{}{}".format(self.name))
