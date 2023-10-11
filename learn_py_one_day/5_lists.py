'''
Lists

Refers to a collection of dara which are normally related. Instead of storing these data
on separate variables, we can store them as a list
We declare them as a variable but the arguments are inside square brackets [] separated by commas
We can declare a empty list too, then use .append() method to add items on the list
Each item has a position, we always start from ZERO

Syntax:
listName = [initial values]
'''

userAge = [21,22,25,27]
print(userAge[0]) # 21 => First item
print(userAge[2]) # 25 => Third item

print(userAge[-1]) # 27 => Last item
print(userAge[-2]) # 25 => Before last item

userAge2 = userAge # We can assing the items on a list to another variable
print(userAge2) # [21, 22, 25, 27]

userAge3 = userAge[2:4] # We can assing part of a list to a variable
print(userAge3) # [25 , 26]

"""
The notation 2:4 is known as a slice
When using slices in Python, the item at the start index is always included, but the
item on the end is always excluded
"""

#The slice notation includes a third number called the stepper

example = [1,0,2,0,3,0,4,0,5]
print(example) # [1,0,2,0,3,0,4,0,5]

example_stepper = example[0:9:2] # We will get a sublist consisting of every second number
print(example_stepper) # [1,2,3,4,5]

'''
Slice notation have useful defaults
The first number is Zero and the default for the second number is the size 
of the list sliced
'''

example_stepper = example[::2] # This works the same as the example above
print(example_stepper) # [1,2,3,4,5]

'''
To modify items on a list

Syntax:
listName[Index of item to be modified] = new value
'''

userAge = [21, 22, 25, 27]
userAge[1] = 50
print(userAge) # [21,50,25,27]

#Other examples

myList = [1, 2, 3, 5.5, 'Hello']

#Print the entire list
print(myList) # [1, 2, 3, 5.5, 'Hello']

#Print the third item
print(myList[2]) # 3

#Print the last item
print(myList[-1]) # 'Hello'

#append a new item to myList and print the updated list
myList.append('How are you')
print(myList) # [1, 2, 3, 5.5, 'Hello', 'How are you']

#remove the fifth item from myList and print the updated list
del myList[4]
print(myList) # [1, 2, 3, 5.5, 'How are you']