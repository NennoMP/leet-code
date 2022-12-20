# https://leetcode.com/problems/counting-bits/

from typing import List

"""Built-in functions based solution.
   - TIME: O(n*b), where b is the number of bits iterated by the 'count'    
           built-in function
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]


"""Dynamic programming based solution."""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1, n+1):
            ans[i] = ans[i//2] if i % 2 == 0 else ans[i-1] + 1
        return ans


"""Bit manipulation based solution.
   - TIME: O(n*b)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ones = 0
            # Shift to the right until i becomes 0
            while i:
                # If least significant bit of i is 1, increment counter
                if i & 1:
                    ones += 1
                # Shift i to the right by 1 bit
                i >>= 1
            ans.append(ones)
        return ans
