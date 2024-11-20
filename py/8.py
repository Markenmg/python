def is_neon_number(num):
    
    square = num ** 2
    
    
    digit_sum = sum(int(digit) for digit in str(square))
    
   
    return digit_sum == num


number = int(input("Enter a number to check if it is a neon number: "))

if is_neon_number(number):
    print(f"{number} is a neon number.")
else:
    print(f"{number} is not a neon number.")
