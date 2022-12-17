# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for o in operations:
            if o[1] == '+':
                result += 1
            else:
                result -= 1

        return result

