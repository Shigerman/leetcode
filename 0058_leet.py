# 58 Length of Last Word

# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
# A word is a maximal substring consisting of non-space characters only.


def lengthOfLastWord(s: str) -> int:
    word_length = 0
    position = -1

    while True:
        if s[position].isalpha():
                word_length += 1
        else:
            if word_length > 0:
                return word_length
        if abs(position) == len(s):
            return word_length
        position -= 1

# second variant (runtime is longer):
# all_words = string.strip().split(" ")
# return len(all_words[-1])


assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
assert lengthOfLastWord("luffy is still joyboy") == 6
assert lengthOfLastWord("s") == 1
