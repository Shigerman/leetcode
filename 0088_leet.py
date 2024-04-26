# 88 Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in
# nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead
# be stored inside the array nums1. To accommodate this, nums1 has a length
# of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2
# has a length of n.

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    def insert_integer():
        low = 0
        high = m - 1
        while True:
            mid = (low + high) // 2
            guess = nums1[mid]
            if guess == num2:
                nums1.insert(mid, num2)
                nums1.pop(-1)
                return
            if guess < num2:
                low = mid
            else:
                high = mid
            if nums1[low] == num2:
                nums1.insert(low, num2)
                nums1.pop(-1)
                return
            if high - low == 1:
                nums1.insert(high, num2)
                nums1.pop(-1)
                return

    for num2 in nums2:
        if num2 >= nums1[m - 1]:
            nums1[-n] = num2
        elif num2 <= nums1[0]:
            nums1.insert(0, num2)
            nums1.pop(-1)
        else:
            insert_integer()
        n -= 1
        m += 1
    return nums1


assert merge([-1,0,3,0], 3, [1], 1) == [-1,0,1,3]
assert merge([-1,0,3,0], 3, [4], 1) == [-1,0,3,4]
# ================ in the list =======================
assert merge([2,3,0], 2, [2], 1) == [2,2,3]
assert merge([2,3,4,0], 3, [2], 1) == [2,2,3,4]
assert merge([2,3,4,5,0,0], 4, [2,3], 2) == [2,2,3,3,4,5]
assert merge([-1,0,3,0,], 3, [1], 1) == [-1,0,1,3]
# ================ not in the list====================#
assert merge([3,4,0], 2, [2], 1) == [2,3,4]
assert merge([2,4,0], 2, [3], 1) == [2,3,4]
assert merge([2,4,0], 2, [6], 1) == [2,4,6]
assert merge([-1,0,3,0,], 3, [1], 1) == [-1,0,1,3]
assert merge([3,4,0,0], 2, [2,6], 2) == [2,3,4,6]
assert merge([3,5,0,0,0], 2, [2,4,6], 3) == [2,3,4,5,6]
assert merge([3,4,0], 2, [6], 1) == [3,4,6]
assert merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3) == [-1,0,0,1,2,2,3,3,3]
assert merge([3,0,0,0,0,0], 1, [1,2,4,6,100], 5) == [1,2,3,4,6,100]
assert merge([-1,0,0,3,3,3,0,0], 6, [1,6], 2) == [-1,0,0,1,3,3,3,6]
# ============= bigger than min in list ===========
assert merge([1,2,3,0], 3, [4], 1) == [1,2,3,4]
assert merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
assert merge([-1,0,3,0,], 3, [6], 1) == [-1,0,3,6]
assert merge([-1,0,3,0,0], 3, [1,6], 2) == [-1,0,1,3,6]
# ================ corner cases ======================
assert merge([1], 1, [], 0) == [1]
assert merge([0], 0, [1], 1) == [1]
assert merge([0,0], 0, [1,2], 2) == [1,2]
# ================ mix ======================
assert merge([1,3,0], 2, [2], 1)
assert merge([1,3,0], 2, [0], 1)
assert merge([1,3,0], 2, [6], 1)
assert merge([1,3,0,0,0], 2, [0,4,8], 3)
assert merge([1,4,0,0], 2, [2,3], 2) == [1,2,3,4]
assert merge([1,3,0,0,0], 2, [0,3,8], 3) == [0,1,3,3,8]
assert merge([1,3,0,0,0,0,0], 2, [0,2,2,3,8], 5) == [0,1,2,2,3,3,8]
assert merge([1,3,6,8,9,10,15,21,24,270,0,0,0,0], 10, [0,4,8,12], 4) == [0,1,3,4,6,8,8,9,10,12,15,21,24,270]
