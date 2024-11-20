num=int(input("enter a number"))
sum=0
prod=1
origibal_number=num
while num!=0
     rem=num%10
     sum=sum+rem
     prod=prod*rem
     num=num//10
if sum+prod==origibal_number
    print("special number")
else:
    print("not a spescial number")