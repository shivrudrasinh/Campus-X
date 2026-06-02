### Q5:- Write a program to find the simple interest when the value of principle,rate 
         #  of interest and time period is provided by the user.

# Taking input from user
P = int(input("Enter Principal amount:"))
R = int(input("Enter Rate of interest:"))
T = int(input("Enter Time period:"))

# Calculating Simple interest
answer = (P*R*T)/100
ans = answer/365  # If time period is iin years than /100 , period in days than /100*365 

# Displaying 
print("The simple interest is:",ans)