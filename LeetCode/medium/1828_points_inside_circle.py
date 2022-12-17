# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result: List[int] = []

        points.sort(key=lambda x: x[0])
        
        for q in queries:
            count = 0
            center_x, center_y, radius = q
            for p in points:
                x, y = p
                if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                    count += 1
            result.append(count)

        return result