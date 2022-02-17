def num_palindrome_check():
    from getpass import getpass
    _num = getpass("Enter your number: ")
    num = str(_num)
    rev_num = reversed(num)

    valid_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for char in num:
        if char not in valid_num:
            print("Invalid Syntax!")
            break

        else:
            pass


    if list(num) == list(rev_num):
        print(num + " is a palindromous number!")
    else:
        print(num + " isn't a palindromous number!")


while True:
    num_palindrome_check()
