#write a python program to check whether a given value is present in a a tuple. Ifpresent, display its position

n = int(input("Enter number of elements: "))

values = []

for i in range(n):
    num = int(input("Enter value: "))
    values.append(num)

my_tuple = tuple(values)

value = int(input("Enter value to search: "))

if value in my_tuple:
    position = my_tuple.index(value)
    print("Value is present at position:", position)
else:
    print("Value is not present in the tuple.")
