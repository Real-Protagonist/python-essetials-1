numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

# Adding in the and of the list
numbers.append(4)

print(len(numbers))
print(numbers)

# Adding in a spacific location in the list, zero position in case
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

# Adding 333 in the position 1 in the list
numbers.insert(1, 333)
print(numbers)

# Starting with a new and empty list
my_list = []

for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)

my_list = []

for i in range(5):
    my_list.append(i + 1)
print(my_list)
