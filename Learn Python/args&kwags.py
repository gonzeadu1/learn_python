def myfunc(*args):
    return sum(args)


# a function that takes in an arbitrary number of integer items
# and returns only the even numbers

def myfunction(*args):
    return [items for items in args if items % 2 == 0]


def mylist3(*args):
    my_even_numbers = []
    for items in args:
        if items % 2 == 0:
            my_even_numbers.append(items)
    return my_even_numbers


def mylist(*args):
    my_even_numbers = []
    for item in args:
        if item % 2 == 0:
            my_even_numbers.append(item)
    return my_even_numbers


print(mylist(8, 3, 4, 5, 5, 6, 6, 7, 7, 8, 48))


# A function that takes in a string
# and returns a matching string where every even letter is uppercase


def my_string_func(args):
    result = []
    for items in range(len(args)):
        if items % 2 == 0:
            result.append(args[items].upper())
        else:
            result.append(args[items].lower())
    return ''.join(result)


print(my_string_func("Anthropomorphism"))


def alternate_uppercase(s):
    # Initialize an empty string to store the result
    result = ""

    # Iterate over the string, character by character
    for i in range(len(s)):
        # Check if the character index is even
        if i % 2 == 0:
            # Add the character in uppercase to the result
            result += s[i].upper()
        else:
            # Add the character in its original form (lowercase) to the result
            result += s[i]

    return result


# Test the function
print(alternate_uppercase("hello"))  # Should print "HeLlO"


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def myfunc0(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)


print(myfunc0("Anthropomorphism"))
