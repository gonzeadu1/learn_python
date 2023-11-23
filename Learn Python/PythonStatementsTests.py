# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for letters in st.split():
    if letters[0] == 's' or letters[0] == 'S':
        #   if letters.__contains__('s'):
        print(letters)

# Use range() to print all the even numbers from 0 to 10.
for even_nums in range(0, 11, 2):
    if even_nums % 2 == 0:
        print(even_nums)

# OR
for even_nums in range(0, 11, 2):
    print(even_nums)

# OR
mylist = [even_nums for even_nums in range(0, 11, 2) if even_nums % 2 == 0]
print(mylist)

# OR
print(list(range(0, 11, 2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# my_list = []
# for nums in range(1, 51):
#     my_list.append(nums % 3 == 0)
#     print(nums)
#     print(type(my_list.append(nums % 3 == 0)))
# print(my_list)

my_list1 = [x for x in range(1, 51) if x % 3 == 0]
print(my_list1)
print([x for x in range(1, 51) if x % 3 == 0])

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for chars in st.split():
    if len(chars) % 2 == 0:
        print(chars)

# List Comprehension
my_even_list = [chas for chas in st.split() if len(chas) % 2 == 0]
print(my_even_list)

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print('Fizz')
    elif nums % 5 == 0:
        print('Buzz')
    else:
        print(nums)


# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
my_first_letters = []
for letters in st.split():
    my_first_letters.append(letters[0])
print(my_first_letters)

# OR
my_list1 = [word[0] for word in st.split()]
print(my_list1)
