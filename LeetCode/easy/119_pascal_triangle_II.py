# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List


"""Dynamic programming - Iterative approach."""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        result = [[1] for _ in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
                
        return result[-1]


"""Dynamic programming - Recursive approach."""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def getRowRec(row: int):
            if row == 1:
                return [[1]]

            result = getRowRec(row-1)
            prev_row = result[-1] # previous row
            curr_row = [1]
            for i in range(len(prev_row)-1):
                curr_row.append(prev_row[i] + prev_row[i+1])
            curr_row.append(1)
            result.append(curr_row)

            return result
        
        return getRowRec(rowIndex+1)[-1]