from sci import operations

go_on = True

while go_on:
    a, b = map(int, input("Enter 2 numbers > ").split())
    op = operations.Operators(a, b)
    choice = int(input("1. Add both    2. Add with 3rd\n3. Subtract    4. Multiply\n5. Divide      6. Floor "
                       "Division\n7. "
                       "Reminder    8. Exponent\n9. Root        10. Log            11. Exit\n > "))
    if choice == 1:
        op.add()
    elif choice == 2:
        op.add(int(input("3rd number > ")))
    elif choice == 3:
        op.subtraction()
    elif choice == 4:
        op.multiply()
    elif choice == 5:
        op.divide()
    elif choice == 6:
        op.floordiv()
    elif choice == 7:
        op.mod()
    elif choice == 8:
        op.exponent()
    elif choice == 9:
        op.root()
    elif choice == 10:
        op.log()
    elif choice == 11:
        go_on = False
