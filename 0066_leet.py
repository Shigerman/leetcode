# 66 Plus One

# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are
# ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    position = -1

    while True:
        if abs(position) > len(digits):
            digits.insert(0, 1)
            return digits
        if digits[position] != 9:
            digits[position] += 1 
            return digits
        else:
            digits[position] = 0
            position -= 1


assert plusOne([1,2,3]) == [1,2,4]
assert plusOne([4,3,2,1]) == [4,3,2,2]
assert plusOne([9, 9]) == [1,0,0]
assert plusOne([9]) == [1,0]
