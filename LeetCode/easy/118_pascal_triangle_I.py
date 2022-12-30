# https://leetcode.com/problems/pascals-triangle/

from typing import List


"""Dynamic programming - Iterative approach."""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] for _ in range(numRows)]

        for i in range(1, numRows):
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)

        return result


"""Dynamic programming - Recursive approach."""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def generateRec(row: int):
            if row == 1:
                return [[1]]

            result = generateRec(row-1)
            prev_row = result[-1] # previous row
            curr_row = [1]
            for i in range(len(prev_row)-1):
                curr_row.append(prev_row[i] + prev_row[i+1])
            curr_row.append(1)
            result.append(curr_row)

            return result
        
        return generateRec(numRows)