def func():
    return 1


func()


def hello():
    return "hello"


hello()

greet = hello

print(greet())


def hello(name='Jose'):
    print("The hello function has been executed")

    def greet():
        return '\t This is the greet function inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print("Return a function!")
    if name == 'Jose':
        return greet
    else:
        return welcome

    # print(greet())
    # print(welcome())
    # print("This is the end of the Hello() function")


my_new_func = hello('Jose')
my_new_func.__str__()

print(my_new_func)


# RETUrning a function in a function
def cool():
    def super_cool():
        return 'I am very cool'

    return super_cool


some_func = cool()
print(some_func)
some_func()


# Passing function as an argument in another function
def hello():
    return 'Hi Josie!'


def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())


print('==============================')
print(hello)
print('++++++++++++++++++++++++++++++')
print(hello())

print(other(hello))


# print(hello())

# Python Generators
def create_cubes(n):
    for x in range(n):
        yield x ** 3


for x in create_cubes(10):
    print(x)


def gen_fibon(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibon(10):
    print(number)

