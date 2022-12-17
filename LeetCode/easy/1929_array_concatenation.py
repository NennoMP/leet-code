# https://leetcode.com/problems/concatenation-of-array/

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result: List[int] = []

        n = len(nums)
        for i, v in enumerate(nums):
            result.insert(i, v)
            result.insert(i + n, v)

        return result