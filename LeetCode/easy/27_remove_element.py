# https://leetcode.com/problems/remove-element/description/

from typing import List


"Two-pointer based solution."
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        insert_index = 0
        for v in nums:
            if v != val:
                nums[insert_index] = v
                insert_index += 1

        return insert_index
