'''
Extract username from a given email.
Eg if the email is nitish24singh@gmail.com
then the username should be nitish24singh 
'''

g = input("Enter your mail id:")

position = g.index('@')
print(g[0:position])

