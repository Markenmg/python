def is_duck_number(num):
    num_str = str(num)
    
  
    if num_str[0] == '0':
        return False
    
    
    return '0' in num_str


number = input("Enter a number to check if it is a duck number: ")

if is_duck_number(number):
    print(f"{number} is a duck number.")
else:
    print(f"{number} is not a duck number.")
