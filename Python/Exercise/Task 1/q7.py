### Q7:- Write a program to find the sum of squares of first n natural numbers where 
         # n will be provided by the user.

n = int(input("Enter the number:"))

sum = 0

for i in range(1,n+1):
    sum += i**2

print("Sum of square of first",n,"natural number =",sum)

