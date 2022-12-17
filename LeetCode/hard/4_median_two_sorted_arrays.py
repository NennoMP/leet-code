# https://leetcode.com/problems/median-of-two-sorted-arrays/

from math import floor
from typing import List

MAX_VALUE = (10 ** 6) + 1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result:float
        merged_array = []

        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while (i < m or j < n):
            val1 = (nums1[i] if i < m else MAX_VALUE)
            val2 = (nums2[j] if j < n else MAX_VALUE)

            if val1 < val2:
                merged_array.append(val1)
                i += 1
            else:
                merged_array.append(val2)
                j += 1

            len_merged = len(merged_array)
            if len_merged % 2 != 0:
                result = merged_array[floor(len_merged / 2)]
            else:
                result = (
                    merged_array[len_merged // 2 - 1]
                    + merged_array[len_merged // 2]
                ) / 2

        return result
    
