
# Write a program that can check a given string is palindrome or not 
# A string that reads the same forward and backward.
# eg: abba , malayalam

s = input("Enter a string: ")
flag = True
for i in range(0,len(s)//2):
    if s[i] != s[len(s) - i - 1]:
     flag = False
     print('Not a palindrome')
     break

if flag:
   print("Palindrome")
   