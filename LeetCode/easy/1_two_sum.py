# https://leetcode.com/problems/two-sum/

from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap: dict = {}
            
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[v] = i
