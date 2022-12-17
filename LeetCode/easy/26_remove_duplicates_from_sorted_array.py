# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


"""Two-pointer based solution."""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        insert_index = 1
        for v in nums[1:]:
            # Found a unique element
            if nums[insert_index - 1] != v:
                nums[insert_index] = v
                insert_index += 1

        return insert_index