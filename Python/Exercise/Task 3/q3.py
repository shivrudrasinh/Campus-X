'''
### `Problem 3`:Write a program to pring the following pattern

        *
      * * *
    * * * * *
   * * * * * * *
* * * * * * * * *


'''

row = 5

for i in range(1,row +1):
    # Print space
    for j in range(row - i):
        print("", end = " ")
    
     # Print stars
    for k in range(2*i -1):
        print("*" ,end="")    
    
    print()