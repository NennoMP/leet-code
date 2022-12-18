# https://leetcode.com/problems/climbing-stairs/

from functools import lru_cache


"Iterative solution."
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1

        x1, x2 = 1, 1
        for _ in range(n-1):
            result = x2 + x1
            x1 = x2
            x2 = result

        return result


"""Recursive solution with memoization."""
class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {0: 1, 1: 1}
        def climbingStairsRec(n: int, memo: dict) -> int:
            if n not in memo:
                memo[n] = climbingStairsRec(n-1, memo) + climbingStairsRec(n-2, memo)
            return memo[n]

        return climbingStairsRec(n, memo)


"""Recursive solution with memoization using @cache decorator."""
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def climbingStairsRec(n: int) -> int:
            return 1 if n <= 1 else climbingStairsRec(n-1) + climbingStairsRec(n-2)

        return climbingStairsRec(n)
