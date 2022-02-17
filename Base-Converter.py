def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n//2)
    print(n % 2, end='')

def binary_to_dec(n):
    import math
    n = str(n)
    length = len(n)
    byte_gen = []
    for number in n:
        if number == '1':
            byte_gen.append(int(number) * math.pow(2, length-1))
            length -= 1
        else:
            byte_gen.append(int(number))
            length -= 1
    num_eval = 0
    for i in byte_gen:
        num_eval += int(i)
    print(num_eval)

num_1 = int(input('Enter number to convert to binary: '))
dec_to_binary(num_1)
print()
num_2 = int(input('Enter binary number to convert to denary: '))
binary_to_dec(num_2)