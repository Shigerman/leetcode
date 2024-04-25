# 69 Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1

    low = 0
    high = x
    while True:
        mid = (low + high) // 2
        guess = mid * mid
        if guess == x:
            return mid
        if guess < x:
            low = mid
        else:
            high = mid
        if high - low == 1:
            return low


assert mySqrt(0) == 0
assert mySqrt(1) == 1
assert mySqrt(2) == 1
assert mySqrt(3) == 1
assert mySqrt(4) == 2
assert mySqrt(8) == 2
assert mySqrt(9) == 3
assert mySqrt(14) == 3
assert mySqrt(60) == 7
assert mySqrt(600) == 24
assert mySqrt(2000) == 44
