limit = int(input("Enter a upper limit number > ")) + 1

# Making Even & Odd List
even_list = []
odd_list = []

for n in range(0, limit, 2):
    even_list.append(n)
for n in range(1, limit, 2):
    odd_list.append(n)

print("Even list : ", even_list, "\nOdd list : ", odd_list, "\n")

# merging both lists and sorting
merged_list = even_list + odd_list
print("Merged list : ", merged_list)
merged_list.sort()
print("Sorted list : ", merged_list, "\n")

# Taking Input for x and adding it to start
x = input("Enter a value for x > ")
# merged_list.insert(0, x)
merged_list[0] = x
print("Value of x inserted at start : ", merged_list)

for i in range(0, len(merged_list)):
    merged_list[i] = str(merged_list[i])

# Popping the middle element in list
middle = int(len(merged_list) / 2)
merged_list.pop(middle)
print("Popped the middle element : ", merged_list)

# Printing Min and Max value from the list
print("Max value : ", max(merged_list), "\nMin value : ", min(merged_list), "\n")

# Taking input for n elements and adding to list
n = int(input("Enter the number of names you want to enter in list > "))
for i in range(0, n):
    merged_list.append(input("Enter ", i, "th element > "))
print("Entered all values in list : ", merged_list)

# Searching for word 'python'
if 'python' in merged_list:
    print("'python' is found at index ", merged_list.index("python"))
else:
    print("'python' not found in the list")
