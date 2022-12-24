# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        return sorted(arr, key=lambda x: bin(x).count('1'))