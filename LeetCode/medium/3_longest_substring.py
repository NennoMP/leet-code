# https://leetcode.com/problems/longest-substring-without-repeating-characters/


"""Solution v1."""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        left    = 0
        right   = 0
        result  = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                
            result = max(result, right - left + 1)
            right += 1
            
        return result


"""Solution v2."""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        result = 0

        i = 0
        for j, v in enumerate(s):
            if v in hashmap:
                i = max(hashmap[v], i)

            result = max(result, j - i + 1)
            hashmap[v] = j + 1

        return result


"""Optimal solution."""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left    = 0
        right   = 0
        result  = 0
        
        while right < len(s):
            r = s[right]
            index = chars[ord(r)]
            
            if index != None and index >= left and index < right:
                left = index + 1

            result = max(result, right - left + 1)

            chars[ord(r)] = right
            right += 1
            
        return result
