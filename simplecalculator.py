from random import choice


def simplecalculator():
    print("Choose an operator :")
    print("(+)")
    print("(-)")
    print("(*)")
    print("(/)")

    choice = input("Enter operator (): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))

        if choice == '+' :
            print("The sum is:", (num1 + num2))
        elif choice == '-' :
            print("The difference is:", (num1 - num2) )
        elif choice == '*' :
            print("The product is: ", (num1 * num2))
        elif choice == '/' :
            if num2 =='0':
                print("The result is: ", (num1 / num2))
            else :
                print("Error: Division by zero is invalid")
    else:
        print("Invalid operator")
simplecalculator()








