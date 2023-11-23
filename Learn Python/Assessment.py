import math

test = ((((100.25 / 2) - 30) * 2) + 60 ** 1)
print(test)

test1 = math.sqrt(16)
print(test1)
print(test1 ** 2)

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
print(s[1])
print(s[-4])

s = 'hello'
# Reverse the string using slicing
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
#
s = 'hello'
# Print out the 'o'
# Method 1:
print(s[-1])

# Method 2:
print(s[4])
print(s.split('hello'))

# Lists
# Build this list [0,0,0] two separate ways.

# Method 1:
x = [0, 0, 0]
print(x)
# # Method 2:
y = [0] * 3
print(y)
my_tuple = (0, 0, 0)
x = [my_tuple]
print(x)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

# Another method using SORTED method
print(sorted(list4))

# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key': 'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
my_set = set(list5)
print(sorted(my_set))
list5.sort()
print(list5)
print(my_set)
