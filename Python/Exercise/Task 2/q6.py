### `Problem 6` - Find the factorial of a given number.

''' Write a program to use the loop to find the factorial of a given number.
    The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.
    For example: calculate the factorial of 5

    5! = 5 × 4 × 3 × 2 × 1 = 120 '''


num = int(input("Enter a number to find its factorial:"))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("The factorial of 0 is 1.")

elif num > 0:
    factorial = 1 
    for i in range(1,num+1):
        factorial = factorial * i

print(f"The factorial of {num} is {factorial}.")


n = num
fact = 1

print(f"{n}! =", end=" ")

for i in range(n, 0, -1):
    fact *= i
    print(i, end=" × " if i != 1 else " = ")

print(fact)








