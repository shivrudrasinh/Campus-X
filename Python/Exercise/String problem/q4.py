
# Write a program that can remove a particular character from a String 


inp = input("Enter a string: ")
rem = input("What you like to remove: ")

result =''

for i in inp:
    if i != rem:
        result = result + i

print(result)        
