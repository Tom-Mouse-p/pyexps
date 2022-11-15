class Employee:
    def __int__(self, identity='', name='', salary=0):
        self.identity = identity
        self.name = name
        self.salary = salary

    def read(self):
        return self.identity, self.name, self.salary


d = []
go_on = True
while go_on:

    choice = int(input("1. Create Employee\n2. See Employee Details\n3. Modify Employee Details\n4. Exit\n> "))

    if choice == 1:
        n = int(input("Enter the number of Employees to add\n> "))
        for i in range(n):
            temp_employee = Employee()
            print(f"Employee no. {len(d) + 1}")
            temp_employee.identity = input("Assign Id > ")
            temp_employee.name = input("Name > ")
            temp_employee.salary = int(input("Salary > "))
            d.append(temp_employee)

    elif choice == 2:
        for i in range(len(d)):
            print(i + 1, d[i].read())

    elif choice == 3:
        t = int(input("Enter Employee Number\n> "))
        t = t - 1
        print(f"{t + 1}: {d[t].read()}\n1. Change Identity Number\n2. Change Name\n3. Change "
              f"Salary")
        change = int(input("> "))
        if change == 1:
            d[t].identity = input("New Id > ")
        elif change == 2:
            d[t].name = input("New Name >")
        elif change == 3:
            d[t].salary = int(input("New Salary > "))
        print((t + 1), d[t].read())

    elif choice == 4:
        go_on = False

    print("-----------")
