### Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%)
               #  DA(5%), PF(3%) and taxes deduction as below:
'''
> Salary(Lakhs) : Tax(%)

*   Below 5 : 0%
*   5-10 : 10%
*   10-20 : 20%
*   aboove 20 : 30% '''

salary = int(input("Enter your salary:"))
hra = (10/100) * salary
da = (5/100)* salary
pf = (3/100) * salary

if salary < 500000:
    tax = 0
    print(f'tax is: {tax}')
    print("In hand monthly salary is:", (salary - hra - da - pf - tax)//12)

elif 500000 <= salary < 1000000:
    tax = (10/100) * salary
    print(f'tax is: {tax}')
    print("In hand montly salalry is:",salary-hra-da-pf-tax//12)

elif 1000000 <= salary < 2000000:
    tax = (20/100) * salary
    print(f'tax is: {tax}')
    print("In hand salary is:", (salary-hra-da-pf-tax)//12)

elif salary >= 2000000:
    tax = (30/100) * salary
    print(f'tax is: {tax}')
    print("In hand salary is:", (salary-hra-da-pf-tax)//12)

else:
    print("Invalid salary")