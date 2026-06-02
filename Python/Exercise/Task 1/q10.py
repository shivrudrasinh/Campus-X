### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of 
          # milk can be obtained? Assume all the inputs are provided by the user.

h = int(input("Enter the height of the tank:"))
b = int(input("Enter the breadth of the tank:"))
w = int(input("Enter the width of the tank:"))
g = int(input("Enter the volume of glass:"))

# Volume of the tank 
vol = h*b*w

# calculating the answer 

print("Number of glass of milk:",vol//g)