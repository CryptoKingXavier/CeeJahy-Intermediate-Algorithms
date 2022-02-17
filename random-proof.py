import random, math

a, b, c = 6, 8, 9
n = 3

while True:
    print(f"Gap Size is: {math.pow(c, n) - (math.pow(a, n) + math.pow(b, n))}")
    print(f"a -> {a}, b -> {b}, c -> {c}")
    n += 1
