go_on = True

while go_on:

    print()
    # Menu to choose operations
    print("Choose an option from the menu")
    print("1 : Check For Palindrome\n2 : Calculate Factorial\n3 : Exit")
    option_chosen = int(input("Enter an option > "))

    # Parsing the input
    if option_chosen == 1:
        # Palindrome
        string = input("Enter a string > ")
        n = int(len(string) / 2)
        string2 = string[0:n]
        string3 = string[len(string) - n:]
        rev_string3 = string3[len(string3)::-1]

        if string2.lower() == rev_string3.lower():
            print("Palindrome!")
        else:
            print("Not A Palindrome!")

    elif option_chosen == 2:
        # Factorial
        number = int(input("Enter a number > "))
        if number == 0:
            print("Factorial = ", number)
        elif number > 0:
            factorial = 1
            for i in range(1, (number + 1)):
                factorial *= i
            print("Factorial of ", number, " is ", factorial)
        elif number < 0:
            print("For calculation of factorial number must be +ve or zero(0), you entered a -ve number : ", number)
        else:
            print("Something went wrong")
    elif option_chosen == 3:
        # Exit
        go_on = False
