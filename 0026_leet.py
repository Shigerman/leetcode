# 26 Remove duplicates from sorted array

# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain the
# unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.

# Return k.

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    unique_elements = 0
    for elem in nums:
        unique_elements += 1
        elem_in_nums = nums.count(elem)
        if elem_in_nums > 1:
            for _ in range(elem_in_nums - 1):
                nums.remove(elem)
    return unique_elements


assert removeDuplicates([1,1,2]) == 2 
assert removeDuplicates([2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 2
assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
