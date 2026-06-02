### Q4:- Write a program to find the euclidean distance between two coordinates.Take
         #  both the coordinates from the user as input.

# Taking input from user
x1 = float(input("Enter X1 :"))
x2 = float(input("Enter X2 :"))

y1 = float(input("Enter Y1 :")) 
y2 = float(input("Eenter Y2 :"))

# Calculating Euclidean Distance
E = ((x2 - x1)**2 + (y2 - y1)**2) **0.5

# Displaying Euclidean Distance
print("Euclidean Distance",E)



