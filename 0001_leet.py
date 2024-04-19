# 1 Two Sum

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# ========================================
# This is a problem about matrix and nested loops
# Inner cycle: range start should be index1+1 from the outer loop.
# It's a well-known trick not to repeat operations (6 operations instead of 16)
# With this range start we do not need to check if an element is
# comapared with itself: it does not happen.


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    len_nums = len(nums)

    for index1 in range(len_nums):
        for index2 in range(index1 + 1, len_nums):
            if nums[index1] + nums[index2] == target:
                return[index1, index2]


assert twoSum([3, 3], 6) == [0,1]
assert twoSum([3, 2, 4], 6) == [1,2]
assert twoSum([2,7,11,15], 9) == [0,1]
