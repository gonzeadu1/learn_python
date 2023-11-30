# Maps and how to use them
# Always use map when you want to perform an operation on each of the constituents
# of the elements in the list ot be provided
def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)

my_list = list(map(square, my_nums))
print(my_list)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return mystring
    else:
        return mystring[0]


names = ["Gideon", "Hope", "Feyi", "Love", "Godso"]

# Always put them in a list
print("names:", list(map(splicer, names)))


# Filter functions and how to use  them

# Method must return a bool
def is_even(nums):
    return nums % 2 == 0


my_nums = [12, 45, 656, 778, 89, 3, 54, 56, 67]

# Always put the filter and maps in a list to see the constituents.
print(list(filter(is_even, my_nums)))

# Lambda expressions and how to use them
# with Map Function
my_lambda_list = list(map(lambda nums: nums ** 2, my_nums))
print("my_lambda_list", my_lambda_list)

my_lambda_list1 = list(filter(lambda mystring: len(mystring) % 2 == 0, names))
print("my_lambda_list1", my_lambda_list1)

# Lambda Expressions with Filter functions
# It is like a one-liner methods/functions, but must return a bool
my_lambda_list2 = list(filter(lambda nums: nums % 2 == 0, my_nums))
print("my_lambda_list2", my_lambda_list2)


my_lambda_list3 = list(map(lambda my_loved_ones: my_loved_ones[::1], names))
print(my_lambda_list3)

