import math
import string


# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4 / 3) * (rad ** 3) * math.pi


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, (high + 1)):
        return num in range(low, (high + 1))


print(ran_check(3, 1, 10))


# Write a Python function that accepts a string and calculates the number of upper case letters
# and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
#
# HINT: Two string methods that might prove useful: .isupper() and .islower()
#
# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    dict_counter = {'uppercase_counter': 0, 'lowercase_counter': 0}
    for char in s:
        if char.isupper():
            dict_counter["uppercase_counter"] += 1
        elif char.islower():
            dict_counter['lowercase_counter'] += 1
        else:
            pass
    return dict_counter


# check
print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


# Write a Python function that takes a list
# and returns a new list with unique elements of the first list.
#
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    return list(set(lst))


def unique_list2(lst):
    unique_numbers = []
    for number in lst:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


def unique_list3(lst):
    seen = set()
    unique = []
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique


print(unique_list3([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# e.g., madam,kayak,racecar, or a phrase "nurses run".
# Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces.
# Also google search how to reverse a string in Python,
# there are some clever ways to do it with slicing notation.

def palindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return "it's palindrome"
    else:
        return "not palindrome"


print(palindrome("madam"))
print(palindrome("nurses run"))


def ispangram(str):
    my_letters = set(str)
    subset_check = set(str.lower())
    return my_letters.issubset(subset_check)


def is_pangram(str, alphabet=string.ascii_lowercase):
    alpha_set = set(alphabet)
    space_removal = str.replace(' ', '')
    lower_case = space_removal.lowercase()
    set_convert = set(lower_case)
    return set_convert.issubset(alpha_set)

def ispangram1(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')

    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)

    # Now check that the alpahbet set is same as string set
    return str1 == alphaset

