### Q6:- Write a program that will tell the number of dogs and chicken are there when 
         # the user will provide the value of total heads and legs.

# Taking value from user 

head = int(input("Enter the number of heads:"))
legs = int(input("Enter the number of legs:"))

dog = (legs - 2*head)//2
chicken = head - dog 

print("Total number of Dogs are:",dog)
print("Total number of hens are:",chicken)


