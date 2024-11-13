import math

num = int(input("Enter a number: "))
sum_factorials = 0
original_number = num

while num != 0:
    rem = num % 10
    sum_factorials += math.factorial(rem)  
    num //= 10 

if sum_factorials == original_number:
    print("Special number (factorion)")
else:
    print("Not a special number")
