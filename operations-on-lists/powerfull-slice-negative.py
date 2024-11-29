my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]

print(new_list)

# If the start specifies an element lying further tan the one described by the end (from the list's beginning, the slice will be empty

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]

print(new_list)

# If the start is omited, it's assumed that you want to get a slice beginning at the element with index 0
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]

print(new_list)
