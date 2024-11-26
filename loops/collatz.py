c0 = int(input())

steps = 0

print()
while c0 != 1:
    steps += 1
    if (c0 % 2 == 0):
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))

print("steps = ", steps)

word = "python"
for letter in word:
    print(letter, end="*")
