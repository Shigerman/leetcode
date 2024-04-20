# 14 Longest Common Prefix

# Write a function to find the longest common prefix string
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    com_prefix = ""
    current_letter = ""

    for i in range(min(map(len, strs))):
        for word in strs:
            if strs.index(word) == 0:
                current_letter = word[i]
            if word[i] != current_letter:
                return com_prefix
        com_prefix += word[i]
        current_letter = ""
    return com_prefix


assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
