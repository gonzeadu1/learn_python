wage = 30
hours = 40
weeks = 40
salary = wage * hours * weeks

print("Salary is:", salary)
var = 7 % 4
print(var)

a = 5
a = 10
a = a + a
print(a)
type(a)

my_income = 67000
my_taxRate = 0.1
my_taxes = my_taxRate * my_income
print('my taxable income =', my_taxes)

# Strings in python
word = "hello world"
print("The length of the above letters is", len(word))
print("The dataType for word is ", type(word))

# for new line
print("hello \nworld")

# for new tab
print("hello \tworld")

# Indexing
word = "hello world"
print(word[8])
print(word[9])

print(word[-2])

# slicing
print(word[2:])
# up to but not including
print(word[2:7])
# up to but not including
print(word[:3])

# jumping in stepSize
print(word[::2])

# Slicing with stepSizing
print(word[0:10:2])

# trick for reversing string python
print(word[::-1])

# immutability of Strings: This means you cannot change a String
name = "Pam"
lastLetters = name[1:]
print("P" + lastLetters)
x = " Hello World"

print(name + x)

y = x.upper()
# splitting in python
z = x.split()
a = x.split('w')
print(y)
print(a)
print(z)

# formatting Strings
print("This is a string {}".format("brown", "fox", "quick"))
print("The {2} {1} {0}".format("brown", "fox", "quick"))
# using variable format
print("The {c} {a} {c}".format(a="brown", b="fox", c="quick"))

# float formatting
# float formatting follows "{value:width.precision f}"
result = 100 / 777
print("The result of the calculations above is = {r: 1.5f} ".format(r=result))

# using the format method follows {value:{width}.{precision}}
print(f"The result of the calculations above is = {result}")
print(f"The result of the calculations above in formatting is = {result:{1}.{7}}")

# Lists = This is just like arrays in Java
# The most important methods are: append methods, pop and sort
# The elements here are mutable unlike in Strings

elements = ["man", 12, 423.4, "woman", "love", 0.211]
# eg of mutable
print(elements[0])
elements[0] = "woman"
print(elements[0])
elements.append("Gideon")
additionalElements = elements
print(additionalElements)
elements.pop()
print(elements)
elements.pop(0)
print(elements)
elements.pop(-1)
print(elements)
elements.pop(2)
print("The elements here are: ", elements)
elements.reverse()
newElements = elements
print(newElements)
# elements.sort()

newElements = elements
print(newElements)
# slicing of lists
print(elements[1:])
print(elements[0:])
i = elements.pop(1)
print(i)
print(elements)

# Dictionaries
# These are unordered mappings for storing objects.
# It stores objects using key-value relationship.
# Dictionaries uses curly braces and colons to signify the keys and their associated values
# Eg. {'key1:'value','key2': 'value'}
# We only use keys to locate the values. You can sort dictionaries.
# But we can sort List and locate the index location

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
element_1 = my_dict['key1']
print(element_1)

# dictionaries are very flexible. They can combine both int and str without declaration
d = {"k1": 1.233, "k2": 3.4}
print(d["k2"])

d = {'k1': 123, 'k2': [1, 2, "e", 3], 'k3': 100, 'k4': {'insideKey': 100}}
print(d["k1"])
print(d['k2'][3])
print(d['k4']['insideKey'])

# to return the keys of a dictionary
print(d.keys())

# to return the values of a dictionary
print(d.values())

# to return the pairings of a dictionary
print(d.items())

# Tuples are like list except that they are immutable.
# Once assigned, the elements cannot change. Tuples use parenthesis instead of square[] brackets

t = (1, 3, 4, "redhat")
print("This is a tuple", t)
print(t[0])
# t[0] = '8'

# sets
# An unordered collections of unique elements. No two elemts can be in a set
my_set = set()
print(my_set)
my_set.add(12)
print(my_set)
print("Feyi")
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set)

# How to cast set in a List
my_List = [1,3,3,4,5,6,7,1,2,3,4,54,5,6,76,87,8,98,0,12,3,4,5,6,6,7,8,8,9,9,0]
castingListInASet = set(my_List)
print(castingListInASet)
print(set(my_List))
#Can I add the elements of a set directly into a list?

# Booleans
# They are operators to convey TRUE or FALSE

r = True
print("This a boolean:", r)
print(type(r))
print(set([1,1,2,3]))

# Input and output files
# print(pwd)
my_file = open("C:\\Users\\Gideon\\OneDrive\\Documents\\Feyi.txt")
my_file = open('python.txt')
print(my_file.read())
print("Hi, Feyi. Could you pls read this: ", my_file.readline())
my_file.read() # To read a file content
print(my_file.read())
my_file.seek(0) # Resetting to the beginning
my_file.readlines() # Reading line my line
my_file.close()
with open('my_file.txt') as my_new_file:
    contents = my_new_file.read()

# how to read, write, a and open files
# with open('Feyi.txt', mode='r') as my_file:
#     contents = my_new_file.read()

# mode = 'r' is read only
# mode = 'w' is write only (will overwrite files or create new!)
# mode = 'r+' is reading and writing
# mode = 'a' is append only (will add on to files)
# mode = 'w+' is writing and reading (overwrites exsiting files or ceates a new file!)

with open('my_file.txt', mode='r') as f:
    print((f.read()))




