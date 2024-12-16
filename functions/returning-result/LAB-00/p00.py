def is_leap_year(yr):
    if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
        return True

test_data = [1900, 2000, 2016, 1987, 2023, 2024]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_leap_year(yr)
    if result:
        print("OK")
    else:
        print("Failed")
