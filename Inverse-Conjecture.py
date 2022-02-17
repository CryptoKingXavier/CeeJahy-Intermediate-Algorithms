import random

a = random.randint(1, 11)
b = random.randint(1, 11)

while (a != b):
    if (a * b) ** -1 == (a**-1 * b**-1):
        print(f"[{a} * {b}]^-1 = -> = [{a}^-1 * {b}^-1]")
    else:
        continue
    a = random.randint(1, 11)
    b = random.randint(1, 11)