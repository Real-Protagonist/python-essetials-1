hat_list = [1, 2, 3, 4, 5]

number = int(input("Number to replace: "))

hat_list[2] = number

del hat_list[-1]

print(len(hat_list))

print(hat_list)
