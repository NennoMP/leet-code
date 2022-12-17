# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        reversed_list = digits[::-1] # reverse the list

        for i, v in enumerate(reversed_list):
            # If a 9 we propagate the remainder to next digit
            if v == 9:
                reversed_list[i] = 0
                # If last digit append 1 as remainder
                if i == n - 1:
                    reversed_list.append(1)
                    return reversed_list[::-1]
            # If not a 9 we just increment
            else:
                reversed_list[i] += 1
                return reversed_list[::-1]