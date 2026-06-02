### `Problem 4`: Write a menu-driven program -
''' 1. cm to ft
    2. km to miles
    3. USD to INR
    4. exit             '''



num = int(input("Enter number between 1 to 4:"))

if num == 1:
    cm = int(input("Enter length in cm:"))
    ft = cm/ 30.48
    print("Length in ft:",ft)


elif num == 2:
   km = int(input("Enter distance in km:"))
   miles = km *0.621371
   print("Distance in miles is:",miles)


elif num == 3:
    usd = int(input("Enter curreny in USD:"))
    inr = usd *82.74
    print("Currency in INR is:",inr)

elif num == 4:
    print("Exit")        
