# 9 Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# =========================================================================
# this problem has two solutions: a string solution and a non-string-solution


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True

    """x = str(x)
    middle = len(x) // 2
    for i in range(middle):
        if x[i] != x[-(i+1)]:
            return False
    return True"""

    my_list = []

    while True:
        my_list.append(x % 10)
        x = x // 10
        if x < 10:
            my_list.append(x)
            break
        continue

    middle = len(my_list) // 2
    for i in range(middle):
        if my_list[i] != my_list[-(i+1)]:
            return False
    return True


assert isPalindrome(121) is True
assert isPalindrome(-121) is False
assert isPalindrome(5795579) is False
assert isPalindrome(123454321) is True
assert isPalindrome(456789010987654) is True
