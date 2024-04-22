# 28 Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    haystack_positions = range(len(haystack))
    for element_number in haystack_positions:
        if haystack[element_number] == needle[0]:
            probable_needle_end = element_number+len(needle)
            if haystack[element_number:probable_needle_end] == needle:
                return element_number


assert strStr("sadbutsad", "sad") == 0
assert strStr("leetcode", "leeto") == -1
