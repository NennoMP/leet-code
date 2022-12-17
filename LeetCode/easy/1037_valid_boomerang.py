# https://leetcode.com/problems/valid-boomerang/

from math import sqrt
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = sqrt((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)   # side a
        b = sqrt((points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2)   # side b
        c = sqrt((points[1][0] - points[2][0])**2 + (points[1][1] - points[2][1])**2)   # side c


        p = (a + b + c) / 2 # perimeter
        try:
            area = sqrt(p*(p - a)*(p - b)*(p - c))  # area
        except ValueError:
            return False

        # Avoid edge case
        if area > 0.001:
            return True
        else:
            return False