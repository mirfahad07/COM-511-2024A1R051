#write a python program to store repeated values in a tuple and count how many times a given value appears

n = int(input("Enter number of elements: "))

values = []

for i in range(n):
    num = int(input("Enter value: "))
    values.append(num)

numbers = tuple(values)

value = int(input("Enter value to count: "))

count = 0

for num in numbers:
    if num == value:
        count += 1

print("Tuple:", numbers)
print("The value appears", count, "times.")
