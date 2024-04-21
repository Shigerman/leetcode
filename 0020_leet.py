# 20 Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    while True:
        if "[]" in s or "()" in s or "{}" in s:
            s = s.replace("[]", "")
            s = s.replace("()", "")
            s = s.replace("{}", "")
            continue
        break
    if not s:
        return True
    return False


assert isValid("()") == True
assert isValid("{[]}") == True
assert isValid("()[]{}") == True
assert isValid("(([]){})") == True
assert isValid("(]") == False
assert isValid("([)]") == False
