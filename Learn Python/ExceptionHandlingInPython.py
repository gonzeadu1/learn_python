# Trying to write a file while reading instead will generate OSError
try:
    f = open('testfile', 'r')
    f.write("I am trying to figure what I am doing")
    f.close()
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey, you have an OS Error!")
finally:
    print("I always run.")


def ask_for_int():
    while True:
        try:
            result = int(input("Pls, provide a number: "))
            print(f"The number you added is: {result}")
        except:  # TypeError:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        # finally:
        #     print("End of try/catch/finally")


ask_for_int()
