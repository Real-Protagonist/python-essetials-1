temps = [[0.0 for h in range(24)] for d in range(31)]

# Monthly average noon temperature
total = 0.0

for day in temps:
    total += day[11]

average = total / 31
print("Average temperature at noon: ", average)

# Find the highest temperature during the whole month
highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was: ", highest)

# Count the days when the temperature at noon was at least 20 ºC
hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, " days were hot.")
