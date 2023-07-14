
# algorithm:
# use & operator
# 1&1=1, 1&0=0: use this logic to check if 1 is there
# shift right

def no_of_1_bits(n):
    res = 0
    i = 0
    while i < 32:
        if (n & 1) == 1:
            res += 1
        n >>= 1
        i += 1
    return res


print(no_of_1_bits(int('00000000000000000000000000001011', 2)))  # prints 3
