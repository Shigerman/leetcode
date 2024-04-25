# 70 Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

from functools import cache


def climbStairs(n: int) -> int:
    @cache
    def fibonacci(n: int) -> int:
        corner_cases = {0: 0, 1: 1, 2: 2, 3: 3}
        if n in corner_cases:
            return corner_cases[n]
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n)


assert climbStairs(0) == 0
assert climbStairs(1) == 1
assert climbStairs(2) == 2
assert climbStairs(3) == 3
assert climbStairs(4) == 5
assert climbStairs(5) == 8
assert climbStairs(6) == 13
assert climbStairs(7) == 21
assert climbStairs(8) == 34
assert climbStairs(9) == 55
assert climbStairs(10) == 89
assert climbStairs(38) == 63245986
