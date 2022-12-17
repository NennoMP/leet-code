# https://leetcode.com/problems/search-insert-position/

from math import floor
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def searchInsertAux(nums, target):
            n = len(nums)           # Size
            m = floor(n / 2)   # Middle element

            # Base case
            if nums[m] == target:
                return m

            # Array exausted
            if (n <= 2):
                if nums[m] > target:
                    return m - 1 if m != 0 and nums[m-1] >= target else m
                elif nums[m] < target:
                    return m + 1

            # Recursive calls
            if nums[m] > target:
                return searchInsertAux(nums[:m], target)
            elif nums[m] < target:
                return (m + 1) + searchInsertAux(nums[(m+1):n], target)

        return searchInsertAux(nums, target)
