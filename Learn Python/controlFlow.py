# Always watch out for indentations in python!
from random import shuffle, randint

hungrey = True
if hungrey:
    print("IT'S TRUE")
else:
    print("I am not hungry")

loc = 'Store'
if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool/good")
elif loc == "Store":
    print("Feyi buy some food items while coming back!")
else:
    print("I do not know much")

name = "Feyi"
if name == "Feyi":
    print("I love you babe!")
elif name == "Past":
    print("Forget it!")
else:
    print("So, what is your name?")

# For-Loops
# This is for iterating over elements/objects of an entity
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 89, 0]
for num in mylist:
    print(num)
for jelly in mylist:
    print("hello")
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 89, 0]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print("The total is: ", list_sum)

# Iterating over strings
my_String = 'hello world'

for _ in my_String:
    print('xxhigh')
for letters in my_String:
    print(letters)

# Iterating through a tuple
tupl = (1, 2, 3)
for t in tupl:
    print(t)

mylist = [(1, 2), (2, 3), (4, 5), (7, 8)]
print("The length of myList is: ", len(mylist))
for num_sets in mylist:
    print(num_sets)
# tuple unpacking
for (a, b) in mylist:
    print(b)

# iterating through dictionary
my_dict = {'k1': 1, 'k2': 2, 'k3': 42}
for key, value in my_dict.items():
    print(value)
for elements in my_dict.items():
    print("  nvvvnvnvnvnvnnvnnvnnnvnvn ", elements)

# While-loops
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    # x = x + 1
    # or
    x += 1
else:
    print(x, 'is not less than 5')

# using breaks, continue and Pass
x = [1, 2, 3]
for items in x:
    # comment
    pass
print('end of my scripts')

mystring = 'Feyi'
for letters in mystring:
    if letters == 'e':
        continue
    print(letters)

x = 0
while x < 5:
    if x == 4:
        break
    print("hhhhhhhhhhhhhhhh", x)
    x += 1

# Using Range in python
myNum = [2, 32, 4, 4, 5, 66]
for num in range(0, 10, 2):
    print(num)

# using index count
index_count = 0
for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

word = 'Apple'
# jumping in stepSize
print(word[::2])

# ordinary slicing
print(word[:2])

# Slicing with stepSizing
print(word[0:5:2])

# using enumerate function
for index, letters in enumerate(word):
    print(letters)
    print(index)
    print('\n')

# The zip function zips couple of items together
mylist1 = [1, 32, 4]
mylist2 = ['asta', 'diya', 'dab']
mylist3 = ['hello', 'apple', 'Feyi']
for item in zip(mylist1, mylist2, mylist3):
    print("This is a zip function:", item)

for a, b, c in zip(mylist1, mylist2, mylist3):
    print("What! ", a)
    #    print('\n')
    print("Okay: ", b)
    #    print('\n')
    print("Feyi, it is well:", c)

# list function
print(list(zip(mylist1, mylist2, mylist3)))

# using the 'in' keyword
print('Feyi' in mylist1)
print('Feyi' in mylist2)
print('Feyi' in mylist3)

myKeys = {'mykey1': 346, "mykey2": 6453}
print("mykey1" in myKeys)

# using the max and min functions
mylist4 = [1, 2, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 0, 00, 0, -10]
print("The maximum number here is: ", max(mylist4), "\n",
      "While the minimum number here is: ", min(mylist4))

# using the shuffle function from the random library. It has no return type.
# So, you can't assign it to a variable. It is an in-place function
# Any function that is void type cannot be printed directly
shuffle(mylist4)
print(mylist4)

# using rand from random library for getting random integer. It has a return type
ranInt = randint(0, 100)
print("This is a random integer: ", ranInt)

# user-input. How to do it
# result = int(input('Enter a number here: '))
# print("The number chosen is: ", result)
# print(type(result))

# List Comprehensions
mysTRING = 'Hello'
mylist5 = []
for letter in mysTRING:
    mylist5.append(letter)
print(mylist5)

# OR using one-liner (i.e. flattened for-loop)
mylist6 = [letter for letter in mysTRING]
print(mylist6)
mylist7 = [akjaska for akjaska in 'asasasa']
print(mylist7)

# using flattened FOR-LOOP in range
mylist8 = [num for num in range(0, 10)]
print(mylist8)

# performing operations in enhanced for-loop
mylist8 = [num ** 2 for num in range(0, 10)]
print(mylist8)

# using if-conditions
mylist9 = [x for x in range(0, 11) if x % 2 == 0]
print(mylist9)

# doing more complex examples wih enhanced For-loop
celcius = [0, 10, 20, 45, 89]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

# This is the same as:
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9 / 5) * temp + 32))
print(fahrenheit)

# if and if-else statements in enhanced for-loop
mylist10 = [x ** 2 for x in (range(0, 11)) if x % 2 == 0]
print("mylist10", mylist10)

# if-else statement is kinda reverse of the order of IF-ELSE statement

mylist11 = [x ** 2 if x % 2 == 0 else x == 'ODD' for x in range(0, 11)]
print(mylist11)

# Nested FOR-LOOPS in List Comprehension or ENHANCED FOR-LOOPS
my_list = []
for num in [2, 4, 6]:
    for secondNums in [1, 10, 1000]:
        my_list.append(num * secondNums)
print(my_list)

my_list1 = [num * secondNums for num in [2, 4, 6] for secondNums in [1, 10, 1000]]
print(my_list1)
