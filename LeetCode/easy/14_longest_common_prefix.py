# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = ""
            
        n = len(strs)
        min_len = len(min(strs, key=len))
        tmp: str = ""
        
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
            
        for i in range(min_len):
            for j in range(n-1):
                tmp = strs[j][i]
                if strs[j][i] != strs[j+1][i]:
                    return result
            result += tmp
            
        return result