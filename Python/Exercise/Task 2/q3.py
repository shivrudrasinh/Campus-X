### `Problem 3`: Write a program that will take user input of cost 
# price and selling price and determines whether its a loss or a profit.


cost = int(input("Enter cost :"))
selling = int(input("Enter selling price:"))

if selling > cost:
    print('Profit of :',selling - cost)

elif cost > selling:
    print("Loss of:",cost - selling)

else:
    print("No profit No loss")
    
             