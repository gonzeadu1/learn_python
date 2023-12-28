def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0, 11)
    within_range = False


#     while not choice.isdigit() or not within_range:
#         choice = input("Pls, enter a number (0-10): ")
#         # digit check
#         if not choice.isdigit():
#             print("Sorry that is not a digit!")
#         # Range Check
#         if choice.isdigit():
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Number not within range!")
#                 within_range = False
#     return int(choice)
#
#
# print(user_choice())


# def display_game(game_list):
#     print("Here is the current list: ")
#
#
# print(display_game([0,1,2]))


def user_choice2():
    while True:
        choice = input("Pls, enter a number (0-10): ")

        # digit check
        if not choice.isdigit():
            print("Sorry that is not a digit!")

        # Range Check
        else:
            if int(choice) in range(0, 11):
                return int(choice)
            else:
                print("Number not within range!")


print(user_choice2())



