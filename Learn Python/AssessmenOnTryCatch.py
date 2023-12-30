# Assessment
# Handle the exception thrown by the code below by using try and except blocks.
# Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("unsupported operand type(s) for ** or pow(): 'str' and 'int")
finally:
    print("Testing Try/catch/finally")

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("division by zero!")
finally:
    print("All Done.")


# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    # waiting = True
    while True:  # while waiting
        try:
            number = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is {number ** 2}")
            # waiting = False
            break


ask()
