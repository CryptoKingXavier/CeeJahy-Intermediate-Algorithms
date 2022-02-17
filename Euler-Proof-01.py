print("This is a Euler Conjecture Variant!")
# Euler's Conjecture: a**2 + b**2 + c**2 == d**2
import random

def EulerConjecture():
    a = int(random.randint(0, 11))
    b = int(random.randint(0, 11))
    c = int(random.randint(0, 11))
    d = int(random.randint(0, 11))

    print(f"Combinations are: {a},{b},{c},{d}")
    
    if ((a**2 + b**2 + c**2) == (d**2)) and (a == b and a == c and a == d and b == c and b == d and c == d):
        print(f"The Sum of the Squares of: {a},{b},{c} = The Square of {d}")
    else:
        EulerConjecture()
                    

EulerConjecture()