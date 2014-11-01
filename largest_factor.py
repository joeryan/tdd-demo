import pytest

def largest_factor(x):
    if x <= 1:
        raise ValueError
    if x % 1 != 0:
        raise ValueError

    divisor = 2
    while x > 1:
        quotient, remainder = divmod(x, divisor)
        if remainder == 0:
            x = quotient
        else:
            divisor += 1
    return divisor
