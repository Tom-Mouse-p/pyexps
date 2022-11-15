import sys


def swap_numbers():
    global num1, num2
    print(f"Original Numbers\nNumber 1: {num1}, Number 2: {num2}\n")
    num1 += num2
    num2 = num1 - num2
    num1 -= num2
    print(f"Swapped Numbers\nNumber 1: {num1}, Number 2: {num2}\n")


def check_character():
    if num1 == 0:
        print(f"{num1} is zero (0).")
    elif num1 > 0:
        print(f"{num1} is positive(+ve).")
    else:
        print(f"{num1} is negative(-ve).")


# Taking input from commandline
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Calling functions to swap the number and then checking the first number is Positive, Negative or Zero
swap_numbers()
check_character()
print()
