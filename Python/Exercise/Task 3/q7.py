### `Problem 7` - Find the sum of the series upto n terms.
'''

Write a program to calculate the sum of series up to n term. For example, if n =5 the series 
will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the 
output style should match which is given in the example.'''


digit = int(input("Enter a digit :"))
n = int(input("Enter number of terms :"))


term = 0 
total = 0 

for i in range(1,n+1):
    term = term * 10 + digit
    total += term

    print(term,end=" ")
    if i != n:
        print("+",end=' ')

print()
print("Sum of all above series is:",total)        

