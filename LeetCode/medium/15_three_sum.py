# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]

        n = len(nums)
        if n < 3:
            return result

        nums.sort()
        i = 0
        k = n-1
        while i < k:
            if nums[i] + nums[i+1] + nums[k] == 0:
                result.append([nums[i],nums[i+1],nums[k]])
                i += 1
            elif nums[i] + nums[i+1] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[i+1] + nums[k] < 0:
                i += 1 

        return result


