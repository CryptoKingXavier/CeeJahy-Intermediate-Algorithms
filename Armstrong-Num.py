import math

armstrong_num = []

def armstrongCheck(num):
    global armstrong_num
    product = 0
    for value in str(num):
        product = product + math.pow(int(value), len(str(num)))
    print(f"Product is {product}")
    if product == num:
        print(f"-> {num} is an Armstrong Number")
        armstrong_num.append(num)
    else:
        print(f"-> {num} isn't an Armstrong Number")


num = list(range(370, 1635, 1))
for n in num:
    armstrongCheck(n)

print()
mySet = set(armstrong_num)
print(mySet)