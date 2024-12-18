def is_prime(number):
    for i in range(2, int(1 + number** 0.5)):
        if number % i == 0:
            return False
    return True

for ii in range(1, 20):
    if is_prime(ii + 1):
        print(ii + 1, end=" ")
print()
