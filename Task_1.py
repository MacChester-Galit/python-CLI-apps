# Simple Calculator App

num1 = input("Enter the first number: ")
try:
    num1 = float(num1)
except ValueError:
    print("Please enter a valid number.")


num2 = input("Enter the first number: ")
try:
    num2 = float(num2)
except ValueError:
    print("Please enter a valid number.")

the_operation = input("Chooose what kind of operation you'll be using:\n"
"+ for addition\n"
"- for subtraction\n"
"* for multiplication\n"
"/ for division\n"
"Your operation: ")

match the_operation:
    case "+":
        the_sum = num1 + num2
        print(the_sum)
    case "-":
        the_difference = num1 - num2
        print(the_difference)
    case "*":
        the_product = num1 * num2
        print(the_product)
    case "/":
        if num2 == 0.0:
            print("Division by 0 is not allowed. Please use a positive number")
        else:
            the_quotient = num1 / num2
            print(the_quotient)
    case err:
        print("Invalid operation. Please use a valid operation in the list.")