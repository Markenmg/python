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
        
class Bank(User):
    def __init__(self, name, age, gender, id_number):  
        super().__init__(name, age, gender, id_number)  
        self.balance = 0  
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):  
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance for withdrawal.")
            
    def view_balance(self):
        print(f"Your current balance is: {self.balance}")
        

user1 = Bank("Alice", 30, "Female", "ID123456") 
user1.user_information() 
user1.deposit(1000)  
user1.withdraw(500)  
user1.withdraw(600)  
