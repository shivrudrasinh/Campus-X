### `Problem 9`: Write a program that keeps on accepting a number from the user until the user enters 
                 # Zero. Display the sum and average of all the numbers.
total = 0

while True:
    num = int(input("Enter a number (0 to stop):"))
    if num == 0:
        break
    else:
     total += num

print(f"The sum of all the numbers is: {total}")