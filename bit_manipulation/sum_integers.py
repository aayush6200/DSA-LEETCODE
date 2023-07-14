
import math


def sum_integers(a, b):
    return int(math.log(math.exp(a)*math.exp(b))) if a != 0 and b != 0 else a or b


print(sum_integers(3, 4))  # prints 7
