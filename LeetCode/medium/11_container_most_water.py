# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        n = len(height)
        left = 0    # L index
        right = n-1 # R index
        while left < right:
            b = right - left                     # base
            h = min(height[left], height[right]) # height
            max_area = max(max_area, b*h)        # area: base*height

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
