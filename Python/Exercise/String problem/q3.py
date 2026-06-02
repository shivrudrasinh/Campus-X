'''
Count the frequency of a particular character in a provided string.
Eg: 'hello how are you' is the string, the frequency of h in this string is 2.
'''


inp = input("Enter a string: ")
sea = input("What you like to search: ")

counter = 0
for i in inp:
    if i == sea:
        counter += 1
print(f" The letter comes {counter} times")        
