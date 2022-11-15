import os

go_on = True
while go_on:
    print()
    choice = int(input("1. Read and copy a file to another\n2. Append data to existing file\n3. See details of a "
                       "file\n4. Display all available files in directory\n5. Exit\n>  ").strip())
    if choice == 1:
        print("---reading file1.txt")
        with open("file1.txt", 'r') as file1:
            data = file1.read()
            print(data)
            with open('file2.txt', 'w+') as file2:
                file2.write(data)
                print("---copied text to file2.txt\n")
                print("---reading file2.txt")
                file2.seek(0)
                print(file2.read())

    if choice == 2:
        print("---Appending to file3.txt")
        with open('file3.txt', 'a+') as file3:
            file3.write(input("> ").strip())
            file3.write("\n")
            file3.seek(0)
            print("---done\n---updated file3.txt file: ")
            print(file3.read())

    if choice == 3:
        print("---reading file3.txt")
        with open('file3.txt', 'r') as file3:
            data = file3.read()
            file3.seek(0)
            print(f"Lines: {len(file3.readlines())}")
            print(f"Words: {len(data.split())}")
            print(f"Characters: {len(data) - 1}")

    if choice == 4:
        print("---files in current directory:")
        for f in os.listdir():
            if os.path.isfile(f):
                print("- ", f)
            else:
                print(f)
        print()

    if choice == 5:
        go_on = False
