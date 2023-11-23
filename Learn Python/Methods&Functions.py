from random import shuffle

mylist = [3, 3, 4, 4, 5, 5]
mylist.pop()
print(mylist)


# help function
# help(mylist)


def name_of_function(num1, num2):
    # Trying to write a comment
    print(num1 * num2)
    return num1 + num2


result = name_of_function(1, 3)
print(result)


def say_hello():
    print("Hello how are you ")
    print("what's up babe?")


def say_hello(name='Default'):
    print(f'Hello {name}')


def add_num(num1, num2):
    return num1 + num2


result = add_num(3, 9)

print(result)

add_num(68, 9)


def even_check(number):
    return number % 2 == 0


print(even_check(45))


def check_even_list(num_list):
    #     placeHolder
    place_holder_list = []
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


my_list = [1, 3, 5]
my_list1 = [2, 4, 5]
my_list2 = [1, 1, 1, 1]
print(check_even_list([9, 1, 7, 5]))


def check_even_list(num_list):
    even_num = []
    for num in num_list:
        if num % 2 == 0:
            even_num.append(num)
        else:
            pass
    return even_num


print(check_even_list([1, 3, 43, 4, 5, 6, 7, 7, 6, 55]))


def check_even_list(number_list):
    list_comprehension = [num for num in number_list if num % 2 == 0]
    return list_comprehension


print(check_even_list([3, 4, 5, 6, 7, 7]))


# Tuple unpacking in functions/methods
def employee_of_the_month_check(wells_Fargo_employees):
    max_hour = 0
    employee_of_the_month = ''
    for employee, hour in wells_Fargo_employees:
        if hour > max_hour:
            max_hour = hour
            employee_of_the_month = employee
        else:
            pass
    return employee_of_the_month, max_hour


work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]
print("Printing out as a single item:", employee_of_the_month_check(work_hours))
name, hours = employee_of_the_month_check(work_hours)
print("printing name and hours:", name, hours)
print("Printing name only:", name)
print("Printing hours only:", hours)

mylist = [2, 3, 4, 4, 5, ]
print(mylist[::-2])

# interacting between functions
my_list_example = [1, 2, 3, 4, 5, 6, 7, 8, 4, 2, 1]
shuffle(my_list_example)
print("The shuffled list is:", my_list_example)


# print(shuffle_list(my_list_example))

# mylist_game = ['', 'O', '']
# print("This is my shuffled list: ", shuffle_list(shuffle_list(mylist_game)))

def shuffle_list(my_list_):
    shuffle(my_list_)
    return my_list_


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)


# print(player_guess())
# myindex = player_guess()
# print(myindex, "<===My index")
def check_guess(mylist, guess):
    if mylist[guess] == 0:
        print("correct")
    else:
        print("Wrong guess!")
        print(mylist)


# INITIAL LIST
mylist = ['', 'O', '']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
print("The result is: ")
check_guess(mixedup_list, guess)
