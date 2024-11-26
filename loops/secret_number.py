secret_number = 777

print(
"""
+===============================+
| Welcome to my game, muggle!   |
| Enter an integer number       |
| and guess what number I've    |
| picked for you.               |
| So, what is the secret number |
+===============================+
"""
)

number = int(input("Enter the number: "))

while secret_number != number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter the number: "))
print("Secret Number: ", secret_number)
print("Well done, muggle! You are free now.")
