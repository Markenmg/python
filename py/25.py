class User:
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number
    
    def user_information(self):
        print("User Information:")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"id_number: {self.id_number}")

class bank(user)
 def __init__(self, name, age, gender, id_number):  
     super().__init__(name, age, gender, id_number)
     self.balance = 0
def deposit(self,amount):
         self.balance += amount
         print(f"Deposited {amount}. New balance: {self.balance}")
     

user1 = User("Alice", 30, "Female", "ID123456")
user1.user_information()
