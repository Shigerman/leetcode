# 67 Add Binary

# Given two binary strings a and b, return their sum as a binary string


def addBinary(a: str, b: str) -> str:
    # add leading zeros to a shorter binary string to avoid IndexError
    difference = abs(len(b) - len(a))
    if len(a) < len(b):
        a = ("0" * difference) + a
    else:
        b = ("0" * difference) + b

    sum = list("0" * len(a))
    position = -1
    carry = 0

    while True:
        if abs(position) > len(a):
            if carry == 1:
                sum.insert(0, "1")
            return "".join(sum)
        if a[position] != b[position]:  # combination 1 and 0
            if carry == 1:
                sum[position] = "0"
            else:
                sum[position] = "1"
        if a[position] == b[position] == "0":
            if carry == 1:
                sum[position] = "1"
                carry = 0
            else:
                sum[position] = "0"
        if a[position] == b[position] == "1":
            if carry == 1:
                sum[position] = "1"
            else:
                sum[position] = "0"
                carry = 1
        position -= 1


assert addBinary("0", "0") == "0"
assert addBinary("1", "1") == "10"
assert addBinary("11", "10") == "101"
assert addBinary("11", "11") == "110"
assert addBinary("11", "1") == "100"
assert addBinary("111", "1") == "1000"
assert addBinary("11111", "1") == "100000"
assert addBinary("1010", "1011") == "10101"
assert addBinary("100", "110010") == "110110"
