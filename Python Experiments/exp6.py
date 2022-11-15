print("--Dictionary--")
oxford = {}
go_on = True

while go_on:
    choice = int(input("1: Create a key-value pair\n2: Edit an existing item\n3: Print a value\n4: Add a key-value "
                       "list to this dictionary\n5: Print dictionary\n5: Exit\n> "))
    if choice == 1:
        key, value = input("Enter a key and a value\n> ").strip().split(" ")
        temp = {key: value}
        oxford.update(temp)
        print("Added item.\n")
    elif choice == 2:
        wanted = input("Enter the key for which value is to be edited\n> ")
        found = oxford.get(wanted, -345)
        if found != -345:
            option = int(input("1: Update the value\n2: Concatenate Value\n3: Delete value\n4: Exit Operation."))
            if option == 1:
                update_value = input("Enter new value\n> ")
                updated_pair = {wanted: found}
                oxford.update(updated_pair)
                print("Updated\n")
            elif option == 2:
                updated_value = input(f"Concatenate your value\n> {found}")
                updated_pair = {wanted: updated_value}
                oxford.update(updated_pair)
                print("Updated\n")
            elif option == 3:
                updated_pair = {wanted: found}
                sure = input(f"Are you sure ypu wanted to delete '{updated_pair}?\n(Y/N) > ").strip()
                if sure == "y" or "Y":
                    del oxford[wanted]
                    print("Deleted")
                if sure == "n" or "N":
                    continue
            elif option == 4:
                continue

    elif choice == 3:
        wanted = input("Enter the key for which value is to be edited\n> ")
        found = oxford.get(wanted, -345)
        if found != -345:
            updated_pair = {wanted: found}
            print(updated_pair)
            print()

    elif choice == 4:
        keys = list(input("Enter all the keys in order\n> ").strip().split(" "))
        values = list(input("Enter all the values in order\n> ").strip().split(" "))
        pairs = dict(zip(keys, values))
        oxford.update(pairs)

    elif choice == 5:
        print(oxford)

    elif choice == 6:
        go_on = False
        print("Bye!")