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

