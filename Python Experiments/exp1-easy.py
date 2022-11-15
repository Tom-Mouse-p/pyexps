import sys

# Taking input from commandline
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Swapping Numbers
print(f"Original Numbers\nNumber 1: {num1}, Number 2: {num2}\n")
num1 += num2
num2 = num1 - num2
num1 -= num2
print(f"Swapped Numbers\nNumber 1: {num1}, Number 2: {num2}\n")

# check if positive or negative
if num1 == 0:
    print(f"{num1} is zero (0).")
elif num1 > 0:
    print(f"{num1} is positive(+ve).")
else:
    print(f"{num1} is negative(-ve).")

# To run the program, type in format "python3 file_name 2_numbers"
# eg: python3 exp1-easy.py 77 88

