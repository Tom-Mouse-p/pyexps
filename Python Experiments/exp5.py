print("Sets :)")
go_on = True
a = set([i for i in input("Enter string 1 > ").lower()])
b = set([i for i in input("Enter string 2 > ").lower()])
while go_on:
    choice = int(input("1. Change Strings\n2. See common elements\n3. See difference\n4. See Union\n5. See Symmetric "
                       "difference\n6. Exit\n> "))
    if choice == 1:
        a = set([i for i in input("Enter string 1 > ").lower()])
        b = set([i for i in input("Enter string 2 > ").lower()])
    elif choice == 2:
        print(a.intersection(b))
    elif choice == 3:
        print(a.difference(b))
    elif choice == 4:
        print(a.union(b))
    elif choice == 5:
        print(a.symmetric_difference(b))
    elif choice == 6:
        go_on = False
