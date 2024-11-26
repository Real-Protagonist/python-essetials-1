year = int(input("Enter the a gregorian year:"))

if year % 4 == 0:
    txt = "Common year"
elif year % 100 != 0:
    txt = "Leap year"
elif year % 400 != 0:
    txt = "common year"
elif year < 1582:
    txt = "Not within the Gregorian calendar period"

print(txt)
