while True:
    the_num = input("Enter a number: ")
    try:
        the_num = int(the_num)
        if the_num % 2 == 0:
            print("The number you entered: " + str(the_num) + " " + "is even.")
        else:
            print("The number you entered: " + str(the_num) + " " + "is odd.")
        break
    except ValueError:
        print("Invalid input. Please enter a number.")