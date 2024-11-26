my_list = [10, 1, 8, 3, 5]
leng = len(my_list)

for i in range(leng // 2):
    my_list[i], my_list[leng - i - 1] = my_list[leng - i - 1], my_list[i]

print(my_list)
