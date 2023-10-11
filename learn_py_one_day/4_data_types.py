'''
Integer

Numbers with no decimal part
'''

userAge = 20
mobileNumber = 4128325494

'''
Float

Numbers that have a decimal part
'''

userHeight = 1.82
userWeight = 85.3

"""
Strings

Refers to text
"""

userName = 'Peter'
userSpouseName = 'Sandra'
userAge = '30' # This is a string because the quotes

# We can combine multiple strings by using the concatenate sing (+)
userName = 'Peter'
userLastname = 'Lee'
print(userName + userLastname) # PeterLee

"""
Strings functions

Used to manipulate strings, they do not change the original variable
"""

userName = 'peter'
print(userName.upper()) # PETER
print(userName) # peter

print(userName.title()) # Peter

userName = 'Peter'
print(userName.lower()) # peter

"""
Formatting a using the (%) Operator

syntax:
"String to be formatted"%(values or variables to be inserted in the
string separated by commas)

%s = String
%d = Integer
%f = Float
"""

brand = 'Apple'
exchangeRate = 1.2352

message = "The price of this %s laptop is %d USD and the exchange rate is %4.2f to 1EUR"%(brand, 1299, exchangeRate)
print(message)

'''
If we want to add spaces before an integer we can add a number between % and d to
indicate the desired lenght of the string
'''

message = "%5d"%(123)
print(message) # "  123"

"""
The %f formats a float. In the example %4.2 where 4 refers to the total lenght
and 2 refers to the decimal places
"""

example = 1.247854
message = "%7.2f"
print(message) # '   1.24'

"""
Formatting strings with the format() value

Syntax:
"string to be formatted".format(values or variables to be inserted in the string
separated by commas)

When we use the format() we use Braces {} as place holders
"""

message = """
The price of this {0:s} laptop is {1:d} USD and the exchage rate is {2:4.2f} USD to 1 EUR
""".format('Apple',1299,1.2352)
print(message)

"""
We are passing 3 arguments to the format() method. Arguments are data that the method
needs in order to perform its task

Positions always start from ZERO

0: 'Apple'
1: 1299
2: 1..2352

When we write {0:s} we are refering to argument in position 0 and its a string
(Formatter is s)

When we write {1:d} we are refering to argument in position 1 and its a integer
(Formatter is d)

When we write {2:4.2f} we are refering to argument in position 2 and its a float
and we want it with 2 decimal places and a total lenght of 4
(Formatter is f)
"""

'''
If you do not want to format the string you can just write:
'''
message = """
The price of this {} laptop is {} USD and the exchage rate is {} USD to 1 EUR
""".format('Apple',1299,1.2352)
print(message)

'''
Here we do not have to specify the position of the arguments.
The interpreter will replace the braces based on the order or the arguments provided
'''
# Other examples:

message1 = '{0} is easier than {1}'.format('Python', 'Java')
print(message1) # Python is easier than Java

message2 = '{1} is easier than {0}'.format('Python', 'Java')
print(message1) # Java is easier than Python

message3 = '{:10.2f} and {:d}'.format(1.2342342, 12)
print(message3) #       1.23 and 12
# You do not need to indicate the position of the arguments

message4 = '{}'.format(1.2453455)
print(message4) #1.2453455
# No formatting is done

"""
Type casting

Sometimes it is necessary to convert one data type to other
Such as from an integer to a string. This is known as type casting

Python uses three built-in functions
float() / int() / str()
"""

# int() Takes a float or an appropiate string to an integer

example = int(5.2541)
print(example) # We get 5. Anything after the decimal point is removed

example = int('7') # '7' is a string
print(example) # We get 7 as a integer

'''
example = int('Hello')
print(example) # This will gives us an error. We cannot turn 'Hello' to a integer

example = int('4.2458')
print(example) # This will gives us an error to
'''

# float() Takes an integer or an appropiate string to a float

example = float(2)
print(example) # We get 2.0

example = float('5')
print(example) # We get 5.0

example = float('2.5478')
print(example) # We get 2.5478

# str() Takes an integer or a floar to a string

example = str(2.45)
print(example) # We get '2.45'

example = str(5)
print(example) # We get '5'




