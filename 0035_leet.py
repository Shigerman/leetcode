# 35 Search Insert Position

# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the
# index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target > nums[-1]:  # should stand the last in nums
        return len(nums)
    if target < nums[0]:  # should stand the first in nums
        return 0

    low = 0
    high = len(nums) - 1
    while True:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid  # this target is found in the nums
        if guess < target:
            low = mid
        else:
            high = mid
        if nums[low] == target:
            return low  # this target is found in the first half of nums
        if high - low == 1:
            return high # this target should be in nums


assert searchInsert([1,3,5], 0) == 0
assert searchInsert([1,3,5,6], 2) == 1
assert searchInsert([1,3,5,6], 5) == 2
assert searchInsert([1,3,5,6], 7) == 4
assert searchInsert([1,3,6,7,8,9,10,12,13,15,20,22], 14) == 9
