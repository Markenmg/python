num = int(input("Enter a number: "))
sum_digits = 0
prod_digits = 1
original_number = num

while num != 0:
    rem = num % 10
    sum_digits += rem        
    prod_digits *= rem       
    num //= 10              

if sum_digits + prod_digits == original_number:
    print("Special number")
else:
    print("Not a special number")
