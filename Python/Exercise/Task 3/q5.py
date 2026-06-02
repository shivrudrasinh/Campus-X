'''
Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:<br>
1 + x^2/2 + x^3/3 + … x^n/n<br>
n will be provided by the user

'''

x = int(input("Enter value of x:")) 
n = int(input("Enter value of n:"))

sum_series = 1

for i in range(2,n+1):
    term = (x**i) /i
    sum_series += term

print("Sum of n term is:",sum_series)    