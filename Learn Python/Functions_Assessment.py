# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    elif a % 2 == 1 or b % 2 == 1:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    wordlist = text.lower().split()
    first_word = wordlist[0]
    second_word = wordlist[1]
    if len(wordlist) >= 2:
        return first_word[0] == second_word[0]


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(n1, n2):
    if (n1 + n2 == 20) or (n1 == 20) or (n2 == 20):
        return True
    else:
        return False


print('"""""""""""""""""""')
print(makes_twenty(10, 10))
print(makes_twenty(20, 0))


def animal_crackers(text):
    words = text.lower().split()  # Convert to lowercase and split

    # Check if there are at least two words
    if len(words) >= 2:
        return words[0][0] == words[1][0]
    else:
        # Handle cases with less than two words (optional, depending on your requirements)
        return False


# Test the function
print(animal_crackers("Levelheaded Llama"))  # Should return True
print(animal_crackers("Crazy Kangaroo"))  # Should return False


# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
    first_character = ''
    fourth_character = ''
    for i in name:
        my_list = name.split()
        first_character = my_list[0][0].upper()
        fourth_character = my_list[0][3].upper()
    return first_character + my_list[0][1:3] + fourth_character + my_list[0][4:]


def new_macdonald(name):
    first_half = name[:3].capitalize()
    second_half = name[3:].capitalize()
    return first_half + second_half


# Check
print(old_macdonald('macdonald'))
print(new_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentence):
    result = sentence.split()
    var = result[::-1]
    return ' '.join(var)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
    #     return True
    # else:
    #     return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))


# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# print(items)


print("'''''''''''''''''''''''''''''''")
print(has_33([1, 3, 1, 3]))
print(has_33([1, 3, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original
# there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    mylist = [i * 3 for i in text]
    return ' '.join(mylist)


print("''''''''''''''''''''''''")
print(paper_doll("Hello"))
print(paper_doll('Mississippi'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a, b, c):
    reduced_value = 0
    for i in a, b, c:
        if sum([a + b + c]) <= 21:
            return a + b + c
        elif sum([a + b + c]) > 21 and ((a == 11) or (b == 11) or (c == 11)):

            reduced_value = sum([a + b + c]) - 10
            return reduced_value

        elif reduced_value > 21:
            pass
    return "BUST"


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
    my_list = 0
    if not arr:
        return 0
    for nums in arr:
        if nums <= 5 or nums > 9:
            my_list += nums
    return my_list


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# SPY GAME: Write a function that takes in a list of integers and
# returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    counter = 0
    for i in nums:
        if i == 0:
            counter += 1
        if i == 7 and counter == 2:
            return True
    return False

print('SPY GAMES')
print(spy_game([0, 2, 4, 0, 0, 7,0]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to
# and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.


def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


def count_primes3(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


def count_primes(num):
    primes = [2]
    candidates = 3
    if num < 2:
        return 0
    while candidates <= num:
        for items in range(3, candidates, 2):
            if candidates % items == 0:
                candidates += 2
                break
        else:
            primes.append(candidates)
            candidates += 2
    print(primes)
    return len(primes)


print("''''''''''''''''''''''''")
print(count_primes(0))
print(count_primes(1))
print(count_primes(2))
print(count_primes(100))
