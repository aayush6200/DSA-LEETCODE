# algorithm
# shift res
# compute of with res and & with n
# shift n


def reverse_bits(n):
    res = 0
    i = 0

    while i < 32:
        res <<= 1
        res |= (n & 1)
        n >>= 1
        i += 1
    return res


# prints 00111001011110000010100101000000  which is 964176192
print(reverse_bits(int('00000010100101000001111010011100', 2)))
