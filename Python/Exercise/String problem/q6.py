
# Write a program to count the number of words in a string without split ()

print('hi how are you'.split())

s = input("Enter the string : ")
l = []
temp = ''

for i in s:
    if i != ' ':
        temp = temp + i
    else:
        l.append(temp)
        temp = ''

l.append(temp)
print(l)
