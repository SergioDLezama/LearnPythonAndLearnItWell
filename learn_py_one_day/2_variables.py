jumpline = '-' * 20 + '\n'
'''
Variables are names given to data that we need to store and manipulate
in our program

Every time you declare a nwe variable, you need to give it an initial value

A variable name in python can only contain letters, numbers and underscores
however the first character cannot be a number
'''

userAge = 0
userName = "Peter"

userAge, userName= 0, "Peter"

x= 5
y = 10
print("x = ", x) # x = 5
print("y = ", y) # y = 10

print(jumpline)

# A variable can be overwrited
x= 5
y = 10
x = y
print("x = ", x) # x = 10
print("y = ", y) # y = 10
