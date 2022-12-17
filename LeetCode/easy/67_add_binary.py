# https://leetcode.com/problems/add-binary/

from itertools import zip_longest


"""Solution v1."""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a, 2) + int(b, 2)
        return format(result, 'b') # format to byte


"""Solution v2."""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a = a[::-1]
        b = b[::-1]

        overflow = 0
        # Iterate the two strings in parallel
        for v1, v2 in zip_longest(a, b, fillvalue=0):
            curr_sum = int(v1) + int(v2) + overflow
            mod = curr_sum % 2
            overflow = curr_sum // 2
            result += str(curr_sum % 2)

        # Add a 1 if overflow on last element
        if overflow:
            result += str(overflow)

        return result[::-1]