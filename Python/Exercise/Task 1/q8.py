### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series.
         #  Assume all inputs are provided by the user.

a1 = int(input("Enter the first term:"))
a2 = int(input("Enter the second term:"))
n = int(input("Enter the Nth term:"))

# Finding the difference
d = a2 - a1

# Finding the Nth term
term = a1 +(n-1)*d

print("The Nth term of the Arithmetic series is", term)