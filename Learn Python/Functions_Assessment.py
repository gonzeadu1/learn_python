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
    return var


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
