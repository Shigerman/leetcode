# 118 Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle
# In Pascal's triangle, each number is the sum of the two numbers directly above it

from typing import List


def generate(numRows: int) -> List[List[int]]:
    result = []
    corner_cases = {1:[[1]], 2:[[1,1]]}

    for num in range(1, numRows + 1):
        if num in corner_cases:
            result.extend(corner_cases[num])
        else:
            # add the first un-changeable element at the beginning
            current_row = [1]

            # create the changeable part
            upper_row = result[num - 2]
            for i in range(len(upper_row) - 1):
                current_row.append(upper_row[i] + upper_row[i + 1])

            # add the last un-changeable element at the end
            current_row.append(1)

            result.extend([current_row])
    return result


assert generate(1) == [[1]]
assert generate(2) == [[1],[1,1]]
assert generate(3) == [[1],[1,1], [1,2,1]]
assert generate(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
