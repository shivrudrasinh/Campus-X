# Find the length of given string without using len()

s = input("Enter the string: ")
 
counter = 0 
for i in s:
    counter +=1
print(f'The length of string is: {counter}')