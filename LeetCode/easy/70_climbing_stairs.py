# https://leetcode.com/problems/climbing-stairs/


"Fibonacci numbers based solution."
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
